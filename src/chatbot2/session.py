from pydantic import BaseModel, Field


class ChatSession(BaseModel):
    """Clean session model following the required facts JSON structure."""

    # Core session state
    initial_processing_done: bool = False
    role_determined: bool = False

    # Client role flags (no complex role enum)
    is_buyer: bool = False
    is_seller: bool = False

    # Facts JSON structure: {"client_information": {...}, "products": [], "facts": {...}}
    client_information: dict = Field(default_factory=dict)
    products: list[str] = Field(default_factory=list)
    facts: dict[str, str] = Field(default_factory=dict)  # Only decision tree attributes

    # Navigation
    current_node_id: str | None = None
    current_tree: str | None = None
    tree_sequence: list[str] = Field(default_factory=list)
    completed_trees: list[str] = Field(default_factory=list)

    # History
    conversation_history: list[dict[str, str]] = Field(default_factory=list)

    def add_conversation_turn(self, question: str, answer: str, node_id: str):
        """Add a conversation turn to history."""
        self.conversation_history.append(
            {"question": question, "answer": answer, "node_id": node_id}
        )

    def to_json(self):
        """Return the clean facts JSON structure as requested."""
        return {
            "client_information": self.client_information,
            "products": self.products,
            "facts": self.facts,
        }
