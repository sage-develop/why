flowchart TD
    A[Seller Post-shipment<br/>LC Payment Method] --> B{What type of LC<br/>are you using?}

    B -->|Sight LC | C[Calculate financing gap<br/>with Sight LC formula | attr=is_sight_lc]
    B -->|Usance LC | D[Calculate financing gap<br/>with Usance LC formula | attr=is_usance_lc]

    C --> E{Do you need<br/>financing? | attr=needs_financing}
    D --> F{Do you need<br/>financing? | attr=needs_financing}

    E -->|Yes | G[Export Bill under Letter of Credit | attr=use_export_bill]
    E -->|No | H[Wait until buyer's bank<br/>pays at sight | attr=wait_for_sight_payment]

    F -->|Yes | I[Bill Receivable under Letter of Credit | attr=use_bill_receivable]
    F -->|No | J[Wait until maturity date<br/>for buyer's bank to pay | attr=wait_for_usance_payment]

    G --> K[Transaction completed | attr=transaction_completed]
    H --> L[Transaction completed | attr=transaction_completed]
    I --> M[Transaction completed<br/>at LC maturity when<br/>buyer's bank pays | attr=transaction_completed]
    J --> N[Transaction completed<br/>at LC maturity when<br/>buyer's bank pays | attr=transaction_completed]

    style G fill:#e1f5fe
    style I fill:#e1f5fe