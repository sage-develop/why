from typing import Any
from src.chatbot.decision_tree import GlobalMarketsDecisionTree
from src.chatbot.session import ConsultationSession
from src.chatbot.interface import get_client_info_collection_interface
from src.chatbot.extraction import PreAnswerExtractor


class GlobalMarketsChatbot:
    """
    Main chatbot class that handles the Global Markets product consultation.
    Ensures both FX and IR branches are fully traversed before completion.
    """

    def __init__(self, openai_api_key: str):
        self.decision_tree = GlobalMarketsDecisionTree()
        self.extractor = PreAnswerExtractor(openai_api_key)
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
        self, session_id: str, client_text: str
    ) -> dict[str, Any] | None:
        """
        Process client input using modern LangChain structured extraction.
        """
        session = self.get_session(session_id)
        if not session:
            return None

        if not client_text.strip():
            # No client info provided, move to first question
            session.current_node = "client_type"
        else:
            # Store the raw client text
            session.client_information = client_text

            # Step 1: Extract pre-answers using modern LangChain structured extraction
            decision_nodes = list(self.decision_tree.nodes.values())
            extracted_answers = self.extractor.extract_preanswers(
                decision_nodes, client_text
            )

            # Step 2: Store extracted pre-answers in session
            session.pre_answered_questions = extracted_answers

            # Step 3: Start from first decision node and check for pre-answers
            session.current_node = self._find_first_unanswered_question(
                session, "client_type"
            )

        # Update session as completed preprocessing
        session.client_information_completed = True

        return {
            "session_id": session_id,
            "current_node": session.current_node,
            "extracted_count": (
                len(session.pre_answered_questions)
                if hasattr(session, "pre_answered_questions")
                else 0
            ),
            "is_complete": session.is_complete(),
            "client_information": session.client_information,
        }

    def _find_first_unanswered_question(
        self, session: ConsultationSession, start_node: str
    ) -> str:
        """Find the first question that hasn't been pre-answered."""
        current_node_id = start_node

        while current_node_id in getattr(session, "pre_answered_questions", {}):
            # This question was pre-answered, find the next one
            current_node = self.decision_tree.get_node(current_node_id)
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
            next_node_id = self.decision_tree.get_next_node(current_node_id, pre_answer)
            if not next_node_id:
                break

            current_node_id = next_node_id

            # Check if consultation is complete
            if current_node_id == "consultation_complete":
                break

        return current_node_id

    def process_client_choice(self, session_id: str, user_choice: str) -> str:
        """Process a user's choice in the decision tree."""
        session = self.get_session(session_id)
        if not session:
            return "Session not found. Please start a new consultation."

        current_node = self.decision_tree.get_node(session.current_node)
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
        next_node_id = self.decision_tree.get_next_node(
            session.current_node, user_choice
        )
        if not next_node_id:
            return "Error: No next node found."

        # Check for completion
        if next_node_id == "consultation_complete":
            return self._generate_final_summary(session)

        # Check if next question is pre-answered
        actual_next_node_id = self._find_first_unanswered_question(
            session, next_node_id
        )
        session.current_node = actual_next_node_id

        # Check again for completion
        if actual_next_node_id == "consultation_complete":
            return self._generate_final_summary(session)

        # Format next question
        next_node = self.decision_tree.get_node(actual_next_node_id)
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
