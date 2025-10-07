## Prompt

Create a Mermaid decision tree for Trade Finance Collections Shipping Guarantee by asking the following questions?

- Do the goods usually arrive before the shipping documents?
- Does the buyer want to claim the goods before documents arrive?

## Decision Tree

```mermaid
%% Trade Collections Shipping Guarantee
flowchart TD
    Start[Start: Trade Collections Shipping Guarantee] --> A[Context: Now, goods have arrived in your country. I will explore with you on how to claims the goods under Trade Collections]
    A --> B{"Do the goods usually arrive before the<br>shipping documents?"}
    B -- No --> C["Opportunity: Inward Bill for Collection"]
    B -- Yes --> D{"Does the buyer want to claim the goods<br>before documents arrive?"}
    D -- Yes --> E["Opportunity: Shipping Guarantee Issuance"]
    D -- No --> C
    E --> C
```
