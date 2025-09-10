from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import tool_example_to_messages

from ..decision_tree import DecisionNode, NodeType
from .client_information import ClientInformation
from .preanswer import DecisionTreeAnswer


class ClientAnalysis(BaseModel):
    """Complete full analysis combining client categorization and decision tree pre-answers."""

    # Client categorization (8-category framework)
    client_information: ClientInformation

    # Decision tree pre-answers
    pre_answered_questions: list[DecisionTreeAnswer] = Field(
        description="List of decision tree questions that can be pre-answered from the client information"
    )

    # Overall confidence
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class ClientExtractor:
    """
    full extractor that simultaneously:
    1. Categorizes client information using 8-category framework
    2. Pre-answers decision tree questions from the same information
    """

    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4", temperature=0)
        self.structured_llm = self.llm.with_structured_output(
            schema=ClientAnalysis, method="function_calling"
        )

    def extract_full_analysis(
        self, client_text: str, decision_nodes: list[DecisionNode]
    ) -> ClientAnalysis:
        """
        Perform full extraction of client categorization and decision tree pre-answers.

        Args:
            client_text: Raw client information text (from PDF, manual input, etc.)
            decision_nodes: List of decision tree nodes for pre-answering

        Returns:
            ClientAnalysis containing both client categorization and pre-answers
        """
        system_prompt = self._create_full_prompt(decision_nodes)
        example_messages = self._create_examples(decision_nodes)

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                *example_messages,
                (
                    "human",
                    f"Analyze the following client information:\n\n{client_text}",
                ),
            ]
        )

        result = self.structured_llm.invoke(prompt.format_messages())
        return result

    def _create_full_prompt(self, decision_nodes: list[DecisionNode]) -> str:
        """Create full system prompt for both client categorization and pre-answering."""

        # Filter to decision nodes only
        decision_only_nodes = [
            node for node in decision_nodes if node.node_type == NodeType.DECISION
        ]

        # Build decision tree context
        decision_context = self._build_decision_context(decision_only_nodes)

        return f"""You are an expert relationship manager performing comprehensive client analysis. Your task has two parts:

**PART 1: CLIENT CATEGORIZATION**
Categorize the client according to our 8-category framework:

1. **Type of business** - Choose from:
   - Manufacturing & Production (Manufacturers, Food & Beverage, Plantation & Agriculture, Mining)
   - Trading & Distribution (Import/Export, Wholesalers, E-commerce, Retail)
   - Services & Professional (Consulting, Healthcare, Education, Technology)
   - Infrastructure & Development (Construction, Property Development, Logistics, Energy)
   - Consumer-Facing Businesses (Hospitality, Media, Franchisees)
   - Emerging & Specialized (Startups, Fintech, Social Enterprises, Family Offices)

2. **Industry** - Choose from:
   - Technology & Innovation, Healthcare & Life Sciences, Financial Services
   - Energy & Utilities, Manufacturing & Industrial, Consumer Goods & Retail
   - Real Estate & Construction, Transportation & Logistics, Agriculture & Natural Resources
   - Media & Entertainment, Education & Training, Government & Public Sector

3. **Size of business** - Choose from:
   - Enterprise & Large Corporate (>$500M revenue, 1000+ employees)
   - Middle Market ($50M-500M revenue, 100-1000 employees)
   - Small Business & SME ($500K-50M revenue, 1-100 employees)
   - Startups & Emerging Growth (high growth, <$50M revenue)
   - Specialized Segments (Family Offices, Professional Practices, Franchises)

4. **Coverage of business** - Choose from:
   - Domestic only, Cross-border, Both

5. **Trading terms** - Impact on working capital:
   - Extended credit terms (higher financing needs)
   - Cash on delivery (lower financing needs)
   - Advance payments (negative working capital)

6. **Trading currencies** - FX exposure:
   - Single currency, Multiple currencies, Volatile currencies

7. **Cash flow position** - Choose from:
   - Cash generative, Working capital dependent, Seasonal variations

8. **Capex frequency** - Choose from:
   - Regular capex, Lumpy capex, Minimal capex

**PART 2: DECISION TREE PRE-ANSWERING**
Based on the same client information, identify which decision tree questions can be pre-answered:

Decision Tree Context:
{decision_context}

Requirements for pre-answering:
- ONLY extract answers where the client information CLEARLY indicates a specific choice
- Use EXACT choice text from the decision tree options
- Assign confidence levels: High (explicitly stated), Medium (strongly implied), Low (unclear)
- Only include answers where you have medium or high confidence

**IMPORTANT**: 
- Only use categories and subcategories that exist in our framework
- If information is unclear or missing, use the most appropriate general category and note low confidence
- When in doubt about decision tree answers, don't include them"""

    def _build_decision_context(self, decision_nodes: list[DecisionNode]) -> str:
        """Build formatted context of decision tree nodes for the prompt."""
        context_lines = []

        for node in decision_nodes:
            context_lines.append(f"Node ID: {node.node_id}")
            context_lines.append(f"Question: {node.question}")
            context_lines.append(f"Valid Choices: {node.choices}")
            context_lines.append("")  # Empty line for readability

        return "\n".join(context_lines)

    def _create_examples(self, decision_nodes: list[DecisionNode]) -> list:
        """Create few-shot examples for better full extraction."""
        # Import here to avoid circular imports
        from .client_information import (
            BusinessType,
            Industry,
            BusinessSize,
            BusinessCoverage,
            TradingTerms,
            TradingCurrencies,
            CashFlowPosition,
            CapexFrequency,
        )

        examples = [
            (
                "ABC Manufacturing Ltd is a automotive parts manufacturer with annual revenue of $150M and 400 employees. They export 60% of their production to Europe and Asia, primarily dealing in USD and EUR. Payment terms are typically 45 days from customers. They have seasonal peaks in Q2-Q3 and require significant capex every 2-3 years for new equipment. The company wants to hedge about 70% of their FX exposure due to volatility concerns.",
                ClientAnalysis(
                    client_information=ClientInformation(
                        business_type=BusinessType(
                            category="Manufacturing & Production",
                            subcategory="Manufacturers",
                            details="Automotive parts manufacturing with export focus",
                            confidence_score="High",
                        ),
                        industry=Industry(
                            sector="Manufacturing & Industrial",
                            subsector="Automotive",
                            regulatory_requirements="Automotive industry standards and export compliance",
                            confidence_score="High",
                        ),
                        business_size=BusinessSize(
                            category="Middle Market",
                            subcategory="Core Middle Market ($100M-250M revenue, 200-500 employees)",
                            revenue_range="$150M",
                            employee_count="400",
                            confidence_score="High",
                        ),
                        business_coverage=BusinessCoverage(
                            coverage_type="Cross-border",
                            geographic_footprint="Europe and Asia exports (60% of production)",
                            expansion_plans="Not mentioned",
                            confidence_score="High",
                        ),
                        trading_terms=TradingTerms(
                            customer_terms="45 days",
                            supplier_terms="Not mentioned",
                            working_capital_impact="Extended credit terms (higher financing needs)",
                            confidence_score="High",
                        ),
                        trading_currencies=TradingCurrencies(
                            currency_exposure="Multiple currencies",
                            primary_currencies=["USD", "EUR"],
                            hedging_needs="FX hedging for export revenues",
                            confidence_score="High",
                        ),
                        cash_flow_position=CashFlowPosition(
                            cash_flow_type="Seasonal variations",
                            seasonality="Peaks in Q2-Q3",
                            financing_needs="Working capital support for seasonal peaks",
                            confidence_score="High",
                        ),
                        capex_frequency=CapexFrequency(
                            capex_pattern="Lumpy capex",
                            upcoming_investments="Equipment replacement every 2-3 years",
                            financing_preferences="Not specified",
                            confidence_score="High",
                        ),
                    ),
                    pre_answered_questions=[
                        DecisionTreeAnswer(
                            node_id="client_type",
                            question="What is the client's business activity?",
                            chosen_answer="Both Importer & Exporter",
                            confidence="High",
                        ),
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
                    ],
                    confidence_score="High",
                ),
            )
        ]

        # Filter pre-answered questions to only include nodes that exist in current decision tree
        filtered_examples = []
        node_ids = {node.node_id for node in decision_nodes}

        for input_text, expected_output in examples:
            filtered_preanswers = [
                answer
                for answer in expected_output.pre_answered_questions
                if answer.node_id in node_ids
            ]

            filtered_output = ClientAnalysis(
                client_information=expected_output.client_information,
                pre_answered_questions=filtered_preanswers,
                confidence_score=expected_output.confidence_score,
            )

            filtered_examples.append((input_text, filtered_output))

        messages = []
        for input_text, expected_output in filtered_examples:
            messages.extend(
                tool_example_to_messages(
                    input_text,
                    [expected_output],
                    ai_response="I've performed comprehensive client analysis including categorization and decision tree pre-answering.",
                )
            )

        return messages

    def format_analysis_summary(self, analysis: ClientAnalysis) -> str:
        """Format the full analysis into a readable summary."""
        summary = f"""**Comprehensive Client Analysis**

**CLIENT CATEGORIZATION:**

**1. Business Type:** {analysis.client_information.business_type.category}
   - Subcategory: {analysis.client_information.business_type.subcategory}
   - Details: {analysis.client_information.business_type.details}

**2. Industry:** {analysis.client_information.industry.sector}
   - Subsector: {analysis.client_information.industry.subsector}
   - Regulatory: {analysis.client_information.industry.regulatory_requirements or 'Not specified'}

**3. Business Size:** {analysis.client_information.business_size.category}
   - Classification: {analysis.client_information.business_size.subcategory}
   - Revenue: {analysis.client_information.business_size.revenue_range or 'Not specified'}
   - Employees: {analysis.client_information.business_size.employee_count or 'Not specified'}

**4. Coverage:** {analysis.client_information.business_coverage.coverage_type}
   - Geographic Footprint: {analysis.client_information.business_coverage.geographic_footprint or 'Not specified'}
   - Expansion Plans: {analysis.client_information.business_coverage.expansion_plans or 'Not specified'}

**5. Trading Terms:** {analysis.client_information.trading_terms.working_capital_impact}
   - Customer Terms: {analysis.client_information.trading_terms.customer_terms or 'Not specified'}
   - Supplier Terms: {analysis.client_information.trading_terms.supplier_terms or 'Not specified'}

**6. Trading Currencies:** {analysis.client_information.trading_currencies.currency_exposure}
   - Primary Currencies: {', '.join(analysis.client_information.trading_currencies.primary_currencies or ['Not specified'])}
   - Hedging Needs: {analysis.client_information.trading_currencies.hedging_needs or 'Not specified'}

**7. Cash Flow Position:** {analysis.client_information.cash_flow_position.cash_flow_type}
   - Seasonality: {analysis.client_information.cash_flow_position.seasonality or 'Not specified'}
   - Financing Needs: {analysis.client_information.cash_flow_position.financing_needs or 'Not specified'}

**8. Capex Frequency:** {analysis.client_information.capex_frequency.capex_pattern}
   - Upcoming Investments: {analysis.client_information.capex_frequency.upcoming_investments or 'Not specified'}
   - Financing Preferences: {analysis.client_information.capex_frequency.financing_preferences or 'Not specified'}

**DECISION TREE PRE-ANSWERS:**
"""

        if analysis.pre_answered_questions:
            for answer in analysis.pre_answered_questions:
                summary += f"""
**{answer.question}**
   - Answer: {answer.chosen_answer}
   - Confidence: {answer.confidence}"""
        else:
            summary += (
                "\n*No questions could be pre-answered with sufficient confidence*"
            )

        summary += f"""

**Overall Confidence Score:** {analysis.confidence_score}
"""
        return summary

    def get_pre_answered_dict(self, analysis: ClientAnalysis) -> dict[str, str]:
        """Extract pre-answered questions as a simple dict for the chatbot system."""
        extracted_answers = {}
        for answer in analysis.pre_answered_questions:
            # Only include medium/high confidence answers
            if answer.confidence in ["High", "Medium"]:
                extracted_answers[answer.node_id] = answer.chosen_answer
        return extracted_answers
