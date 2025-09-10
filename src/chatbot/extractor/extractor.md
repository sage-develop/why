# Extractor Module Documentation

## What This Module Does

The **extractor** module handles extracting structured information from unstructured client text (like PDFs, descriptions, etc.) and converting it into two useful formats:

1. **Client Categorization** - Organizing client info into 8 business categories
2. **Decision Tree Pre-answering** - Finding questions that can be answered automatically

## Files

### client_information.py
**Purpose**: Categorizes clients into structured business profiles

**What it contains**:
- **8 Business Category Models**: BusinessType, Industry, BusinessSize, BusinessCoverage, TradingTerms, TradingCurrencies, CashFlowPosition, CapexFrequency
- **ClientInformation** - combines all 8 categories
- **ClientInformationExtractor** - AI that reads text and fills out the categories
- **Examples** - sample client descriptions with expected outputs

**Example**:
```python
# Input: "ABC Manufacturing Ltd is a automotive parts manufacturer with $150M revenue..."
# Output: 
ClientInformation(
    business_type=BusinessType(category="Manufacturing & Production", subcategory="Manufacturers"),
    industry=Industry(sector="Manufacturing & Industrial", subsector="Automotive"),
    business_size=BusinessSize(category="Middle Market", revenue_range="$150M"),
    # ... 5 more categories
)
```

### preanswer.py  
**Purpose**: Pre-answers decision tree questions from client information

**What it contains**:
- **DecisionTreeAnswer** - a single pre-answered question
- **PreAnsweredQuestions** - collection of multiple pre-answers
- **PreAnswerExtractor** - AI that reads client text and decision tree questions, then matches them
- **Examples** - sample texts with decision tree answers

**Example**:
```python
# Input: "The company wants to hedge 70% of their FX exposure"
# Output:
PreAnsweredQuestions(answers=[
    DecisionTreeAnswer(
        node_id="hedge_decision_importer",
        question="Do you want to hedge FX risk for imports?",
        chosen_answer="Yes",
        confidence="High"
    ),
    DecisionTreeAnswer(
        node_id="hedge_decision_exporter", 
        question="Do you want to hedge FX risk for exports?",
        chosen_answer="Yes",
        confidence="High"
    )
])
```

### extractor.py
**Purpose**: Combines both client categorization AND pre-answering in one AI call

**What it contains**:
- **ClientAnalysis** - combines ClientInformation + PreAnsweredQuestions
- **ClientExtractor** - main AI that does both tasks at once (more efficient)
- **Combined examples** - samples that show both categorization and pre-answering

**Example**:
```python
# Input: "ABC Manufacturing exports to Europe, deals in USD/EUR, wants to hedge 70% of FX exposure"
# Output:
ClientAnalysis(
    client_information=ClientInformation(...),  # All 8 business categories filled
    pre_answered_questions=[...],               # Decision tree questions pre-answered  
    confidence_score="High"
)
```

## Complete Flow

1. **Load Decision Trees**: Chatbot loads trees from `src/decision_trees/*.md` on startup
2. **PDF + Text Upload**: User uploads client PDF and/or enters text in Streamlit
3. **Combined Input**: App combines PDF text + manual text input  
4. **AI Analysis**: `ClientExtractor` analyzes combined text using decision tree context:
   - Extracts structured client profile (8 categories)
   - Pre-answers decision tree questions based on the text
5. **Smart Navigation**: System uses pre-answers to skip obvious questions
6. **Product Recommendations**: Reaches final recommendations faster

## Example Flow

```
User uploads: "ABC Corp annual report.pdf"
     ↓
Text: "ABC Corp manufactures automotive parts, $150M revenue, exports 60% to Europe..."
     ↓  
ClientExtractor analyzes and produces:
     ↓
ClientAnalysis {
    client_information: {
        business_type: "Manufacturing & Production",
        industry: "Automotive", 
        business_size: "Middle Market ($150M)",
        business_coverage: "Cross-border exports",
        ...
    },
    pre_answered_questions: [
        "What is client's business activity?" → "Both Importer & Exporter",
        "Do you want to hedge FX risk?" → "Yes"
    ]
}
     ↓
Decision tree starts at appropriate node, skips pre-answered questions
     ↓
User only gets asked remaining unknown questions
     ↓
Final product recommendations
```

This makes the consultation much faster and more relevant by automatically extracting client info and skipping obvious questions.
