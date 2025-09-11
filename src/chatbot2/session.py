from pydantic import BaseModel, Field


class ChatSession(BaseModel):
    """
    Stores dynamic client session info and conversation state.
    Facts are stored as a mapping of node_id -> answer or value.
    """

    facts: dict[str, str] = Field(default_factory=dict)
    current_node_id: str | None = None
    conversation_history: list[dict[str, str]] = Field(default_factory=list)
    initial_processing_done: bool = False

    def set_fact(self, node_id: str, answer: str):
        """Set a fact about a specific node."""
        self.facts[node_id] = answer

    def get_fact(self, node_id: str) -> str | None:
        """Get a fact about a specific node."""
        return self.facts.get(node_id)

    def add_conversation_turn(self, question: str, answer: str, node_id: str):
        """Add a conversation turn to history."""
        self.conversation_history.append(
            {"question": question, "answer": answer, "node_id": node_id}
        )

    def has_fact(self, node_id: str) -> bool:
        """Check if we have a fact for a specific node."""
        return node_id in self.facts

    def reset_conversation(self):
        """Reset the conversation state but keep extracted facts."""
        self.current_node_id = None
        self.conversation_history = []
        # Keep initial facts from document processing

    def to_json(self):
        return {
            "facts": self.facts,
            "current_node": self.current_node_id,
            "conversation_history": self.conversation_history,
            "initial_processing_done": self.initial_processing_done,
        }
