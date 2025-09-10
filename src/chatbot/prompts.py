from src.chatbot.decision_tree import DecisionNode


def create_extract_preanswer_prompt(decision_context: str) -> str:
    """Create system prompt for extracting pre-answers from client information and client annual report."""
    return f"""You are analyzing client information and/or client annual report to pre-answer questions from a Global Markets product consultation decision tree.

Your task:
1. Review the decision tree nodes and their available choices
2. Identify which questions can be clearly answered based on the client information  
3. ONLY extract answers where the client information CLEARLY indicates a specific choice
4. Use EXACT choice text from the decision tree options
5. Assign confidence levels: High (explicitly stated), Medium (strongly implied), Low (unclear)

Decision Tree Context:
{decision_context}

IMPORTANT: Only include answers where you have medium or high confidence. When in doubt, don't extract."""


def create_extraction_client_information_prompt() -> str:
    """Create the system prompt for client information extraction."""
    return """You are an expert relationship manager analyzing client information to categorize them according to our 8-category framework.

Your task is to extract and categorize client information into these 8 categories:

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

IMPORTANT: Only use categories and subcategories that exist in our framework. If information is unclear or missing, use the most appropriate general category and note low confidence."""
