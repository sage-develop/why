flowchart TD
    A[Seller Pre-shipment LC Payment Method]
    
    A --> B[Letter of Credit Advising | attr={"is_product": true}]
    
    B --> C{Worried about counterparty risk or counterparty sovereign risk?}
    
    C -->|Yes | attr={"worried_about_counterparty_risk": true}| D[Letter of Credit Confirmation | attr={"is_product": true}]
    C -->|No | attr={"worried_about_counterparty_risk": false}| E{Is seller a middleman who doesn't make goods?}
    
    D --> E
    
    E -->|Yes | attr={"is_middleman": true}| F{Is LC transferable?}
    E -->|No | attr={"is_middleman": false}| G{Want to redirect payments to third parties?}
    
    F -->|Yes | attr={"lc_is_transferable": true}| H{Want to transfer LC to supplier?}
    F -->|No | attr={"lc_is_transferable": false}| G
    
    H -->|Yes | attr={"wants_to_transfer_lc": true}| I[Letter of Credit Transferring | attr={"is_product": true}]
    H -->|No | attr={"wants_to_transfer_lc": false}| G
    
    I --> J[Flow ends here - Middleman transferred LC]
    
    G -->|Yes | attr={"wants_to_assign_proceeds": true}| K[Assignment of Proceeds under Letter of Credit | attr={"is_product": true}]
    G -->|No | attr={"wants_to_assign_proceeds": false}| L{Need pre-shipment working capital?}
    
    K --> L
    
    L -->|Yes | attr={"needs_preshipment_working_capital": true}| M[Packing Credit for Exporters | attr={"is_product": true}]
    L -->|No | attr={"needs_preshipment_working_capital": false}| N[Continue to post-shipment products or complete transaction]
    
    M --> N
    
    style B fill:#e1f5fe
    style D fill:#e1f5fe
    style I fill:#e1f5fe
    style K fill:#e1f5fe
    style M fill:#e1f5fe
