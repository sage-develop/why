## Prompt

Create a Mermaid decision tree for Trade Finance Collections by
starting with "Start: Trade Purchase Financing"
then ask the following questions:

- Does the client have a financing gap based on Cash Conversion Cycle?
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
    A(["Start: Trade Purchase Financing"]) --> n1["Context: Client is buying goods and may need<br>financing to pay suppliers before<br>receiving payment from their customers"]
    n1 --> n2["Does the client generally finance their purchases?"]
    n2 -- Yes --> J["Does the client have a financing gap<br>based on Cash Conversion Cycle?"]
    n2 -- No --> n3["No financing opportunity"]
    J -- Yes --> n4["Who has title to the goods?"]
    J -- No --> L["Proceed without financing"]
    n4 -- The bank --> T@{ label: "<span style=\"background-color:\">Opportunity: <br>Trust Receipt Loan, <br>P/N under Trade Collections, <br>Invoice Financing</span>" }
    n4 -- The buyer --> P1@{ label: "<span style=\"background-color:\">Opportunity: <br>P/N under </span>Trade Collections<span style=\"background-color:\">, <br>Invoice Financing</span>" }
    n4 -- Not sure --> P2@{ label: "<span style=\"background-color:\">Opportunity: <br>P/N under Trade Collections, <br>Invoice Financing</span>" }
    L --> M["Who has title to the goods?"]
    M -- The buyer --> N["Use B/L directly to claim goods"]
    M -- The bank --> O["Opportunity: Endorsement Services"]
    T --> n5["Opportunity: Endorsement Services"]

    n2@{ shape: diam}
    J@{ shape: diam}
    n3@{ shape: rect}
    n4@{ shape: diam}
    T@{ shape: rect}
    P1@{ shape: rect}
    P2@{ shape: rect}
    M@{ shape: diam}
    n5@{ shape: rect}
     T:::productBox
     P1:::productBox
     P2:::productBox
     O:::productBox
     n5:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
