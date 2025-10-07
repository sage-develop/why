## Prompt

Create a Mermaid decision tree for Trade Finance Collections by asking the following questions?

- Do the goods usually arrive before the documents?
  If not, then Opportunity: Inward Bill for Collection.
- Does the buyer want to claim goods immediately after goods arrive?
  If not, then Opportunity: Inward Bill for Collection.
  If the answer is yes to both, then Opportunity: Shipping Guarantee

## Decision Tree

```mermaid
%% Trade Finance Collection Decision Tree

flowchart TD
    Start[Start: Collection] --> A{Do the goods usually arrive before the documents?}
    A -->|No| B[Opportunity: Inward Bill for Collection]
    A -->|Yes| C{Does the buyer want to claim goods immediately after goods arrive?}
    C -->|No| B
    C -->|Yes| D[Opportunity: Shipping Guarantee]
    D --> B
```
