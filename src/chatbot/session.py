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
    current_tree: str = ""  # Current tree being traversed
    conversation_history: list[dict[str, str]] = field(default_factory=list)
    recommended_products: set[str] = field(default_factory=set)

    # Multi-tree progress tracking
    completed_trees: set[str] = field(default_factory=set)
    tree_progress: dict[str, dict[str, Any]] = field(default_factory=dict)

    # TODO: review after update
    # For global markets decision tree
    # FX / IR branch completion tracking
    fx_branch_completed: bool = False
    ir_branch_completed: bool = False

    # Client info & extracted preanswers
    pre_answered_questions: dict[str, str] = field(default_factory=dict)
    client_information: str = ""  # Raw client information provided by user
    client_information_completed: bool = False
    client_analysis: Any = None  # Full client analysis from ClientExtractor

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
        Check if all steps have been completed for all decision trees.
        """
        return self.client_information_completed and (
            len(self.completed_trees) > 0
            # TODO: Remove this
            or (self.fx_branch_completed and self.ir_branch_completed)
        )

    def mark_tree_completed(self, tree_name: str) -> None:
        """Mark a decision tree as completed."""
        self.completed_trees.add(tree_name)

        # TODO: Remove this after we update global markets DAG
        if tree_name in ["global-markets"]:
            self.fx_branch_completed = True
            self.ir_branch_completed = True

    def set_current_tree(self, tree_name: str) -> None:
        """Set the current tree being traversed."""
        self.current_tree = tree_name

    def update_tree_progress(
        self, tree_name: str, progress_info: dict[str, Any]
    ) -> None:
        """Update progress information for a specific tree."""
        if tree_name not in self.tree_progress:
            self.tree_progress[tree_name] = {}
        self.tree_progress[tree_name].update(progress_info)

    def get_tree_progress(self, tree_name: str) -> dict[str, Any]:
        """Get progress information for a specific tree."""
        return self.tree_progress.get(tree_name, {})
