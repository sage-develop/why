## Prompt

Create a Mermaid decision tree for Trade Finance Collections Shipping Guarantee by asking the following questions?

- Do the goods usually arrive before the documents?
- Does the buyer want to claim goods immediately after goods arrive?

## Decision Tree

```mermaid
%% Trade Collections Shipping Guarantee
flowchart TD
    Start[Start: Trade Collections Shipping Guarantee] --> A[Context: Now, goods have arrived in your country. I will explore with you on how to claims the goods under Trade Collections]
    A --> B{Do the goods usually arrive before the documents}
    B -->|No| C[No Opportunity]
    B -->|Yes| D{Does the buyer want to claim the goods immediately upon arrival?}
    D -->|No| C
    D -->|Yes| E[Opportunity: Shipping Guarantee]
```
