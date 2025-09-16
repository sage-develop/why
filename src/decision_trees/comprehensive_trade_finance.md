flowchart TD
    A[Trade Finance Decision System]
    
    A --> B{Are you a buyer or seller?}
    
    B -->|Seller | attr={"party_role": "seller"}| C{What is your current stage?}
    B -->|Buyer | attr={"party_role": "buyer"}| D{What is your current stage?}
    
    C -->|Pre-shipment | attr={"seller_stage": "pre-shipment"}| E{What type of transaction?}
    C -->|Post-shipment | attr={"seller_stage": "post-shipment"}| F{What type of LC are you using?}
    
    D -->|Pre-shipment | attr={"buyer_stage": "pre-shipment"}| G{What type of transaction?}
    
    E -->|International | attr={"seller_transaction_type": "international"}| H{Do you have counterparty risk concerns?}
    E -->|Domestic | attr={"seller_transaction_type": "domestic"}| I{Do you want to redirect payments?}
    
    G -->|International | attr={"buyer_transaction_type": "international"}| J[Letter of Credit Issuance | attr={"is_product": true}]
    G -->|Domestic | attr={"buyer_transaction_type": "domestic"}| J
    
    H -->|Yes | attr={"has_counterparty_risk": true}| K[Letter of Credit Confirmation | attr={"is_product": true}]
    H -->|No | attr={"has_counterparty_risk": false}| I
    
    K --> I
    
    I -->|Yes | attr={"wants_redirect_payments": true}| L[Assignment of Proceeds under Letter of Credit | attr={"is_product": true}]
    I -->|No | attr={"wants_redirect_payments": false}| M{Are you a middleman?}
    
    L --> M
    
    M -->|Yes | attr={"is_middleman": true}| N{Is the LC transferrable?}
    M -->|No | attr={"is_middleman": false}| O{Do you need pre-shipment working capital?}
    
    N -->|Yes | attr={"lc_is_transferrable": true}| P[Letter of Credit Transferring | attr={"is_product": true}]
    N -->|No | attr={"lc_is_transferrable": false}| O
    
    P --> Q[Middleman flow completed]
    
    O -->|Yes | attr={"needs_preshipment_capital": true}| R[Packing Credit for Exporters | attr={"is_product": true}]
    O -->|No | attr={"needs_preshipment_capital": false}| S[Letter of Credit Advising | attr={"is_product": true}]
    
    R --> S
    S --> T[Pre-shipment completed - Ready for post-shipment]
    
    F -->|Sight LC | attr={"seller_lc_type": "sight"}| U{Do you need immediate financing?}
    F -->|Usance LC | attr={"seller_lc_type": "usance"}| V{Do you need post-shipment financing?}
    
    U -->|Yes | attr={"needs_sight_financing": true}| W[Export Bill under Letter of Credit | attr={"is_product": true}]
    U -->|No | attr={"needs_sight_financing": false}| X[Wait for buyer's bank payment at sight]
    
    V -->|Yes | attr={"needs_usance_financing": true}| Y[Bill Receivable under Letter of Credit | attr={"is_product": true}]
    V -->|No | attr={"needs_usance_financing": false}| Z[Wait for payment at LC maturity]
    
    W --> AA[Transaction completed - Bank advances funds]
    X --> BB[Transaction completed - Direct payment received]
    Y --> CC[Transaction completed - Funds received at maturity]
    Z --> DD[Transaction completed - Payment at maturity]
    
    J --> EE{Has your bank received the original B/L?}
    
    EE -->|No | attr={"bl_received": false}| FF{Do you want to claim goods immediately?}
    EE -->|Yes | attr={"bl_received": true}| GG{What type of LC are you using?}
    
    FF -->|Yes | attr={"wants_immediate_claim": true}| HH[Shipping Guarantee Issuance | attr={"is_product": true}]
    FF -->|No | attr={"wants_immediate_claim": false}| II[Wait for B/L arrival]
    
    HH --> GG
    II --> GG
    
    GG -->|Sight LC | attr={"buyer_lc_type": "sight"}| JJ{Do you need buyer financing?}
    GG -->|Usance LC | attr={"buyer_lc_type": "usance"}| JJ
    
    JJ -->|Yes | attr={"needs_buyer_financing": true}| KK{Who is the B/L issued under?}
    JJ -->|No | attr={"needs_buyer_financing": false}| LL[Complete transaction without financing]
    
    KK -->|Buyer's name | attr={"bl_issued_under": "buyer_name"}| MM[P/N under Letter of Credit (Buyer) | attr={"is_product": true}]
    KK -->|Bank's name | attr={"bl_issued_under": "bank_name"}| NN[Trust Receipt Loan under Letter of Credit | attr={"is_product": true}]
    
    MM --> OO[Transaction completed with P/N financing]
    NN --> PP{Need ownership transfer?}
    
    PP -->|Yes | attr={"needs_ownership_transfer": true}| QQ[Endorsement Services | attr={"is_product": true}]
    PP -->|No | attr={"needs_ownership_transfer": false}| RR[Transaction completed with Trust Receipt]
    
    QQ --> SS[Transaction completed with ownership transfer]
    
    style K fill:#e1f5fe
    style L fill:#e1f5fe
    style P fill:#e1f5fe
    style R fill:#e1f5fe
    style S fill:#e1f5fe
    style W fill:#e1f5fe
    style Y fill:#e1f5fe
    style J fill:#e1f5fe
    style HH fill:#e1f5fe
    style MM fill:#e1f5fe
    style NN fill:#e1f5fe
    style QQ fill:#e1f5fe
