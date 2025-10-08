## Prompt

Create a Mermaid decision tree diagram for "Payment Services".
The products in this diagram are FX Spot/Forward and Outward Remittance.
Follow these decision questions step by step:

1. Is the invoice in local or foreign currency?

   - If Local Currency → "Domestic Transfer"
   - If Foreign Currency → continue.

2. If Foreign: Is the payment domestic or cross-border?
   - If Domestic → ask: Is payment due immediately or in the future?
     - If Immediate → "Opportunity: FX Spot only + Domestic Transfer"
     - If Future → "Opportunity: FX Forward only + Domestic Transfer"
   - If Cross-border → ask: Is payment due immediately or in the future?
     - If Immediate → "Opportunity: FX Spot + Outward Remittance"
     - If Future → "Opportunity: FX Forward + Outward Remittance"

### Decision Tree

```mermaid
---
config:
  theme: redux
---
flowchart TD
    Start(["Payment Services Decision"]) --> Context["Context: Client needs to make payments<br>and may require currency exchange<br>or international transfer services"]
    Context --> Q1{"Is the invoice in<br>local or foreign currency?"}
    Q1 -- Local Currency --> DT["Opportunity: Domestic Transfer"]
    Q1 -- Foreign Currency --> Q2{"Is the payment domestic<br>or cross-border?"}
    Q2 -- Domestic --> Q3{"Is payment due<br>immediately or in the future?"}
    Q2 -- "Cross-border" --> Q4{"Is payment due<br>immediately or in the future?"}
    Q3 -- Immediate --> FXS1["Opportunity: FX Spot + Domestic Transfer"]
    Q3 -- Future --> FXF1["Opportunity: FX Forward + Domestic Transfer"]
    Q4 -- Immediate --> FXS2["Opportunity: FX Spot + Outward Remittance"]
    Q4 -- Future --> FXF2["Opportunity: FX Forward + Outward Remittance"]
     FXS1:::Sky
     FXF1:::Sky
     FXS2:::Sky
     FXF2:::Sky
    classDef Sky stroke-width:1px, stroke-dasharray:none, stroke:#374D7C, fill:#E2EBFF, color:#374D7C
```
