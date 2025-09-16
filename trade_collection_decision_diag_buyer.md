# Trade Collection - Buyer Pre-shipment Decision Diagram

```mermaid
flowchart TD
    A@{ label: "<span style=\"color:\">Trade Collection</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Buyer Decision Diagram</span>" } --> B@{ label: "Has the original B/L arrived at buyer's bank?" }
    B -- No --> C{"Does buyer want to claim goods immediately?"}
    B -- Yes --> D["Inward Bill for Collection"]
    C -- Yes --> E["Shipping Guarantee Issuance"]
    C -- No --> F["Continue base flow - wait for B/L arrival"]
    F --> D
    D --> G{"What payment terms is the buyer using: D/P or D/A?"}
    G -- D/P --> H["Calculate financing gap using D/P formula"]
    G -- D/A --> I["Calculate financing gap using D/A formula"]
    H --> J{"Does buyer need financing based on gap calculation?"}
    I --> J
    J -- Yes --> K["P/N under Bill for Collection - Buyer"]
    J -- No --> L["Proceed without financing"]
    K --> M{"Who has title to the goods on the B/L?"}
    L --> M
    M -- The buyer --> N["Use B/L directly to claim goods"]
    M -- The bank --> O["Endorsement Services"]
    O --> P{"Was Shipping Guarantee Issuance used earlier?"}
    N --> P
    P -- Yes --> Q["Exchange B/L for Shipping Guarantee to complete flow"]
    P -- No --> R["Trade Collection transaction completed successfully"]
    E --> S["Buyer claims goods immediately with Shipping Guarantee"]
    S --> T["Wait for original B/L arrival and continue base flow"]
    T --> D
    Q --> R

    A@{ shape: rect}
    B@{ shape: diamond}
    style D fill:#e1f5fe
    style E fill:#e1f5fe
    style K fill:#e1f5fe
    style O fill:#e1f5fe
```

## Decision Points Summary

1. **B/L Arrival Status**: Determines if buyer can proceed with standard collection or needs shipping guarantee
2. **Immediate Goods Claim**: When B/L hasn't arrived, decides if urgent goods access is needed
3. **Payment Terms**: D/P (Documents against Payment) vs D/A (Documents against Acceptance) affects financing calculations
4. **Financing Need**: Based on calculated financing gap using appropriate formula
5. **B/L Ownership**: Determines if endorsement services are required
6. **Shipping Guarantee Usage**: Affects final completion steps

## Flow Conclusion

The Trade Collection buyer pre-shipment flow concludes when the buyer successfully receives the goods and completes payment obligations according to the agreed terms (D/P or D/A), with all necessary document exchanges completed.
