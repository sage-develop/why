from typing import Any
from dataclasses import dataclass, field
import uuid


@dataclass
class ConsultationSession:
    """
    Represents a single client consultation session.
    """

    session_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    current_node: str = "preprocessing"
    conversation_history: list[dict[str, str]] = field(default_factory=list)
    recommended_products: set[str] = field(default_factory=set)

    # FX / IR branch completion tracking
    fx_branch_completed: bool = False
    ir_branch_completed: bool = False

    # Client info & extracted preanswers
    pre_answered_questions: dict[str, str] = field(default_factory=dict)
    client_information: str = ""  # Raw client information provided by user
    client_information_completed: bool = False

    def add_interaction(self, question: str, answer: str, node_id: str):
        """
        Add an interaction to the conversation history.
        """
        self.conversation_history.append(
            {"node_id": node_id, "question": question, "answer": answer}
        )

    def add_products(self, products: list[str]):
        """
        Add recommended products to the session.
        """
        self.recommended_products.update(products)

    def update_client_information(self, key: str, value: Any):
        """
        Update client profile information.
        """
        self.client_information[key] = value

    def is_complete(self) -> bool:
        """
        Check if all steps have been completed.
        """
        return (
            self.client_information_completed
            and self.fx_branch_completed
            and self.ir_branch_completed
        )
