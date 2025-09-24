# Trade Collection - Buyer Shipping Guarantee Decision Path

```mermaid
flowchart TD
    A@{ label: "Step 3 Manufacturing Buyer Collection | cond={'is_buyer':'true', 'is_collection':'true'}" } --> B@{ label: "Has the original B/L arrived at buyer's bank?" }
    B -- "No | bl_arrived={'bl_arrived': 'false'}" --> C{"Does buyer want to claim goods immediately?"}
    B -- "Yes | bl_arrived={'bl_arrived': 'true'}" --> D["Continue to step 4"]
    C -- "Yes | immediate_claim={'immediate_claim': 'true'}" --> E["Shipping Guarantee Issuance | feat={'is_product': 'true'}"]
    E --> S["Buyer claims goods immediately with Shipping Guarantee"]

    A@{ shape: stadium}
    B@{ shape: diamond}
    D@{ shape: rect}
    S@{ shape: rect}
     E:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
