# Letter of Credit Products - Seller Pre-shipment Decision Tree (With Extra Products)

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">LC Seller Pre-shipment</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Decision Diagram</span>" } --> LCAdvising["Letter of Credit Advising"]
    LCAdvising --> RiskConcern{"Worried about counterparty risk or counterparty sovereign risk?"}
    RiskConcern -- Yes --> LCConfirm["Letter of Credit Confirmation"]
    RiskConcern -- No --> CheckMiddleman@{ label: "Is seller a middleman who doesn't make goods?" }
    LCConfirm --> CheckMiddleman
    CheckMiddleman -- Yes --> TransferableCheck{"Is LC transferable?"}
    TransferableCheck -- Yes --> WantTransfer{"Want to transfer LC to supplier?"}
    WantTransfer -- Yes --> LCTransfer["Letter of Credit Transferring"]
    WantTransfer -- No --> BackToBackCheck{"Does the seller need more control OR different LC terms (amounts, dates, documents)?"}
    TransferableCheck -- No --> BackToBackCheck
    LCTransfer --> End1["Flow ends here - Middleman transferred LC"]
    CheckMiddleman -- No --> CheckAssign{"Want to redirect payments to third parties?"}
    BackToBackCheck -- Yes --> BackToBackLC["Back-to-Back LC"]
    BackToBackCheck -- No --> CheckAssign
    BackToBackLC --> CheckAssign
    CheckAssign -- Yes --> AssignProceeds["Assignment of Proceeds under Letter of Credit"]
    CheckAssign -- No --> CheckPacking{"Need pre-shipment working capital?"}
    AssignProceeds --> CheckPacking
    CheckPacking -- Yes --> ECRCheck{"Is government export credit program available AND (want to expand exports OR reduce financing costs)?"}
    CheckPacking -- No --> ContinueFlow@{ label: "Continue to post-shipment<br style=\"--tw-scale-x:\">products or complete transaction" }
    ECRCheck -- Yes --> ECR["Export Credit Refinancing"]
    ECRCheck -- No --> PackingCredit["Packing Credit for Exporters"]
    ECR --> ContinueFlow
    PackingCredit --> ContinueFlow

    Start@{ shape: stadium}
    CheckMiddleman@{ shape: diamond}
    ContinueFlow@{ shape: rect}
     LCAdvising:::productBox
     LCConfirm:::productBox
     LCTransfer:::productBox
     BackToBackCheck:::newDecisionBox
     BackToBackLC:::newProductBox
     AssignProceeds:::productBox
     ECRCheck:::newDecisionBox
     ECR:::newProductBox
     PackingCredit:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    classDef newProductBox fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#c62828
    classDef newDecisionBox fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#d81b60
```

## Decision Points Summary

1. **Start**: Seller is using LC payment method (mandatory Letter of Credit Advising)
2. **Risk Concern**: Check if seller is worried about counterparty risk or sovereign risk
3. **Middleman Check**: Determine if seller is a middleman who doesn't manufacture goods
4. **Transferable Check**: For middlemen, check if the LC is transferable
5. **Transfer Intent**: If transferable, check if seller wants to transfer LC to supplier
6. **Back-to-Back LC Check**: If not transferring or LC not transferable, assess if seller needs more control or different LC terms
7. **Assignment Check**: Check if seller wants to redirect payments to third parties
8. **Working Capital Check**: Determine if seller needs pre-shipment working capital
9. **ECR Eligibility**: For working capital needs, check if government export credit program is available and seller wants to expand exports or reduce costs

## Product Flow Conclusions

- **LC Transfer Path**: Middleman transfers LC to supplier - flow ends
- **Back-to-Back LC Path**: Seller gets bank to issue new LC to supplier using original LC as security, provides more control and flexibility
- **ECR Path**: Government-subsidized financing with cheaper rates for export expansion
- **Standard Packing Credit Path**: Traditional pre-shipment working capital financing
- **Assignment Path**: Payments redirected to specified third parties
- **No Working Capital Path**: Continue to post-shipment products or complete transaction

## New Products Added

### Back-to-Back LC

- **Product Type**: A financing/guarantee for Sellers who act as middlemen (Pre-shipment timing)
- **How It Works**:
  - Seller uses the original LC agreed with buyer as security
  - Bank issues another LC to the supplier on behalf of the seller
- **Use When**:
  - Original LC is NOT transferable
  - Seller needs more control over the transaction
  - LC terms need to be different (amounts, dates, documents)
- **Benefits**:
  - Provides flexibility when LC Transfer is not suitable
  - Allows middleman to maintain control over supplier relationship
  - Enables customization of terms for supplier LC

### Export Credit Refinancing (ECR)

- **Product Type**: A government-subsidized financing for sellers (Pre-shipment)
- **How It Works**:
  - Central bank/export agency provides cheap funds to commercial banks
  - Commercial banks pass on cheaper rates to sellers
  - "Government helps banks so banks help sellers"
- **Use When**:
  - Government export credit program is available
  - Seller wants to expand exports but concerned about financing costs
  - Seller wants to reduce interest rates to make export deal viable
- **Benefits**:
  - Cheaper credit for sellers compared to standard rates
  - Government backing reduces financing costs
  - Supports export expansion and competitiveness
- **Decision Point**: Check if both government program availability and seller's expansion/cost concerns align
