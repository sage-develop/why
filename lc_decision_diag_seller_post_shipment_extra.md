# Letter of Credit Products - Seller Post-shipment Decision Tree (With Extra Products)

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">LC Seller Post-shipment</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Decision Diagram</span>" } --> LCTypeCheck{"What type of LC<br>is the seller using?"}
    LCTypeCheck -- "Sight LC" --> SightCalc["Calculate financing gap<br>with Sight LC formula"]
    LCTypeCheck -- "Usance LC" --> UsanceCalc["Calculate financing gap<br>with Usance LC formula"]
    SightCalc --> SightFinanceCheck{"Does seller need financing based on gap calculation?"}
    UsanceCalc --> UsanceFinanceCheck{"Does seller need financing based on gap calculation?"}

    SightFinanceCheck -- Yes --> ECRAvailableSight{"Is a government Export Credit Refinancing program available for this transaction?"}
    SightFinanceCheck -- No --> SightWait@{ label: "Wait until buyer's bank<br>pays at sight" }

    UsanceFinanceCheck -- Yes --> ECRAvailableUsance{"Is a government Export Credit Refinancing program available for this transaction?"}
    UsanceFinanceCheck -- No --> UsanceWait@{ label: "Wait until maturity date<br>for buyer's bank to pay" }

    ECRAvailableSight -- No --> ExportBill["Export Bill under Letter of Credit"]
    ECRAvailableSight -- Yes --> ECRWantSight{"Does the client want to use the program (cheaper cost but with eligibility/paperwork)?"}

    ECRAvailableUsance -- No --> BillReceivable["Bill Receivable under Letter of Credit"]
    ECRAvailableUsance -- Yes --> ECRWantUsance{"Does the client want to use the program (cheaper cost but with eligibility/paperwork)?"}

    ECRWantSight -- Yes --> ECRPostSight["Export Credit Refinancing Post"]
    ECRWantSight -- No --> ExportBill["Export Bill under Letter of Credit"]

    ECRWantUsance -- Yes --> ECRPostUsance["Export Credit Refinancing Post"]
    ECRWantUsance -- No --> BillReceivable["Bill Receivable under Letter of Credit"]

    ExportBill --> SightComplete["Transaction completed"]
    ECRPostSight --> SightCompleteECR["Transaction completed"]
    BillReceivable --> UsanceComplete@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }
    ECRPostUsance --> UsanceCompleteECR@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }
    SightWait --> SightCompleteWait["Transaction completed"]
    UsanceWait --> UsanceCompleteWait@{ label: "Transaction completed<br>at LC maturity when<br>buyer's bank pays" }

    Start@{ shape: stadium}
    SightWait@{ shape: rect}
    UsanceWait@{ shape: rect}
    UsanceComplete@{ shape: rect}
    UsanceCompleteECR@{ shape: rect}
    UsanceCompleteWait@{ shape: rect}
    ExportBill:::productBox
    BillReceivable:::productBox
    ECRAvailableSight:::newDecisionBox
    ECRAvailableUsance:::newDecisionBox
    ECRWantSight:::newDecisionBox
    ECRWantUsance:::newDecisionBox
    ECRPostSight:::newProductBox
    ECRPostUsance:::newProductBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
    classDef newProductBox fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#c62828
    classDef newDecisionBox fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#d81b60
```

## Decision Points Summary

1. **Start**: Seller is using LC payment method and has shipped goods (post-shipment timing)
2. **LC Type Check**: Determine if seller is using Sight LC or Usance LC
3. **Financing Gap Calculation**: Calculate financing needs using appropriate LC formula
4. **Financing Need Check**: Determine if seller needs financing based on gap calculation
5. **ECR Program Availability**: Check if a government Export Credit Refinancing program is available for this transaction
6. **ECR Program Usage**: If available, determine if client wants to use the program (cheaper cost but with eligibility/paperwork requirements)

## Product Flow Conclusions

- **Sight LC with ECR**: Government-subsidized financing with cheaper rates for immediate payment needs
- **Usance LC with ECR**: Government-subsidized financing with cheaper rates for deferred payment structures
- **Standard Export Bill Path**: Traditional immediate financing under Sight LC
- **Standard Bill Receivable Path**: Traditional financing for Usance LC with immediate cash flow
- **No Financing Path**: Wait for natural payment timing based on LC terms

## New Product Added

### Export Credit Refinancing Post

- **Product Type**: A government-subsidized financing for exporters (Post-shipment timing)
- **How It Works**:
  - Central bank/export agency provides cheap funds to commercial banks
  - Commercial banks pass on cheaper rates to exporters
  - Financing provided after goods are shipped and documents are submitted
  - "Government helps banks so banks help exporters"
- **Use When**:
  - Government export credit program is available
  - Seller wants to expand exports but concerned about financing costs
  - Seller wants to reduce post-shipment financing costs
  - Documents have been submitted and seller needs immediate cash flow
- **Benefits**:
  - Cheaper credit for exporters compared to standard rates
  - Government backing reduces financing costs
  - Supports export expansion and competitiveness
  - Available for both Sight and Usance LC structures
- **Decision Points**:
  - Step 1: Check if government Export Credit Refinancing program is available for the transaction
  - Step 2: If available, check if client wants to use the program despite eligibility and paperwork requirements
