flowchart TD
    A[LC Seller Post-shipment Products]
    
    A --> B{What type of LC are you using?}
    
    B -->|Sight LC | attr={"lc_type": "sight"}| C[Calculate financing gap with Sight LC formula]
    B -->|Usance LC | attr={"lc_type": "usance"}| D[Calculate financing gap with Usance LC formula]
    
    C --> E{Do you need financing for immediate payment?}
    D --> F{Do you need financing for post-shipment working capital?}
    
    E -->|Yes | attr={"needs_financing": true}| G[Export Bill under Letter of Credit | attr={"is_product": true}]
    E -->|No | attr={"needs_financing": false}| H[Wait until buyer's bank pays at sight]
    
    F -->|Yes | attr={"needs_financing": true}| I[Bill Receivable under Letter of Credit | attr={"is_product": true}]
    F -->|No | attr={"needs_financing": false}| J[Wait until maturity date for buyer's bank to pay]
    
    G --> K[Bank advances funds once compliant documents are presented - Transaction completed]
    H --> L[Receive payment when buyer's bank pays at sight - Transaction completed]
    I --> M[Transaction completed at LC maturity when buyer's bank pays]
    J --> N[Receive payment at LC maturity - Transaction completed]
    
    style G fill:#e1f5fe
    style I fill:#e1f5fe
