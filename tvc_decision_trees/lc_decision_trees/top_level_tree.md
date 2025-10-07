## Prompt

Create a Mermaid decision tree for Trade Finance Letter of Credit
Start with "Start: Trade Finance LC Top Level"
The next level is "Opportunity: LC Issuance"
Then next level has 3 nodes in parallel:
Purchase Financing tree
LC Shipping Guarantee tree
Payment Services tree

## Decision Tree

```mermaid
%% Trade Finance Letter of Credit - Top Level Decision Tree

flowchart TD
    A[Start: Trade Finance LC Top Level]
    A --> B[Opportunity: LC Issuance]
    B --> C[Purchase Financing tree]
    B --> D[LC Shipping Guarantee tree]
    B --> E[Payment Services tree]
```
