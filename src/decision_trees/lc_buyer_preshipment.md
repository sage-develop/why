flowchart TD
    A[LC Buyer Pre-shipment Products]
    
    A --> B{What type of transaction are you handling?}
    
    B -->|International | attr={"transaction_type": "international"}| C[Letter of Credit Issuance | attr={"is_product": true}]
    B -->|Domestic | attr={"transaction_type": "domestic"}| C
    
    C --> D{Has your bank received the original B/L?}
    
    D -->|No | attr={"bl_received_by_bank": false}| E{Do you want to claim goods immediately?}
    D -->|Yes | attr={"bl_received_by_bank": true}| F{What type of LC are you using?}
    
    E -->|Yes | attr={"wants_immediate_claim": true}| G[Shipping Guarantee Issuance | attr={"is_product": true}]
    E -->|No | attr={"wants_immediate_claim": false}| H[Wait for original B/L to arrive]
    
    G --> I{When B/L arrives, what type of LC are you using?}
    H --> F
    
    F -->|Sight LC | attr={"lc_type_buyer": "sight"}| J[Calculate financing gap with Sight LC formula]
    F -->|Usance LC | attr={"lc_type_buyer": "usance"}| K[Calculate financing gap with Usance LC formula]
    
    I -->|Sight LC | attr={"lc_type_after_guarantee": "sight"}| J
    I -->|Usance LC | attr={"lc_type_after_guarantee": "usance"}| K
    
    J --> L{Do you need financing?}
    K --> L
    
    L -->|Yes | attr={"needs_buyer_financing": true}| M{Who is the original B/L issued under?}
    L -->|No | attr={"needs_buyer_financing": false}| N{Was a Shipping Guarantee used?}
    
    M -->|Buyer's name | attr={"bl_issued_under": "buyer_name"}| O[P/N under Letter of Credit (Buyer) | attr={"is_product": true}]
    M -->|Buyer's bank name | attr={"bl_issued_under": "bank_name"}| P[Trust Receipt Loan under Letter of Credit | attr={"is_product": true}]
    
    N -->|Yes | attr={"shipping_guarantee_used": true}| Q{Who was the Shipping Guarantee issued under?}
    N -->|No | attr={"shipping_guarantee_used": false}| R[Transaction completed - No additional services needed]
    
    O --> S{Was a Shipping Guarantee used?}
    P --> T[Use Endorsement Services to transfer ownership]
    
    S -->|Yes | attr={"guarantee_used_after_pn": true}| U[Exchange B/L for Shipping Guarantee - Transaction completed]
    S -->|No | attr={"guarantee_used_after_pn": false}| V[Transaction completed with P/N financing]
    
    T --> W{Was a Shipping Guarantee used?}
    
    W -->|Yes | attr={"guarantee_used_after_endorsement": true}| X[Exchange B/L for Shipping Guarantee - Transaction completed]
    W -->|No | attr={"guarantee_used_after_endorsement": false}| Y[Transaction completed with Trust Receipt and Endorsement]
    
    Q -->|Buyer's name | attr={"guarantee_issued_under": "buyer_name"}| Z[Use Shipping Guarantee to exchange - Transaction completed]
    Q -->|Buyer's bank name | attr={"guarantee_issued_under": "bank_name"}| AA[Endorsement Services | attr={"is_product": true}]
    
    AA --> AB[Use Shipping Guarantee after endorsement - Transaction completed]
    
    style C fill:#e1f5fe
    style G fill:#e1f5fe
    style O fill:#e1f5fe
    style P fill:#e1f5fe
    style AA fill:#e1f5fe
