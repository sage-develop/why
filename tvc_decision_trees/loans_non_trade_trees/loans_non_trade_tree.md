## Prompt

Create a Mermaid decision tree diagram for Non-Trade Transactions (Overdraft).
Follow these steps:

1. Start: "Non-Trade Transaction (Overdraft)" with context about cash flow gaps and urgent funding needs.

2. Ask: "Does the client have sufficient funds for their business needs?"

   - If Yes → "No non-trade financing opportunity"
   - If No → continue

3. Ask: "Does the client need flexible access to funds for cash flow gaps?"

   - If Yes → continue
   - If No → "Opportunity: Term Loan"

4. Ask: "Do they prefer no fixed repayment schedule?"

   - If Yes → Warning about usage
   - If No → "Opportunity: Term Loan"

5. Warning: "Will they avoid excessive or long-term usage to prevent high costs?"
   - If Yes → "Opportunity: Overdraft"
   - If No → "Caution: Overdraft may become expensive"

## Decision tree

```mermaid
flowchart TD
    Start(["Start: Non-Trade Transaction<br>(Overdraft)"]) --> Context["Context: The client may face cash flow gaps or urgent funding needs when handling regular business expenses."]
    Context --> Q0{"Does the client have<br>sufficient funds for<br>their business needs?"}
    Q0 -- Yes --> NoLoan["No non-trade financing opportunity"]
    Q0 -- No --> Q1{"Does the client need<br>flexible access to funds<br>for cash flow gaps?"}
    Q1 -- Yes --> Q2{"Do they prefer no fixed<br>repayment schedule?"}
    Q1 -- No --> NotSuitable1["Opportunity: Term Loan<br>"]
    Q2 -- Yes --> Warning{"Warning: Will they avoid<br>excessive or long-term<br>usage to prevent high costs?"}
    Q2 -- No --> NotSuitable2["Opportunity: Term Loan<br>"]
    Warning -- Yes --> Overdraft["Opportunity: Overdraft<br>✓ Flexible credit facility<br>✓ Interest on used amount only<br>✓ No fixed repayment schedule"]
    Warning -- No --> Caution["Caution: Overdraft may become<br>expensive - consider alternatives<br>or usage guidelines"]
```
