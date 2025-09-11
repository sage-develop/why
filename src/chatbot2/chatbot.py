from pathlib import Path
import json

from .models import (
    DecisionTree,
    SellerPostShipmentLCDecision,
    DecisionTreeNode,
    NodeType,
)
from .extractor import Extractor
from .parser import MermaidDecisionTreeParser
from .session import ChatSession


class Chatbot:
    """
    Chatbot that processes client input, extracts structured info,
    and applies a decision tree to determine results.
    """

    def __init__(
        self,
        openai_api_key: str,
        tree_md_path: str,
        tree_name: str,
        tree_context: str = "",
    ):
        self.extractor = Extractor(openai_api_key=openai_api_key)
        self.tree_md_path = Path(tree_md_path)
        self.tree_name = tree_name
        self.tree_context = tree_context

        # Load and parse decision tree
        self.decision_tree = self._load_tree()
        self.session = ChatSession()

    def _load_tree(self) -> DecisionTree:
        if not self.tree_md_path.exists():
            raise FileNotFoundError(
                f"Decision tree file not found: {self.tree_md_path}"
            )

        with self.tree_md_path.open("r") as f:
            mermaid_text = f.read()

        tree = MermaidDecisionTreeParser().parse_mermaid_to_decision_tree(
            md_text=mermaid_text,
            tree_name=self.tree_name,
            context=self.tree_context,
        )
        return tree

    def process_client_input(
        self, client_text: str, session: ChatSession | None = None
    ) -> SellerPostShipmentLCDecision:
        """
        Process client input text, extract structured attributes,
        and populate session facts instead of mutating tree nodes.
        """
        # Step 1: Extract client info using LLM + Pydantic model
        client_info = self.extractor.extract(client_text, SellerPostShipmentLCDecision)

        # Step 2: Store extracted attributes in session facts
        all_nodes = self._get_all_nodes()
        for node in all_nodes:
            attr_name = node.attr_name
            if attr_name and hasattr(client_info, attr_name):
                value = getattr(client_info, attr_name)
                if value is not None:
                    # Store in session using attribute name as key
                    # {"is_sight_lc": "true", "is_usance_lc": "false", "needs_financing": "true"}
                    session.set_fact(attr_name, str(value))

        # Step 3: Mark initial processing as done and set starting position
        session.initial_processing_done = True
        if not session.current_node_id:
            # Start from the first decision node (B), not the root (A) which is just a label
            first_decision_node = None
            for node in self._get_all_nodes():
                if node.node_type == NodeType.DECISION:
                    first_decision_node = node
                    break
            session.current_node_id = (
                first_decision_node.node_id if first_decision_node else None
            )

        # Step 4: Return the structured client info for downstream use
        return client_info

    def find_node_by_id(self, node_id: str) -> DecisionTreeNode | None:
        """Find a node by its ID in the decision tree."""

        def search_nodes(nodes: list[DecisionTreeNode]) -> DecisionTreeNode | None:
            for node in nodes:
                if node.node_id == node_id:
                    return node
                # Search children recursively
                found = search_nodes(node.children)
                if found:
                    return found
            return None

        return search_nodes(self.decision_tree.nodes)

    def _get_all_nodes(self) -> list[DecisionTreeNode]:
        """Get all nodes in the decision tree (flattened)."""
        all_nodes = []

        def collect_nodes(nodes: list[DecisionTreeNode]):
            for node in nodes:
                all_nodes.append(node)
                collect_nodes(node.children)

        collect_nodes(self.decision_tree.nodes)
        return all_nodes

    def get_next_question(self, session: ChatSession) -> dict | None:
        """
        Get the next question to ask based on current session state.
        Returns None if we've reached an end node or there are no more questions.
        """
        if not session.current_node_id:
            return None

        current_node = self.find_node_by_id(session.current_node_id)
        if not current_node:
            return None

        # If current node is an end node, check if it has children (intermediate) or is final
        if current_node.node_type == NodeType.END:
            if len(current_node.children) == 0:
                # This is a final end node - show recommendation
                return {
                    "type": "end",
                    "node_id": current_node.node_id,
                    "message": f"Recommendation: {current_node.node_id}",
                    "is_final": True,
                }
            else:
                # This is an intermediate step - automatically move to the next node
                session.current_node_id = current_node.children[0].node_id
                return self.get_next_question(session)  # Continue traversal

        # For decision nodes, check if we already have the answer using attribute name
        if current_node.node_type == NodeType.DECISION and current_node.attr_name:
            if session.has_fact(current_node.attr_name):
                # We have the answer, move to the appropriate child
                answer = session.get_fact(current_node.attr_name)
                next_node = self._find_next_node_by_answer(current_node, answer)
                if next_node:
                    session.current_node_id = next_node.node_id
                    return self.get_next_question(session)  # Recursive call to continue

        # Try LLM auto-answer before asking the user
        if current_node.node_type == NodeType.DECISION:
            llm_answer = self._try_auto_answer_with_llm(current_node, session)

            if llm_answer and llm_answer.get("auto_answered"):
                # LLM is confident - process the answer automatically
                answer = llm_answer["answer"]

                # Store the fact using attribute name or node-specific key as fallback
                fact_key = (
                    current_node.attr_name or f"node_{current_node.node_id}_response"
                )
                session.set_fact(fact_key, answer)

                # Add to conversation history with LLM reasoning
                question_text = self._extract_question_text(current_node)
                session.add_conversation_turn(
                    question_text,
                    f"{answer} (auto-answered)",
                    current_node.node_id,
                )

                # Find next node and continue
                next_node = self._find_next_node_by_answer(current_node, answer)
                if next_node:
                    session.current_node_id = next_node.node_id
                    return self.get_next_question(session)

        # We need to ask this question to the user
        if current_node.node_type == NodeType.DECISION:
            question_text = self._extract_question_text(current_node)
            options = self.get_response_options(current_node)

            return {
                "type": "question",
                "node_id": current_node.node_id,
                "question": question_text,
                "options": options,
                "attr_name": current_node.attr_name,
            }

        return None

    def get_response_options(self, node: DecisionTreeNode) -> list[dict] | None:
        """Get available response options for a decision node based on edge labels."""
        if not node.children:
            return []

        options = []

        # First priority: Use edge labels from the decision tree
        if node.edges:
            for edge in node.edges:
                options.append(
                    {
                        "text": edge["label"],
                        "value": edge["value"],
                        "target": edge["target"],
                    }
                )
            return options

        else:
            raise ValueError(f"Node {node.node_id} has children but no edges defined")

    def process_user_response(
        self, session: ChatSession, response_value: str, target_node_id: str
    ) -> bool:
        """
        Process a user's response and update the session state.
        Returns True if successful, False otherwise.
        """
        if not session.current_node_id:
            return False

        current_node = self.find_node_by_id(session.current_node_id)
        if not current_node:
            return False

        # Store the fact using attribute name or node-specific key as fallback
        fact_key = current_node.attr_name or f"node_{current_node.node_id}_response"
        session.set_fact(fact_key, response_value)

        # Add to conversation history
        question_text = self._extract_question_text(current_node)
        session.add_conversation_turn(
            question_text, response_value, session.current_node_id
        )

        # Move to the target node
        session.current_node_id = target_node_id

        return True

    def _extract_question_text(self, node: DecisionTreeNode) -> str:
        """Extract a readable question from a decision node."""
        # First priority: use the question from the decision tree
        if node.question and node.question.strip():
            return node.question.strip()

        # Second priority: generate from attribute name
        if node.attr_name:
            # Convert attribute name to readable question
            attr_words = node.attr_name.replace("_", " ").title()
            if node.attr_name.startswith("is_"):
                return f"Is {attr_words[3:]} applicable?"
            elif node.attr_name.startswith("needs_"):
                return f"Do you need {attr_words[6:]}?"
            elif node.attr_name.startswith("use_"):
                return f"Will you use {attr_words[4:]}?"
            else:
                return f"What about {attr_words}?"

        # Fallback to generic question
        return f"Please make a choice for {node.question}"

    def _find_next_node_by_answer(
        self, current_node: DecisionTreeNode, answer: str
    ) -> DecisionTreeNode | None:
        """Find the next node based on the user's answer using the tree structure."""
        if not current_node.children:
            return None

        # Normalize answer
        normalized_answer = str(answer).lower().strip()

        # Use edge information to find the target - this is the only logic we need
        if current_node.edges:
            for edge in current_node.edges:
                if edge["value"] == normalized_answer:
                    return self.find_node_by_id(edge["target"])

        # If no edge matches but we have children, this means the decision tree
        # is missing edge labels - in this case we can't determine the path
        print(
            f"Warning: No edge found for answer '{answer}' on node {current_node.node_id}"
        )
        print(f"Available edges: {[edge['value'] for edge in current_node.edges]}")

        return None

    def _try_auto_answer_with_llm(
        self, current_node: DecisionTreeNode, session: ChatSession
    ) -> dict | None:
        """
        Use LLM to analyze existing facts and try to answer the current question automatically.
        Returns answer dict if confident, None if not confident enough.
        """
        if not current_node or current_node.node_type != NodeType.DECISION:
            return None

        # Get the question text
        question = self._extract_question_text(current_node)

        # Prepare existing facts for LLM analysis
        facts_summary = self._format_facts_for_analysis(session.facts)

        if not facts_summary.strip():
            return None  # No facts to analyze

        # Try to firstly match the question attribute name with the
        # Create prompt for LLM analysis
        analysis_prompt = f"""
You are analyzing a banking/trade finance conversation to determine if you can confidently answer a question based on existing facts.

EXISTING FACTS:
{facts_summary}

QUESTION TO ANSWER:
{question}

POSSIBLE ANSWERS FOR THIS QUESTION:
{self._get_possible_answers_for_node(current_node)}

TASK:
1. Analyze if the existing facts provide enough information to confidently answer this question
2. If confident (80% or higher), provide the answer
3. If not confident enough, indicate that user input is needed

Respond in JSON format:
{{
    "confident": true/false,
    "confidence_level": 0.0-1.0,
    "answer": "your answer if confident, null otherwise",
    "reasoning": "brief explanation of your reasoning"
}}
"""

        try:
            # Use the same LangChain LLM as the extractor
            full_prompt = f"You are an expert banking analyst that helps determine answers based on available information.\n\n{analysis_prompt}"

            response = self.extractor.llm.invoke(full_prompt)
            result_text = response.content.strip()

            # Parse the JSON response
            try:
                result = json.loads(result_text)

                if (
                    result.get("confident", False)
                    and result.get("confidence_level", 0) >= 0.8
                ):
                    answer = result.get("answer")
                    if answer:
                        return {
                            "answer": answer.lower(),  # Normalize to lowercase
                            "confidence": result.get("confidence_level", 0.8),
                            "reasoning": result.get(
                                "reasoning", "LLM analysis of existing facts"
                            ),
                            "auto_answered": True,
                        }
            except json.JSONDecodeError:
                # If JSON parsing fails, fall back to asking the user
                pass

        except Exception as e:
            # If LLM call fails, fall back to asking the user
            print(f"LLM auto-answer failed: {e}")

        return None

    def _format_facts_for_analysis(self, facts: dict) -> str:
        """Format existing facts for LLM analysis."""
        if not facts:
            return "No facts available."

        formatted_facts = []
        for key, value in facts.items():
            # Make attribute names more readable
            readable_key = key.replace("_", " ").title()

            # Format based on attribute patterns
            if key.startswith("is_"):
                formatted_facts.append(f"• {readable_key[3:]}: {value}")
            elif key.startswith("needs_"):
                formatted_facts.append(f"• Needs {readable_key[6:]}: {value}")
            elif key.startswith("use_"):
                formatted_facts.append(f"• Will use {readable_key[4:]}: {value}")
            else:
                formatted_facts.append(f"• {readable_key}: {value}")

        return "\n".join(formatted_facts)

    def _get_possible_answers_for_node(self, node: DecisionTreeNode) -> str:
        """Get possible answers for a decision node to help LLM choose correctly."""
        if not node.children:
            return "- No valid answers (terminal node)"

        # First priority: Use edge information from the decision tree
        if node.edges:
            options = []
            for edge in node.edges:
                options.append(f"- '{edge['value']}' ({edge['label']})")
            return "\n".join(options)

        # Fallback: If no edges defined, use child node IDs
        # This should not happen in a properly defined decision tree
        options = []
        for child in node.children:
            options.append(f"- '{child.node_id.lower()}' (node {child.node_id})")

        return (
            "\n".join(options) if options else "- No valid answers (no edges defined)"
        )
