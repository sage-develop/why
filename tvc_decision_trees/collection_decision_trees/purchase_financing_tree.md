## Prompt

Create a Mermaid decision tree for Trade Finance Collections by
starting with "Start: Trade Purchase Financing"
then ask the following questions:

- Do you have a financing gap based on Cash Conversion Cycle?
  If no, "Proceed without financing"
  If yes, then "Opportunity: P/N under Bill for Collection / Invoice Financing".
- Who has title to the goods?
  If it's the bank, then "Endorsement Services".
  If it's the buyer, "Use B/L directly to claim goods".
- Was Shipping Guarantee Issuance used earlier?
  If yes, "Exchange B/L for Shipping Guarantee to complete flow" then "Trade Collection transaction completed successfully".
  If no, "Trade Collection transaction completed successfully".

## Decision Tree

```mermaid
%% Trade Finance Collection Decision Tree

flowchart TD
   J{"Do you have a financing gap based on Cash Conversion Cycle?"} -- Yes --> K["Opportunity: P/N under Bill for Collection / Invoice Financing"]
   J -- No --> L["Proceed without financing"]
   K --> M{"Who has title to the goods?"}
   L --> M
   M -- The buyer --> N["Use B/L directly to claim goods"]
   M -- The bank --> O["Endorsement Services"]
   O --> P{"Was Shipping Guarantee Issuance used earlier?"}
   N --> P
   P -- Yes --> Q["Exchange B/L for Shipping Guarantee to complete flow"]
   P -- No --> R["Trade Collection transaction completed successfully"]
   Q --> R
   A(["Start: Trade Purchase Financing"]) --> n1@{ label: "Context: Now, let's explore about purchase financing under Trade Collections" }
   n1 --> J


   K:::productBox
   classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
