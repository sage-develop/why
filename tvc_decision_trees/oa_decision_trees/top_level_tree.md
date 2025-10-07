## Prompt

Create a Mermaid decision tree for Trade Finance Open Account by asking
Start with "Start: Open Account Decision Tree"
Then next level has 2 nodes in parallel
Purchase Financing tree
Payment Services tree

## Decision Tree

```mermaid
%% Trade Finance Open Account - High Level Decision Tree

flowchart TD
A[Start: Trade Finance OA Decision Tree]
A --> B[Context: The client is making purchases under Open Account terms.]
B --> C[Purchase Financing tree]
B --> E[Payment Services tree]
```
