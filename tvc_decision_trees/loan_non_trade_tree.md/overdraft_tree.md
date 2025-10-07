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
   Start(["Start: Non-Trade Transaction<br>(Overdraft)"]) --> Context["Context: Client needs to make<br>non-trade payments but lacks<br>sufficient cash on hand"]
   Context --> Q1{"Does buyer have sufficient<br>cash for payment?"}
   Q1 -- Yes --> End1["Make payment with<br>existing funds"]
   Q1 -- No --> Q2{"What type of non-trade<br>payment is needed?"}
   Q2 -- Equipment/Services<br>down payment --> Q3{"Is this an<br>urgent payment?"}
   Q2 -- Other business<br>payments --> Q4{"Does buyer want to<br>preserve cash flow?"}
   Q3 -- Yes --> P1["Opportunity: Overdraft"]
   Q3 -- No --> Q4
   Q4 -- Yes --> P2["Opportunity: Overdraft"]
   Q4 -- No --> End2["No opportunity"]
```
