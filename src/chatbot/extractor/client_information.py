from pydantic import BaseModel, Field
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.utils.function_calling import tool_example_to_messages

from ..prompts import create_extraction_client_information_prompt


class BusinessType(BaseModel):
    """Client's primary business type classification."""

    category: str = Field(
        description="Primary business category from: Manufacturing & Production, Trading & Distribution, Services & Professional, Infrastructure & Development, Consumer-Facing Businesses, Emerging & Specialized"
    )
    subcategory: str = Field(
        description="Specific subcategory within the main category"
    )
    details: str = Field(description="Key business activities and characteristics")
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class Industry(BaseModel):
    """Industry classification and characteristics."""

    sector: str = Field(
        description="Primary industry sector from: Technology & Innovation, Healthcare & Life Sciences, Financial Services, Energy & Utilities, Manufacturing & Industrial, Consumer Goods & Retail, Real Estate & Construction, Transportation & Logistics, Agriculture & Natural Resources, Media & Entertainment, Education & Training, Government & Public Sector"
    )
    subsector: str = Field(description="Specific industry subsector")
    regulatory_requirements: str | None = Field(
        description="Key regulatory requirements and compliance needs"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class BusinessSize(BaseModel):
    """Business size classification based on revenue and employees."""

    category: str = Field(
        description="Size category from: Enterprise & Large Corporate, Middle Market, Small Business & SME, Startups & Emerging Growth, Specialized Segments"
    )
    subcategory: str = Field(
        description="Specific size subcategory with revenue/employee ranges"
    )
    revenue_range: str | None = Field(description="Annual revenue range if mentioned")
    employee_count: str | None = Field(description="Number of employees if mentioned")
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class BusinessCoverage(BaseModel):
    """Geographic coverage and international operations."""

    coverage_type: str = Field(
        description="Coverage type from: Domestic only, Cross-border, Both"
    )
    geographic_footprint: str | None = Field(
        description="Key regions or countries of operation"
    )
    expansion_plans: str | None = Field(
        description="Future international expansion plans"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class TradingTerms(BaseModel):
    """Payment and trading terms with customers and suppliers."""

    customer_terms: str | None = Field(
        description="Payment terms with customers (e.g., 30 days, cash on delivery)"
    )
    supplier_terms: str | None = Field(description="Payment terms with suppliers")
    working_capital_impact: str = Field(
        description="Working capital impact from: Extended credit terms (higher financing needs), Cash on delivery (lower financing needs), Advance payments (negative working capital)"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class TradingCurrencies(BaseModel):
    """Currency exposure and foreign exchange characteristics."""

    currency_exposure: str = Field(
        description="FX exposure type from: Single currency, Multiple currencies, Volatile currencies"
    )
    primary_currencies: list[str] | None = Field(
        description="List of primary trading currencies"
    )
    hedging_needs: str | None = Field(
        description="FX hedging requirements and current practices"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class CashFlowPosition(BaseModel):
    """Cash flow characteristics and financing needs."""

    cash_flow_type: str = Field(
        description="Cash flow position from: Cash generative, Working capital dependent, Seasonal variations"
    )
    seasonality: str | None = Field(description="Seasonal patterns in cash flow")
    financing_needs: str | None = Field(
        description="Working capital and financing requirements"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class CapexFrequency(BaseModel):
    """Capital expenditure patterns and financing needs."""

    capex_pattern: str = Field(
        description="Capex pattern from: Regular capex, Lumpy capex, Minimal capex"
    )
    upcoming_investments: str | None = Field(
        description="Major upcoming capital projects or investments"
    )
    financing_preferences: str | None = Field(
        description="Preferred methods for financing capital investments"
    )
    confidence_score: str = Field(
        description="Overall confidence in extraction: High/Medium/Low"
    )


class ClientInformation(BaseModel):
    """Complete client information extraction based on 8 key categories."""

    business_type: BusinessType
    industry: Industry
    business_size: BusinessSize
    business_coverage: BusinessCoverage
    trading_terms: TradingTerms
    trading_currencies: TradingCurrencies
    cash_flow_position: CashFlowPosition
    capex_frequency: CapexFrequency


class ClientInformationExtractor:
    """Extract structured client information from unstructured text using the 8-category framework."""

    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(api_key=openai_api_key, model="gpt-4", temperature=0)
        self.structured_llm = self.llm.with_structured_output(
            schema=ClientInformation, method="function_calling"
        )

    def extract_client_information(self, client_text: str) -> ClientInformation:
        """
        Extract structured client information from unstructured text.

        Args:
            client_text: Raw client information text (from PDF, manual input, etc.)

        Returns:
            Structured ClientInformation object
        """
        system_prompt = create_extraction_client_information_prompt()
        example_messages = self._create_examples()

        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                *example_messages,
                (
                    "human",
                    f"Extract client information from the following text:\n\n{client_text}",
                ),
            ]
        )

        result = self.structured_llm.invoke(prompt.format_messages())
        return result

    def _create_examples(self) -> list:
        """Create few-shot examples for better extraction."""
        examples = [
            (
                "ABC Manufacturing Ltd is a automotive parts manufacturer with annual revenue of $150M and 400 employees. They export 60% of their production to Europe and Asia, primarily dealing in USD and EUR. Payment terms are typically 45 days from customers. They have seasonal peaks in Q2-Q3 and require significant capex every 2-3 years for new equipment.",
                ClientInformation(
                    business_type=BusinessType(
                        category="Manufacturing & Production",
                        subcategory="Manufacturers",
                        details="Automotive parts manufacturing with export focus",
                    ),
                    industry=Industry(
                        sector="Manufacturing & Industrial",
                        subsector="Automotive",
                        regulatory_requirements="Automotive industry standards and export compliance",
                    ),
                    business_size=BusinessSize(
                        category="Middle Market",
                        subcategory="Core Middle Market ($100M-250M revenue, 200-500 employees)",
                        revenue_range="$150M",
                        employee_count="400",
                    ),
                    business_coverage=BusinessCoverage(
                        coverage_type="Cross-border",
                        geographic_footprint="Europe and Asia exports (60% of production)",
                        expansion_plans="Not mentioned",
                    ),
                    trading_terms=TradingTerms(
                        customer_terms="45 days",
                        supplier_terms="Not mentioned",
                        working_capital_impact="Extended credit terms (higher financing needs)",
                    ),
                    trading_currencies=TradingCurrencies(
                        currency_exposure="Multiple currencies",
                        primary_currencies=["USD", "EUR"],
                        hedging_needs="FX hedging for export revenues",
                    ),
                    cash_flow_position=CashFlowPosition(
                        cash_flow_type="Seasonal variations",
                        seasonality="Peaks in Q2-Q3",
                        financing_needs="Working capital support for seasonal peaks",
                    ),
                    capex_frequency=CapexFrequency(
                        capex_pattern="Lumpy capex",
                        upcoming_investments="Equipment replacement every 2-3 years",
                        financing_preferences="Not specified",
                    ),
                    confidence_score="High",
                ),
            ),
            (
                "XYZ Tech Services is a small IT consulting firm with $5M annual revenue and 25 employees. They work primarily with local businesses in Malaysia and operate on cash payment terms.",
                ClientInformation(
                    business_type=BusinessType(
                        category="Services & Professional",
                        subcategory="Professional Services (consulting, legal, accounting)",
                        details="IT consulting services for local businesses",
                    ),
                    industry=Industry(
                        sector="Technology & Innovation",
                        subsector="Software & IT Services",
                        regulatory_requirements="IT service provider regulations in Malaysia",
                    ),
                    business_size=BusinessSize(
                        category="Small Business & SME",
                        subcategory="Small Business ($2M-10M revenue, 10-25 employees)",
                        revenue_range="$5M",
                        employee_count="25",
                    ),
                    business_coverage=BusinessCoverage(
                        coverage_type="Domestic only",
                        geographic_footprint="Malaysia local market",
                        expansion_plans="Not mentioned",
                    ),
                    trading_terms=TradingTerms(
                        customer_terms="Cash on delivery",
                        supplier_terms="Not specified",
                        working_capital_impact="Cash on delivery (lower financing needs)",
                    ),
                    trading_currencies=TradingCurrencies(
                        currency_exposure="Single currency",
                        primary_currencies=["MYR"],
                        hedging_needs="No FX hedging required",
                    ),
                    cash_flow_position=CashFlowPosition(
                        cash_flow_type="Cash generative",
                        seasonality="Not mentioned",
                        financing_needs="Minimal financing requirements",
                    ),
                    capex_frequency=CapexFrequency(
                        capex_pattern="Regular capex",
                        upcoming_investments="Technology upgrades and equipment",
                        financing_preferences="Not specified",
                    ),
                    confidence_score="High",
                ),
            ),
        ]

        messages = []
        for input_text, expected_output in examples:
            messages.extend(
                tool_example_to_messages(
                    input_text,
                    [expected_output],
                    ai_response="I've analyzed the client information and categorized it according to our 8-category framework.",
                )
            )

        return messages

    def format_extraction_summary(self, client_info: ClientInformation) -> str:
        """Format the extracted client information into a readable summary."""
        summary = f"""**Client Information Summary**

**1. Business Type:** {client_info.business_type.category}
   - Subcategory: {client_info.business_type.subcategory}
   - Details: {client_info.business_type.details}

**2. Industry:** {client_info.industry.sector}
   - Subsector: {client_info.industry.subsector}
   - Regulatory: {client_info.industry.regulatory_requirements or 'Not specified'}

**3. Business Size:** {client_info.business_size.category}
   - Classification: {client_info.business_size.subcategory}
   - Revenue: {client_info.business_size.revenue_range or 'Not specified'}
   - Employees: {client_info.business_size.employee_count or 'Not specified'}

**4. Coverage:** {client_info.business_coverage.coverage_type}
   - Geographic Footprint: {client_info.business_coverage.geographic_footprint or 'Not specified'}
   - Expansion Plans: {client_info.business_coverage.expansion_plans or 'Not specified'}

**5. Trading Terms:** {client_info.trading_terms.working_capital_impact}
   - Customer Terms: {client_info.trading_terms.customer_terms or 'Not specified'}
   - Supplier Terms: {client_info.trading_terms.supplier_terms or 'Not specified'}

**6. Trading Currencies:** {client_info.trading_currencies.currency_exposure}
   - Primary Currencies: {', '.join(client_info.trading_currencies.primary_currencies or ['Not specified'])}
   - Hedging Needs: {client_info.trading_currencies.hedging_needs or 'Not specified'}

**7. Cash Flow Position:** {client_info.cash_flow_position.cash_flow_type}
   - Seasonality: {client_info.cash_flow_position.seasonality or 'Not specified'}
   - Financing Needs: {client_info.cash_flow_position.financing_needs or 'Not specified'}

**8. Capex Frequency:** {client_info.capex_frequency.capex_pattern}
   - Upcoming Investments: {client_info.capex_frequency.upcoming_investments or 'Not specified'}
   - Financing Preferences: {client_info.capex_frequency.financing_preferences or 'Not specified'}

**Confidence Score:** {client_info.confidence_score}
"""
        return summary
