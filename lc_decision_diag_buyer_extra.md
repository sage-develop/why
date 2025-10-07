# LC Products Decision Diagram - Buyer Pre-shipment

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">LC Buyer Decision Diagram</span>" } --> LC1["Letter of Credit Issuance"]
    LC1 --> BL_Check@{ label: "Has original B/L arrived at buyer's bank?" }
    BL_Check -- No --> Want_Goods{"Does buyer want to claim goods immediately?"}
    BL_Check -- Yes --> LC_Type{"Using Sight LC or Usance LC?"}
    Want_Goods -- Yes --> SG1["Shipping Guarantee Issuance"]
    Want_Goods -- No --> Wait@{ label: "Wait for original B/L to arrive at the buyer's bank" }
    Wait --> LC_Type
    SG1 --> SG_Flow["Buyer claims goods immediately using shipping guarantee"]
    SG_Flow --> BL_Arrive@{ label: "Wait for original B/L to arrive at the buyer's bank" }
    BL_Arrive --> LC_Type
    LC_Type -- Sight LC --> Calc_Sight["Calculate financing gap using Sight LC formula"]
    LC_Type -- Usance LC --> Calc_Usance["Calculate financing gap using Usance LC formula"]
    Calc_Sight --> Need_Finance{"Does buyer need financing based on gap calculation?"}
    Calc_Usance --> Need_Finance
    Need_Finance -- No --> No_Finance_End["Wait for LC payment at maturity - no additional products needed"]
    Need_Finance -- Yes --> Finance_Type{"What type of financing does buyer prefer?"}
    Finance_Type -- Traditional --> BL_Name{"Who has title to the goods on the B/L?"}
    Finance_Type -- Invoice-based --> Has_Invoices{"Does buyer have outstanding invoices/receivables?"}
    BL_Name -- The buyer --> PN1["P/N under Letter of Credit"]
    BL_Name -- The bank --> TR1["Trust Receipt Loan under Letter of Credit"]
    Has_Invoices -- Yes --> IF1["Invoice Financing"]
    Has_Invoices -- No --> BL_Name
    PN1 --> SG_Check1{"Was Shipping Guarantee Issuance used?"}
    TR1 --> Endorse1["Endorsement Services"]
    Endorse1 --> SG_Check2{"Was Shipping Guarantee Issuance used?"}
    SG_Check1 -- Yes --> Exchange1["Exchange B/L for shipping guarantee to complete the flow"]
    SG_Check1 -- No --> PN_Complete["P/N financing completed - buyer can proceed with trade"]
    SG_Check2 -- Yes --> Exchange2["Exchange B/L for shipping guarantee to complete the flow"]
    SG_Check2 -- No --> TR_Complete["Trust receipt and endorsement completed - buyer can proceed with trade"]
    IF1 --> SG_Check3{"Was Shipping Guarantee Issuance used?"}
    SG_Check3 -- Yes --> Exchange3["Exchange B/L for shipping guarantee to complete the flow"]
    SG_Check3 -- No --> IF_Complete["Invoice financing completed - buyer can proceed with trade"]

    Start@{ shape: stadium}
    BL_Check@{ shape: diamond}
    Wait@{ shape: rect}
    BL_Arrive@{ shape: rect}
     LC1:::productBox
     SG1:::productBox
     PN1:::productBox
     TR1:::productBox
     Endorse1:::productBox
     IF1:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```

## Decision Points Summary

1. **Start**: Buyer is already using LC payment method (mandatory Letter of Credit Issuance)
2. **B/L Arrival**: Check if original B/L has arrived at buyer's bank
3. **Immediate Goods**: If no B/L, does buyer want to claim goods immediately?
4. **LC Type**: Determine if using Sight LC or Usance LC
5. **Financing Need**: Calculate financing gap and determine if financing is needed
6. **Financing Type**: Choose between traditional financing (based on goods/B/L) or invoice-based financing
7. **Invoice Availability**: For invoice-based financing, check if buyer has outstanding invoices/receivables
8. **B/L Issuer**: For traditional financing, check if B/L is issued under buyer's name or buyer's bank's name
9. **Shipping Guarantee**: Check if Shipping Guarantee Issuance was used to determine final steps

## Product Flow Conclusions

- **No Financing Path**: Wait for payment completion - no additional products needed
- **P/N Path**: P/N financing completed - buyer can proceed with trade (with potential B/L exchange if shipping guarantee used)
- **Trust Receipt Path**: Trust receipt and endorsement completed - buyer can proceed with trade (with potential B/L exchange if shipping guarantee used)
- **Invoice Financing Path**: Invoice financing completed - buyer can proceed with trade (with potential B/L exchange if shipping guarantee used)
- **Shipping Guarantee Path**: All paths that used shipping guarantee require exchanging B/L for the shipping guarantee to complete the flow

## Invoice Financing Decision Points

**When to offer Invoice Financing:**

- Buyer needs financing but prefers to use their outstanding invoices/receivables as collateral
- Buyer has strong receivables portfolio that can support financing needs
- Buyer wants to solve cash flow issues through invoice-based mechanisms rather than traditional goods-based financing
- Applicable for buyers who have diversified business operations with substantial accounts receivable

**Invoice Financing Benefits:**

- Solves cash flow issues for buyers by leveraging their existing receivables
- Provides alternative financing mechanism not dependent on goods title or B/L ownership
- Can be faster to process as it's based on existing invoices rather than waiting for goods documentation
- Suitable for buyers with strong customer payment history and diversified receivables portfolio
