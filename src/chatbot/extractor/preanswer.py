from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import tool_example_to_messages

from ..decision_tree import DecisionNode, NodeType
from ..prompts import create_extract_preanswer_prompt

# Goal:
# Detect which decision nodes in the DAG can be pre-answered.
# Store these answers in the session (pre_answered_questions).
# Skip those nodes in the tree when traversing, so the user only gets prompted for remaining unknown questions.

# Step:
# 1. Build the decision tree context

# 2. Create the extraction prompt with few-shot examples
#   - Node ID: client_type
#   - Question: What is the client's business activity?
#   - Valid Choices: ['Importer', 'Exporter', 'Both Importer & Exporter']

# 3. Extract structured data
#   "answers": [
#     {
#       "node_id": "client_type",
#       "question": "What is the client's business activity?",
#       "chosen_answer": "Both Importer & Exporter",
#       "confidence": "High"
#     }
#   ]

# 4. Post process the extracted data:
# {
#     "client_type": "Both Importer & Exporter",
#     "hedge_decision_importer": "Yes",
#     "hedge_decision_exporter": "Yes",
#     "hedge_proportion_importer": "Partial hedging needed",
# }


class DecisionTreeAnswer(BaseModel):
    """A pre-answered decision from client information."""

    node_id: str = Field(description="The decision tree node ID")
    question: str = Field(description="The decision tree question")
    chosen_answer: str = Field(
        description="The exact choice selected from available options"
    )
    confidence: str = Field(description="High/Medium/Low confidence in this extraction")


class PreAnsweredQuestions(BaseModel):
    """Collection of pre-answered questions extracted from client information."""

    # So we can extract multiple decision answers
    answers: list[DecisionTreeAnswer] = Field(
        description="List of decision tree questions that can be pre-answered from the client information"
    )


class PreAnswerExtractor:
    """Modern LangChain structured extraction for decision tree pre-answering."""

    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4", temperature=0)

        # Create the structured output LLM
        # https://python.langchain.com/docs/how_to/structured_output/#the-with_structured_output-method
        # Use function_calling method since GPT-4 doesn't support json_schema method
        self.structured_llm = self.llm.with_structured_output(
            schema=PreAnsweredQuestions, method="function_calling"
        )

        # Define few-shot examples for better extraction
        self.examples = self._create_reference_examples()

    def _create_reference_examples(self) -> list:
        """Create reference examples to improve extraction quality."""
        examples = [
            # Example 1: Clear business type indication
            (
                "ABC Corporation is both an importer and exporter operating in Southeast Asia.",
                PreAnsweredQuestions(
                    answers=[
                        DecisionTreeAnswer(
                            node_id="client_type",
                            question="What is the client's business activity?",
                            chosen_answer="Both Importer & Exporter",
                            confidence="High",
                        )
                    ]
                ),
            ),
            # Example 2: Clear hedging preferences
            (
                "The company wants to hedge about 70% of their FX exposure due to volatility concerns.",
                PreAnsweredQuestions(
                    answers=[
                        DecisionTreeAnswer(
                            node_id="hedge_decision_importer",
                            question="Do you want to hedge FX risk for imports?",
                            chosen_answer="Yes",
                            confidence="High",
                        ),
                        DecisionTreeAnswer(
                            node_id="hedge_decision_exporter",
                            question="Do you want to hedge FX risk for exports?",
                            chosen_answer="Yes",
                            confidence="High",
                        ),
                        DecisionTreeAnswer(
                            node_id="hedge_proportion_importer",
                            question="What proportion of imports should be hedged?",
                            chosen_answer="Partial hedging needed",
                            confidence="Medium",
                        ),
                    ]
                ),
            ),
            # Example 3: Domestic only business
            (
                "We only operate domestically and don't deal with foreign currencies.",
                PreAnsweredQuestions(
                    answers=[
                        DecisionTreeAnswer(
                            node_id="ClientType",
                            question="What is the client's business activity?",
                            chosen_answer="Domestic only",
                            confidence="High",
                        )
                    ]
                ),
            ),
            # Example 4: No clear information (should extract empty list)
            (
                "The weather is sunny today.",
                PreAnsweredQuestions(answers=[]),
            ),
        ]

        return examples

    def _build_example_messages(self, decision_nodes: list[DecisionNode]) -> list:
        """Convert examples to message format for few-shot prompting."""
        messages = []

        for text, expected_extraction in self.examples:
            # Filter examples to only include nodes that exist in current decision tree
            valid_answers = []
            node_lookup = {node.node_id: node for node in decision_nodes}

            for answer in expected_extraction.answers:
                if answer.node_id in node_lookup:
                    # Verify the chosen answer is valid for this node
                    node = node_lookup[answer.node_id]
                    if answer.chosen_answer in node.choices:
                        valid_answers.append(answer)

            # Create filtered example
            filtered_extraction = PreAnsweredQuestions(answers=valid_answers)

            # Determine AI response message
            if filtered_extraction.answers:
                ai_response = f"Extracted {len(filtered_extraction.answers)} pre-answered questions from the client information."
            else:
                ai_response = "No decision tree questions can be clearly pre-answered from this information."

            # Convert to message format
            messages.extend(
                tool_example_to_messages(
                    text, [filtered_extraction], ai_response=ai_response
                )
            )

        return messages

    def extract_preanswers(
        self, decision_nodes: list[DecisionNode], client_text: str
    ) -> dict[str, str]:
        """
        Extract pre-answered questions from client text using modern LangChain structured extraction.

        Args:
            decision_nodes: list of decision tree nodes to consider
            client_text: Raw client information text

        Returns:
            Dictionary mapping node_id -> chosen_answer for pre-answered questions
        """

        # Filter to only decision nodes
        decision_only_nodes = [
            node for node in decision_nodes if node.node_type == NodeType.DECISION
        ]

        # Build the decision tree context
        decision_context = self._build_decision_context(decision_only_nodes)

        # Create the extraction prompt with few-shot examples
        example_messages = self._build_example_messages(decision_only_nodes)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", create_extract_preanswer_prompt(decision_context)),
                *example_messages,  # Add few-shot examples
                ("human", f"Client Information: {client_text}"),
            ]
        )

        # Extract structured data
        formatted_prompt = prompt.format_messages(
            decision_context=decision_context, client_text=client_text
        )

        result = self.structured_llm.invoke(formatted_prompt)

        # Convert to simple dict format and filter by confidence
        extracted_answers = {}
        for answer in result.answers:
            # Only include medium/high confidence answers
            if answer.confidence in ["High", "Medium"]:
                extracted_answers[answer.node_id] = answer.chosen_answer

        return extracted_answers

    def _build_decision_context(self, decision_nodes: list[DecisionNode]) -> str:
        """Build formatted context of decision tree nodes for the prompt."""
        context_lines = []

        for node in decision_nodes:
            context_lines.append(f"Node ID: {node.node_id}")
            context_lines.append(f"Question: {node.question}")
            context_lines.append(f"Valid Choices: {node.choices}")
            context_lines.append("")  # Empty line for readability

        return "\n".join(context_lines)
