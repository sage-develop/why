## Prompt

Create a Mermaid decision tree for Trade Open Account Purchase Financing by asking the following questions

- Can the buyer pay the seller on the due date?
  If yes, then "The buyer continues with standard Open Account terms.<br>No additional financing products needed."
  If no, "P/N under Open Account - Buyer / Invoice Financing”

## Decision Tree

```mermaid
flowchart TD
   Start(["Start: Open Account Purchase Financing"]) --> Context["Context: Client is buying goods and may need<br>financing to pay suppliers before<br>receiving payment from their customers"]
   Context --> Q1{"Can the buyer pay the seller on the due date?"}
   Q1 -- Yes --> End1["The buyer continues with standard Open Account terms.<br>No additional financing products needed."]
   Q1 -- No --> Product1["P/N under Open Account - Buyer / Invoice Financing"]
   Product1 --> End2["The buyer receives pre-shipment financing to meet payment obligations.<br>This completes the financing solution for Open Account transactions."]

   Product1:::productBox
   classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
