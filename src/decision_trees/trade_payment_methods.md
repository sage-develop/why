flowchart TD
    Start([Trade Payment Methods]) --> Know{"Does client know what<br>payment method to use?"}

    Know -->|No| PaymentDecision[Trade Payment Methods<br>Decision Diagram]
    Know -->|Yes| Which{"Which payment method<br>does the client want to use?"}

    Which -->|Letter of Credit| LC_Split{What is the client's role in transaction?}
    Which -->|Trade Collection| TC_Split{What is the client's role in transaction?}
    Which -->|Open Account| OA_Split{What is the client's role in transaction?}

    LC_Split -->|Seller/Exporter| LC_Seller_Split{When does the client need<br>financing/services?}
    LC_Split -->|Buyer/Importer| LC_Buyer[Full LC Buyer Decision Diagram]

    TC_Split -->|Seller/Exporter| TC_Seller_Split{When does the client need<br>financing/services?}
    TC_Split -->|Buyer/Importer| TC_Buyer[Full Trade Collection<br>Buyer Decision Diagram]

    OA_Split -->|Seller/Exporter| OA_Seller_Split{When does the client need<br>financing/services?}
    OA_Split -->|Buyer/Importer| OA_Buyer[Full Open Account<br>Buyer Decision Diagram]

    LC_Seller_Split -->|Pre-shipment| LC_Seller_Pre[LC Seller Pre-shipment<br>Decision Diagram]
    LC_Seller_Split -->|Post-shipment| LC_Seller_Post[LC Seller Post-shipment<br>Decision Diagram]

    TC_Seller_Split -->|Pre-shipment| TC_Seller_Pre[Trade Collection Seller<br>Pre-shipment Decision Diagram]
    TC_Seller_Split -->|Post-shipment| TC_Seller_Post[Trade Collection Seller<br>Post-shipment Decision Diagram]

    OA_Seller_Split -->|Pre-shipment| OA_Seller_Pre[Open Account Seller<br>Pre-shipment Decision Diagram]
    OA_Seller_Split -->|Post-shipment| OA_Seller_Post[Open Account Seller<br>Post-shipment Decision Diagram]

    %% Styling for white boxes
    classDef default fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    classDef decision fill:#ffffff,stroke:#666,stroke-width:2px,color:#000
    classDef endpoint fill:#ffffff,stroke:#333,stroke-width:2px,color:#000

    class Start,PaymentDecision,LC_Buyer,TC_Buyer,OA_Buyer,LC_Seller_Pre,LC_Seller_Post,TC_Seller_Pre,TC_Seller_Post,OA_Seller_Pre,OA_Seller_Post endpoint
    class Know,Which,LC_Split,TC_Split,OA_Split,LC_Seller_Split,TC_Seller_Split,OA_Seller_Split decision