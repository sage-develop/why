from src.chatbot.decision_tree import DecisionNode


def create_extract_preanswer_prompt(decision_context: str) -> str:
    """Create system prompt for extracting pre-answers from client information."""
    return f"""You are analyzing client information to pre-answer questions from a Global Markets product consultation decision tree.

Your task:
1. Review the decision tree nodes and their available choices
2. Identify which questions can be clearly answered based on the client information  
3. ONLY extract answers where the client information CLEARLY indicates a specific choice
4. Use EXACT choice text from the decision tree options
5. Assign confidence levels: High (explicitly stated), Medium (strongly implied), Low (unclear)

Decision Tree Context:
{decision_context}

IMPORTANT: Only include answers where you have medium or high confidence. When in doubt, don't extract."""
