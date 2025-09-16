# Trade Collection - Seller Post-shipment Decision Diagram

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">Trade Collection Seller</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Post-shipment Decision Diagram</span>" } --> OutwardBill["Outward Bill for Collection"]
    OutwardBill --> PaymentTerms{"What payment terms is the seller using: D/P or D/A?"}
    PaymentTerms -- D/P --> EndDP["Transaction completed when buyer pays at sight"]
    PaymentTerms -- D/A --> CalcGap["Calculate financing gap<br>with D/A formula"]
    CalcGap --> NeedFinancing{"Does seller need financing based on gap calculation?"}
    NeedFinancing -- Yes --> BillReceivable["Bill Receivable under Outward Bill for Collection"]
    NeedFinancing -- No --> WaitMaturity["Wait until maturity<br>for buyer to pay"]
    BillReceivable --> EndDA["Transaction completed at maturity when buyer pays under D/A"]
    WaitMaturity --> EndDA

    Start@{ shape: stadium}
    CalcGap@{ shape: rect}
    WaitMaturity@{ shape: rect}
     OutwardBill:::productBox
     BillReceivable:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```
