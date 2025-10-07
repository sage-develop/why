## Prompt

Create a Mermaid decision tree for Trade Finance Letter of Credit Shipping Guarantee by asking the following questions:

- Do the goods usually arrive before the documents?
  if No, "No Opportunity"
  if Yes, ask:
  - Does the buyer want to claim goods immediately after goods arrive?
    if Yes, "Opportunity: Shipping Guarantee"
    if No, "No Opportunity"

## Decision Tree

```mermaid
%% Letter of Credit Shipping Guarantee
flowchart TD
    Start[Start: Letter of Credit Shipping Guarantee] --> A[Context: Now, goods have arrived in your country. I will explore with you on how to claims the goods under Letter of Credit]
    A --> B{Do the goods usually arrive before the documents}
    B -->|No| C[No Opportunity]
    B -->|Yes| D{Does the buyer want to claim the goods immediately upon arrival?}
    D -->|No| C
    D -->|Yes| E[Opportunity: Shipping Guarantee]
```
