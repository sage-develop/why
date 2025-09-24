# LC Products Decision Diagram - Buyer (Shipping Guarantee Only)

```mermaid
flowchart TD
    Start@{ label: "Step 3 Manufacturing Buyer LC | cond={'is_buyer':'true', 'is_lc':'true'}" } --> BL_Check@{ label: "Has original B/L arrived at buyer's bank?" }
    BL_Check -- "bl_arrived={'false'}" --> Want_Goods{"Does buyer want to claim goods immediately?"}
    BL_Check -- "bl_arrived={'true'}" --> End_No_SG["No Shipping Guarantee needed - B/L available"]
    Want_Goods -- "claim_goods_immediately={'true'}" --> SG1@{ label: "Shipping Guarantee Issuance | feat={'is_product': 'true'}" }
    Want_Goods -- "claim_goods_immediately={'false'}" --> End_Wait@{ label: "Wait for original B/L to arrive at the buyer's bank" }
    SG1 --> SG_Flow["Buyer claims goods immediately using shipping guarantee"]
    SG_Flow --> BL_Arrive["Wait for original B/L to arrive, then exchange B/L for shipping guarantee"]

    Start@{ shape: stadium}
    BL_Check@{ shape: diamond}
    End_No_SG@{ shape: rect}
    SG1@{ shape: rect}
    End_Wait@{ shape: rect}
    BL_Arrive@{ shape: rect}
     SG1:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
