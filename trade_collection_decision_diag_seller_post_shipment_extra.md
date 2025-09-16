# Trade Collection - Seller Post-shipment Decision Diagram (With Extra Products)

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">Trade Collection Seller</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Post-shipment Decision Diagram</span>" } --> OutwardBill["Outward Bill for Collection"]
    OutwardBill --> PaymentTerms{"What payment terms is the seller using: D/P or D/A?"}
    PaymentTerms -- D/P --> EndDP["Transaction completed when buyer pays at sight"]
    PaymentTerms -- D/A --> CalcGap["Calculate financing gap<br>with D/A formula"]
    CalcGap --> NeedFinancing{"Does seller need financing based on gap calculation?"}
    NeedFinancing -- Yes --> FinancingOptions{"What type of financing does seller prefer?"}
    NeedFinancing -- No --> WaitMaturity["Wait until maturity<br>for buyer to pay"]
    FinancingOptions -- Normal D/A financing with discount --> BillReceivable["Bill Receivable under Outward Bill for Collection"]
    FinancingOptions -- Immediate advance, seller guarantees repayment --> DRF1["Direct Recourse Financing"]
    FinancingOptions -- Immediate cash, no seller obligation --> OBP1["Outward Bill Purchased"]
    BillReceivable --> EndDA["Transaction completed at maturity when buyer pays under D/A"]
    DRF1 --> EndDRF@{ label: "Get cash now, refund bank if buyer doesn't pay" }
    OBP1 --> EndOBP["Transaction completed - seller gets cash, no further obligation"]
    WaitMaturity --> EndDA

    Start@{ shape: stadium}
    EndDP@{ shape: rect}
    CalcGap@{ shape: rect}
    WaitMaturity@{ shape: rect}
    EndDA@{ shape: rect}
    EndDRF@{ shape: rect}
    EndOBP@{ shape: rect}
     OutwardBill:::productBox
     FinancingOptions:::newDecisionBox
     BillReceivable:::productBox
     DRF1:::newProductBox
     OBP1:::newProductBox
     EndDRF:::newDecisionBox
     EndOBP:::newDecisionBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    classDef newProductBox fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#c62828
    classDef newDecisionBox fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#d81b60
```

## Decision Points Summary

1. **Start**: Seller has shipped goods and is using Trade Collection payment method (mandatory Outward Bill for Collection)
2. **Payment Terms**: Determine if using D/A (Documents against Acceptance) or D/P (Documents against Payment)
3. **Financing Need**: For D/A, calculate financing gap and determine if financing is needed
4. **Financing Options**: If financing needed, choose between standard, recourse, or non-recourse financing options

## Product Flow Conclusions

- **D/P Path**: Transaction completed when buyer pays at sight
- **D/A + No Financing**: Wait until maturity for buyer to pay
- **D/A + Bill Receivable**: Standard financing with recourse, completed at maturity
- **D/A + DRF**: Get advance cash with recourse - seller must refund if buyer doesn't pay
- **D/A + OBP**: Seller gets immediate cash with no further obligation

## New Products Added

### Direct Recourse Financing (DRF)

- **Product Type**: A post-shipment financing for sellers with recourse
- **How It Works**:
  - Bank gives seller money in advance
  - If buyer doesn't pay, seller must refund the bank
- **Use When**:
  - Seller needs advance funds and trusts buyer will pay at maturity
  - Seller wants immediate cash but accepts the risk
- **Risk**: Seller bears ultimate responsibility if buyer defaults

### Outward Bill Purchased (OBP)

- **Product Type**: A post-shipment financing for sellers without recourse
- **How It Works**:
  - Seller gets immediate cash with no further obligation
  - Bank handles all buyer payment risk
- **Use When**:
  - Seller wants immediate cash instead of waiting 30-60 days
  - Seller wants bank to handle buyer payment risk completely
- **Benefits**: No further obligation for seller after transaction

Both new products appear once in the diagram and offer distinct financing options with different risk profiles:

- **DRF**: For sellers who trust the buyer will pay and need advance cash with recourse
- **OBP**: For sellers who want immediate cash with no further obligations or risk
