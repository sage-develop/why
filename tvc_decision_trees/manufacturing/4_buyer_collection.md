# Trade Collection - Buyer Decision Diagram (Simplified)

```mermaid
flowchart TD
    A(["Step 4 Manufacturing Buyer Collection | cond={'is_buyer':'true', 'is_collection':'true'}"]) --> B@{ label: "Has the original B/L arrived at buyer's bank?" }
    B -- "Yes<br/>feat={'bl_arrived': 'true'}" --> C["Inward Bill for Collection<br/>feat={'is_product': 'true'}"]
    B -- "No<br/>feat={'bl_arrived': 'false'}" --> M["Continue to step 5"]
    C --> D{"What payment terms is the buyer using: D/P or D/A?"}
    D -- "D/P<br/>feat={'payment_terms': 'dp'}" --> E["Calculate financing gap using D/P formula"]
    D -- "D/A<br/>feat={'payment_terms': 'da'}" --> F["Calculate financing gap using D/A formula"]
    E --> G{"Does buyer need financing based on gap calculation?"}
    F --> G
    G -- "Yes<br/>feat={'needs_financing': 'true'}" --> H["P/N under Bill for Collection - Buyer<br/>feat={'is_product': 'true'}"]
    G -- "No<br/>feat={'needs_financing': 'false'}" --> I["Proceed without financing"]
    H --> J{"Does buyer need additional foreign currency financing?"}
    I --> J
    J -- "Yes<br/>feat={'needs_fx_financing': 'true'}" --> K["Onshore Foreign Currency Loan<br/>feat={'is_product': 'true'}"]
    J -- "No<br/>feat={'needs_fx_financing': 'false'}" --> L["Proceed without additional foreign currency financing"]
    K --> M
    L --> M

    B@{ shape: diamond}
    D@{ shape: diamond}
    G@{ shape: diamond}
    J@{ shape: diamond}
    M@{ shape: rect}
    E@{ shape: rect}
    F@{ shape: rect}
    I@{ shape: rect}
    L@{ shape: rect}
    C:::productBox
    H:::productBox
    K:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
```
