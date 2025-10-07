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
