import json
from pathlib import Path
from enum import Enum

from .models import (
    DecisionTree,
    SellerPostShipmentLCDecision,
    DecisionTreeNode,
    NodeType,
)
from .models.client import ClientInfo, ClientRole, SellerPreShipmentLCDecision
from .extractor import Extractor
from .parser import MermaidDecisionTreeParser
from .session import ChatSession


class Chatbot:
    def __init__(self, openai_api_key: str):
        self.extractor = Extractor(openai_api_key=openai_api_key)
        self.parser = MermaidDecisionTreeParser()
        self.trees = {}  # Cache loaded trees
        self.decision_tree = None  # Current active tree

    def load_tree_by_name(self, tree_name: str) -> DecisionTree:
        """Load a specific decision tree by name."""
        if tree_name in self.trees:
            return self.trees[tree_name]

        tree_paths = {
            "lc_seller_preshipment": "src/decision_trees/lc_seller_preshipment.md",
            "lc_seller_postshipment": "src/decision_trees/lc_seller_postshipment.md",
            "lc_buyer_preshipment": "src/decision_trees/lc_buyer_preshipment.md",
        }

        if tree_name not in tree_paths:
            raise ValueError(f"Unknown tree: {tree_name}")

        tree_path = Path(tree_paths[tree_name])
        if not tree_path.exists():
            raise FileNotFoundError(f"Tree file not found: {tree_path}")

        tree_content = tree_path.read_text()
        tree = self.parser.parse_mermaid_to_decision_tree(tree_content, tree_name, "")
        self.trees[tree_name] = tree
        return tree

    # STEP 1: Process client input with LLM
    def process_client_input(self, client_text: str, session: ChatSession):
        """Step 1: Analyze client input with LLM using ClientInfo model."""
        try:
            # Use LLM to extract client information
            client_info = self.extractor.extract_with_context(
                client_text,
                ClientInfo,
                "Determine if the client is a buyer, seller, or both from their description.",
            )

            # Set role flags based on LLM result
            if client_info.role == ClientRole.BUYER:
                session.is_buyer = True
                session.role_determined = True
                self._setup_tree_sequence(session)
            elif client_info.role == ClientRole.SELLER:
                session.is_seller = True
                session.role_determined = True
                self._setup_tree_sequence(session)
            # If client_info.role is None, role_determined stays False for clarification

            # Update facts JSON
            self._update_facts_json(session, client_text)
            session.initial_processing_done = True

            return client_info

        except Exception as e:
            print(f"LLM analysis failed: {e}")
            # LLM failed - will need role clarification
            session.initial_processing_done = True
            self._update_facts_json(session, client_text)
            return ClientInfo(role=None)

    # STEP 2: Handle role determination with single question
    def get_role_clarification_question(self, session: ChatSession) -> dict:
        """Get role clarification question when role is unknown."""
        return {
            "type": "role_clarification",
            "question": "What is the company's role?",
            "options": [
                {"text": "I am a Seller/Exporter", "value": "seller"},
                {"text": "I am a Buyer/Importer", "value": "buyer"},
                {"text": "I am Both Buyer and Seller", "value": "both"},
            ],
        }

    def process_role_response(self, session: ChatSession, role_value: str) -> bool:
        """Process role selection and finalize role determination."""
        if role_value == "seller":
            session.is_seller = True
        elif role_value == "buyer":
            session.is_buyer = True
        elif role_value == "both":
            session.is_seller = True
            session.is_buyer = True
        else:
            return False

        # Finalize role determination and start trees
        session.role_determined = True
        self._setup_tree_sequence(session)
        self._update_facts_json(session)
        return True

    def _setup_tree_sequence(self, session: ChatSession):
        """Set up tree sequence based on roles."""
        trees = []
        if session.is_seller:
            trees.extend(["lc_seller_preshipment", "lc_seller_postshipment"])
        if session.is_buyer:
            trees.append("lc_buyer_preshipment")

        session.tree_sequence = trees

        if trees:
            session.current_tree = trees[0]
            self.decision_tree = self.load_tree_by_name(session.current_tree)
            self._set_starting_node(session)

    def _set_starting_node(self, session: ChatSession):
        """Find and set the first decision node as starting point."""
        if not self.decision_tree:
            return

        # Find first decision node
        for root in self.decision_tree.nodes:
            first_decision = self._find_first_decision_node(root)
            if first_decision:
                session.current_node_id = first_decision.node_id
                return

    def _find_first_decision_node(
        self, node: DecisionTreeNode
    ) -> DecisionTreeNode | None:
        """Recursively find the first decision node."""
        if node.node_type == NodeType.DECISION:
            return node
        for child in node.children:
            result = self._find_first_decision_node(child)
            if result:
                return result
        return None

    # STEP 3: Navigate decision tree and update facts
    def get_next_question(self, session: ChatSession) -> dict | None:
        """Get the next question in the decision tree."""
        if not session.current_node_id or not self.decision_tree:
            return None

        current_node = self.find_node_by_id(session.current_node_id)
        if not current_node:
            return None

        # Check for single-path auto-advancement (only one choice available)
        if len(current_node.edges) == 1:
            single_edge = current_node.edges[0]
            edge_actions = single_edge.get("actions", {})

            # Auto-advance if there's only one path and no decision attributes
            if not edge_actions or edge_actions.get("is_product"):
                target_node = self.find_node_by_id(single_edge["target"])
                if target_node:
                    session.current_node_id = single_edge["target"]
                    # Check if it's a product
                    if edge_actions.get("is_product"):
                        self._add_product(session, target_node.question)
                    return self.get_next_question(session)  # Continue automatically

        # Check for auto-advancement based on existing facts
        for edge in current_node.edges:
            edge_actions = edge.get("actions", {})
            if self._can_auto_advance(session, edge_actions):
                # Auto-advance
                target_node = self.find_node_by_id(edge["target"])
                if target_node:
                    session.current_node_id = edge["target"]
                    # Check if it's a product
                    if edge_actions.get("is_product"):
                        self._add_product(session, target_node.question)
                    return self.get_next_question(session)  # Continue

        # Handle end nodes
        if current_node.node_type == NodeType.END:
            if not current_node.children:
                # Move to next tree or end
                if self._advance_to_next_tree(session):
                    return self.get_next_question(session)
                else:
                    return {
                        "type": "end",
                        "message": "Decision tree complete",
                        "node_id": session.current_node_id,
                    }

        # Return question for user
        if current_node.question and current_node.edges:
            return {
                "type": "question",
                "question": current_node.question,
                "options": [
                    {
                        "text": edge["label"],
                        "value": edge["value"],
                        "target": edge["target"],
                    }
                    for edge in current_node.edges
                ],
            }

        return None

    def process_user_response(
        self, session: ChatSession, response_value: str, target_node_id: str
    ) -> bool:
        """Process user's response to a decision tree question."""
        current_node = self.find_node_by_id(session.current_node_id)
        if not current_node:
            return False

        # Find the selected edge
        selected_edge = None
        for edge in current_node.edges:
            if edge["target"] == target_node_id:
                selected_edge = edge
                break

        if not selected_edge:
            return False

        # Update facts from edge actions
        edge_actions = selected_edge.get("actions", {})
        for attr_name, attr_value in edge_actions.items():
            if attr_name == "is_product" and attr_value:
                target_node = self.find_node_by_id(target_node_id)
                if target_node and target_node.question:
                    self._add_product(session, target_node.question)
            else:
                # Store decision attributes in facts
                session.facts[attr_name] = str(attr_value).lower()

        # Move to target node
        session.current_node_id = target_node_id

        # Add to conversation history
        session.add_conversation_turn(
            current_node.question, selected_edge["label"], current_node.node_id
        )

        # Update facts JSON
        self._update_facts_json(session)
        return True

    def _can_auto_advance(self, session: ChatSession, edge_actions: dict) -> bool:
        """Check if we can auto-advance based on existing facts."""
        for attr_name, attr_value in edge_actions.items():
            if attr_name == "is_product":
                continue
            # Check if we have this fact
            fact_value = session.facts.get(attr_name)
            if fact_value == str(attr_value).lower():
                return True
        return False

    def _advance_to_next_tree(self, session: ChatSession) -> bool:
        """Move to the next tree in the sequence."""
        if not session.current_tree or not session.tree_sequence:
            return False

        # Mark current tree as completed
        if session.current_tree not in session.completed_trees:
            session.completed_trees.append(session.current_tree)

        # Find next tree
        try:
            current_index = session.tree_sequence.index(session.current_tree)
            if current_index + 1 < len(session.tree_sequence):
                session.current_tree = session.tree_sequence[current_index + 1]
                self.decision_tree = self.load_tree_by_name(session.current_tree)
                self._set_starting_node(session)
                self._update_facts_json(session)  # Update facts with new tree info
                return True
        except ValueError:
            pass

        return False

    def _add_product(self, session: ChatSession, product_name: str):
        """Add a product to the products list."""
        if product_name not in session.products:
            session.products.append(product_name)

    def find_node_by_id(self, node_id: str) -> DecisionTreeNode | None:
        """Find a node by its ID in the current tree."""
        if not self.decision_tree:
            return None

        def search_node(node: DecisionTreeNode) -> DecisionTreeNode | None:
            if node.node_id == node_id:
                return node
            for child in node.children:
                result = search_node(child)
                if result:
                    return result
            return None

        for root in self.decision_tree.nodes:
            result = search_node(root)
            if result:
                return result
        return None

    def _update_facts_json(self, session: ChatSession, original_input: str = None):
        """Update the facts JSON with current session state."""
        # Update client information with role details
        role_names = []
        if session.is_seller:
            role_names.append("Seller")
        if session.is_buyer:
            role_names.append("Buyer")

        session.client_information = {
            "is_buyer": session.is_buyer,
            "is_seller": session.is_seller,
            "role_display": " & ".join(role_names) if role_names else "Unknown",
            "role_determined": session.role_determined,
        }

        if original_input:
            session.client_information["original_input"] = original_input

        # Add decision tree information if available
        if session.role_determined:
            session.client_information["current_decision_tree"] = (
                session.current_tree or "None"
            )
            session.client_information["applicable_decision_trees"] = (
                session.tree_sequence.copy() if session.tree_sequence else []
            )

            # Add progress information
            if session.tree_sequence and session.current_tree:
                try:
                    current_index = session.tree_sequence.index(session.current_tree)
                    total_trees = len(session.tree_sequence)
                    session.client_information["tree_progress"] = (
                        f"{current_index + 1}/{total_trees}"
                    )
                    session.client_information["completed_trees"] = (
                        session.completed_trees.copy()
                    )
                except ValueError:
                    session.client_information["tree_progress"] = "Unknown"
