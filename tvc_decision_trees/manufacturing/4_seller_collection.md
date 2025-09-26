# Trade Collection - Seller Decision Diagram (Manufacturing Scenario 4)

```mermaid
flowchart TD
    Start(["Step 4 Manufacturing Seller Collection | cond={'is_seller':'true', 'is_collection':'true'}"]) --> Q1{"Need pre-shipment financing?"}
    Q1 -->|"Yes | feat={needs_preshipment_financing: true}"| Q2{"Does the seller want government-subsidized<br>financing with cheaper rates?"}
    Q1 -->|"No | feat={needs_preshipment_financing: false}"| Q3{"Need financing in foreign currency<br>with no FX conversion risk?"}
    Q2 -->|"Yes | feat={wants_gov_subsidized: true}"| P1["Export Credit Refinancing Pre Ship | feat={is_product: true}"]
    Q2 -->|"No | feat={wants_gov_subsidized: false}"| P2["Packing Credit | feat={is_product: true}"]
    Q3 -->|"Yes | feat={needs_fx_financing: true}"| P3["Onshore Foreign Currency Loan | feat={is_product: true}"]
    Q3 -->|"No | feat={needs_fx_financing: false}"| End1["No additional products needed"]
    P2 --> End2["Continue to other financing options?"]
    P1 --> End2
    P3 --> End3["Continue to step 5"]
    End2 -->|"Yes | feat={continue_financing_options: true}"| Q3
    End2 -->|"No | feat={continue_financing_options: false}"| End3

    End1@{ shape: rect}
    End2@{ shape: rect}
    End3@{ shape: rect}
     P1:::productBox
     P2:::productBox
     P3:::productBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```
