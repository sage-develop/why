## Prompt

Create a Mermaid decision tree for Trade Finance Letter of Credit
Start with "Start: Trade Finance Letter of Credit Top Level"
The next level is "Opportunity: Letter of Credit Issuance"
Then next level has 3 nodes in parallel:
Purchase Financing tree
Letter of Credit Shipping Guarantee tree
Payment Services tree

## Decision Tree

```mermaid
%% Trade Finance Letter of Credit - Top Level Decision Tree

flowchart TD
    A[Start: Trade Finance Letter of Credit Top Level]
    A --> B[Opportunity: Letter of Credit Issuance]
    B --> C[Purchase Financing tree]
    B --> D[Letter of Credit Shipping Guarantee tree]
    B --> E[Payment Services tree]
```
