from typing import Any
from pathlib import Path
from src.chatbot.parser.tree_manager import MultiDecisionTreeManager
from src.chatbot.session import ConsultationSession
from src.chatbot.interface import get_client_info_collection_interface
from src.chatbot.extractor import ClientExtractor


class GlobalMarketsChatbot:
    """
    Main chatbot class that handles multiple decision tree consultations.
    Supports loading and traversing multiple decision trees from mermaid files.
    """

    def __init__(self, openai_api_key: str, mermaid_directory: Path = None):
        # Initialize multi-tree manager
        self.tree_manager = MultiDecisionTreeManager()

        # Load decision trees from decision_trees folder
        if mermaid_directory:
            self.tree_manager.load_trees_from_directory(mermaid_directory)
        else:
            # Default: load from decision_trees folder
            project_root = Path(__file__).parent.parent.parent
            decision_trees_folder = project_root / "src" / "decision_trees"
            self.tree_manager.load_trees_from_directory(decision_trees_folder)

        self.extractor = ClientExtractor(openai_api_key)
        self.active_sessions: dict[str, ConsultationSession] = {}

    def start_consultation(self) -> tuple[str, ConsultationSession]:
        """
        Start a new consultation session.
        """
        session = ConsultationSession()
        self.active_sessions[session.session_id] = session

        return get_client_info_collection_interface(), session

    def get_session(self, session_id: str) -> ConsultationSession | None:
        """
        Get a session by session ID.
        """
        return self.active_sessions.get(session_id)

    def get_session_info(self, session_id: str) -> dict[str, Any] | None:
        """
        Get information about a specific session.
        """
        session = self.get_session(session_id)

        if not session:
            return None

        return {
            "session_id": session.session_id,
            "current_node": session.current_node,
            "conversation_length": len(session.conversation_history),
            "recommended_products": list(session.recommended_products),
            "fx_completed": session.fx_branch_completed,
            "ir_completed": session.ir_branch_completed,
            "client_information": session.client_information,
            "client_information_completed": session.client_information_completed,
            "is_complete": session.is_complete(),
        }

    def end_session(self, session_id: str) -> bool:
        """
        End and remove a session.
        """
        if session_id in self.active_sessions:
            del self.active_sessions[session_id]
            return True
        return False

    def process_client_input(
        self,
        session_id: str,
        client_text: str,
    ) -> dict[str, Any] | None:
        """
        Process client input using ClientExtractor for both client categorization and decision tree pre-answering.
        """
        session = self.get_session(session_id)
        if not session:
            return None

        if not client_text.strip():
            # No client info provided, move to first available tree
            start_nodes = self.tree_manager.find_start_nodes()
            if start_nodes:
                tree_name, start_node = start_nodes[0]  # Use first available tree
                session.set_current_tree(tree_name)
                session.current_node = start_node.node_id
            else:
                raise ValueError("No start nodes found in any decision tree")
        else:
            # Store the raw client text
            session.client_information = client_text

            # Perform full extraction: client categorization + decision tree pre-answering
            all_decision_nodes = self.tree_manager.get_all_decision_nodes()
            full_analysis = self.extractor.extract_full_analysis(
                client_text, all_decision_nodes
            )

            # Extract pre-answered questions from full analysis
            session.pre_answered_questions = self.extractor.get_pre_answered_dict(
                full_analysis
            )

            # Store the full analysis for potential future use
            session.client_analysis = full_analysis

            # Choose the best tree to start with based on pre-answers
            best_tree = self._choose_best_starting_tree(
                session, session.pre_answered_questions
            )
            session.set_current_tree(best_tree)

            # Start from first decision node and check for pre-answers
            start_node_id = self._get_tree_start_node(best_tree)
            session.current_node = self._find_first_unanswered_question(
                session, start_node_id
            )

        # Update session as completed preprocessing
        session.client_information_completed = True

        return {
            "session_id": session_id,
            "current_node": session.current_node,
            "current_tree": session.current_tree,
            "extracted_count": (
                len(session.pre_answered_questions)
                if hasattr(session, "pre_answered_questions")
                else 0
            ),
            "is_complete": session.is_complete(),
            "client_information": session.client_information,
            "available_trees": self.tree_manager.get_tree_names(),
        }

    def _find_first_unanswered_question(
        self, session: ConsultationSession, start_node: str
    ) -> str:
        """Find the first question that hasn't been pre-answered."""
        current_node_id = start_node

        while current_node_id in getattr(session, "pre_answered_questions", {}):
            # This question was pre-answered, find the next one
            current_node = self.tree_manager.get_node(
                current_node_id, session.current_tree
            )
            if not current_node:
                break

            # Get the pre-answered choice
            pre_answer = session.pre_answered_questions[current_node_id]

            # Add to conversation history as pre-answered
            session.add_interaction(
                f"[Pre-answered] {current_node.question}", pre_answer, current_node_id
            )

            # Add products if any
            if current_node.products:
                session.add_products(current_node.products)

            # Move to next node
            next_node_id = self.tree_manager.get_next_node_id(
                current_node_id, pre_answer, session.current_tree
            )
            if not next_node_id:
                break

            current_node_id = next_node_id

            # Check if consultation is complete
            if current_node_id == "consultation_complete" or self._is_tree_complete(
                current_node_id
            ):
                break

        return current_node_id

    # TODO: Reevaluate this
    # If we know the client is a buyer or seller, we can start with the appropriate tree
    def _choose_best_starting_tree(
        self, session: ConsultationSession, extracted_answers: dict[str, str]
    ) -> str:
        """
        Choose the best decision tree to start with based on pre-answered questions.

        Args:
            session: Current consultation session
            extracted_answers: Pre-answered questions from client info

        Returns:
            Tree name to start with
        """
        tree_scores = {}

        for tree_name in self.tree_manager.get_tree_names():
            score = 0
            tree_nodes = self.tree_manager.get_tree(tree_name)
            if not tree_nodes:
                continue

            # Count how many questions in this tree can be pre-answered
            for node_id in extracted_answers.keys():
                if node_id in tree_nodes:
                    score += 1

            tree_scores[tree_name] = score

        # Return tree with highest score, or first available tree if no matches
        if tree_scores:
            best_tree = max(tree_scores.items(), key=lambda x: x[1])[0]
            if tree_scores[best_tree] > 0:
                return best_tree

        # Fall back to first available tree
        tree_names = self.tree_manager.get_tree_names()
        if tree_names:
            return tree_names[0]

        raise ValueError("No decision trees available")

    def _get_tree_start_node(self, tree_name: str) -> str:
        """Get the start node ID for a given tree."""
        tree_nodes = self.tree_manager.get_tree(tree_name)
        if not tree_nodes:
            raise ValueError(f"Tree '{tree_name}' not found")

        # Find start node
        for node_id, node in tree_nodes.items():
            if node.node_type.value == "start":
                return node_id

        # If no start node found, try common start node names
        common_starts = ["start", "client_type", "Profile"]
        for start_id in common_starts:
            if start_id in tree_nodes:
                return start_id

        # Last resort: return first node
        if tree_nodes:
            return next(iter(tree_nodes.keys()))

        raise ValueError(f"No valid start node found in tree '{tree_name}'")

    def _is_tree_complete(self, node_id: str) -> bool:
        """Check if we've reached a completion node for any tree."""
        completion_indicators = ["consultation_complete", "complete", "finished", "end"]
        return any(indicator in node_id.lower() for indicator in completion_indicators)

    def process_client_choice(self, session_id: str, user_choice: str) -> str:
        """Process a user's choice in the decision tree."""
        session = self.get_session(session_id)
        if not session:
            return "Session not found. Please start a new consultation."

        current_node = self.tree_manager.get_node(
            session.current_node, session.current_tree
        )
        if not current_node:
            return "Error: Invalid session state. Please start a new consultation."

        # Validate choice
        if user_choice not in current_node.choices:
            return (
                f"Invalid choice. Please select from: {', '.join(current_node.choices)}"
            )

        # Record interaction
        session.add_interaction(
            current_node.question, user_choice, session.current_node
        )

        # Add products if any
        if current_node.products:
            session.add_products(current_node.products)

        # Get next node
        next_node_id = self.tree_manager.get_next_node_id(
            session.current_node, user_choice, session.current_tree
        )
        if not next_node_id:
            return "Error: No next node found."

        # Check for completion
        if next_node_id == "consultation_complete" or self._is_tree_complete(
            next_node_id
        ):
            session.mark_tree_completed(session.current_tree)
            return self._generate_final_summary(session)

        # Check if next question is pre-answered
        actual_next_node_id = self._find_first_unanswered_question(
            session, next_node_id
        )
        session.current_node = actual_next_node_id

        # Check again for completion
        if actual_next_node_id == "consultation_complete" or self._is_tree_complete(
            actual_next_node_id
        ):
            session.mark_tree_completed(session.current_tree)
            return self._generate_final_summary(session)

        # Format next question
        next_node = self.tree_manager.get_node(
            actual_next_node_id, session.current_tree
        )
        if not next_node:
            return "Error: Could not find next question."

        return self._format_question_response(next_node)

    def _format_question_response(self, node) -> str:
        """Format a question with choices and pre-answered summary."""
        return f"**{node.question}**\n\n" + "\n".join(
            [f"{i+1}. {choice}" for i, choice in enumerate(node.choices)]
        )

    def _generate_final_summary(self, session: ConsultationSession) -> str:
        """Generate final consultation summary."""
        products = list(session.recommended_products)
        summary = f"""
**Consultation Complete!**

**Session Summary:**

**Recommended Products:**
{chr(10).join([f"• {product}\n" for product in products]) if products else "• No specific products recommended"}
"""

        return summary

    def answer_product_question(self, question: str) -> str:
        """Answer a general product question using available knowledge."""
        return f"I'd be happy to help with product information. However, the product Q&A system is not yet implemented. Your question was: {question}"
