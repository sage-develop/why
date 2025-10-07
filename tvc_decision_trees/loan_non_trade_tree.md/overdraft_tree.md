## Prompt

Create a Mermaid decision tree diagram for Non-Trade Transactions (Overdraft).
Follow these steps:

1. Start: "Non-Trade Transaction (Overdraft)".  
   → Ask: "Does the buyer have sufficient cash for payment?"

   - If Yes → "Make payment with existing funds".
   - If No → continue.

2. If No cash: Ask "What type of non-trade payment is needed?"

   - If Equipment/Services down payment → Ask: "Is this an urgent payment?"
     - If Yes → "Overdraft".
     - If No → Continue to the next question.
   - If Other business payments → continue to next question.

3. Next question: "Does the buyer want to preserve cash flow?"
   - If Yes → "Overdraft".
   - If No → "No opportunity".

## Decision tree

```mermaid
flowchart TD
    Start(["Start: Non-Trade Transaction<br>(Overdraft)"]) --> Context["Context: The client faces cash flow gaps or urgent funding needs<br>not related to import/export trade."]
    Context --> Q1{"Does the buyer have sufficient<br>cash available for payment?"}
    Q1 -- Yes --> End1["Make payment with<br>existing funds"]
    Q1 -- No --> Q2{"What type of non-trade<br>payment is needed?"}
    Q2 -- Equipment / Services<br>Down Payment --> Q3{"Is this payment time-sensitive<br>or contractually urgent?"}
    Q2 -- "Operating Expenses<br>(e.g. rent, utilities, salaries)" --> Q4{"Does the client want to preserve<br>cash for daily operations?"}
    Q2 -- Tax or Government<br>Obligations --> P1["Opportunity: Overdraft<br>(short-term compliance payment)"]
    Q2 -- Debt Repayment /<br>Installment Due --> Q5{"Is refinancing available or preferred?"}
    Q2 -- "Other Business Needs<br>(e.g. insurance, maintenance)" --> Q4
    Q3 -- Yes --> P1a["Opportunity: Overdraft<br>(bridge urgent payment)"]
    Q3 -- No --> Q4
    Q4 -- Yes --> P2["Opportunity: Overdraft<br>(cash flow preservation)"]
    Q4 -- No --> End2["No opportunity<br>"]
    Q5 -- Yes --> End3["Consider refinancing<br>or restructuring"]
    Q5 -- No --> P1b["Opportunity: Overdraft<br>(bridge short-term repayment)"]
```
