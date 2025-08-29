# Letter of Credit Products - Comprehensive Decision Diagram

## Overview

This decision diagram covers all LC-related products offered by the bank, organized by decision order and complexity. Core LC services (issuance for buyers, advising for sellers) are automatic prerequisites. The diagram then branches based on specific business needs and timing requirements.

## Decision Flow

```mermaid
flowchart TD
    A[Client Needs LC Services] --> B{What is the client's role?}

    B -->|Buyer/Importer| C[Buyer LC Services]
    B -->|Seller/Exporter| D[Seller LC Services]

    %% Buyer Services Branch
    C --> C2[Letter of Credit Issuance/Amendment]
    C2 --> C2a{Goods at Carrier, B/L Issued to Seller?}
    C2a -->|Yes| C2b{Who Has Title to Goods?}
    C2b -->|Bank Has Title via B/L| C2b1{What is Buyer's Need?}
    C2b1 -->|Access to Goods Now, Will Repay Later| C4[Trust Receipt Loan under Letter of Credit]
    C2b1 -->|No Financing Needed| C4a[Direct Settlement]
    C2b -->|Buyer Has Title via B/L| C2b2{What is Buyer's Need?}
    C2b2 -->|Funds to Pay Bank and Obtain Documents| C5[P/N under Letter of Credit Buyer]
    C2b2 -->|No Financing Needed| C5a[Direct Settlement]
    C2a -->|No| C2c[Wait for Goods to Reach Carrier and B/L to be Issued]
    C2c --> C2a

    %% Seller Services Branch
    D --> D2[Letter of Credit Advising/Amendment Advising]
    D2 --> D2a{Domestic or International Transaction?}
    D2a -->|International| D2a1{Want to Transfer Foreign Risk to Local Bank?}
    D2a -->|Domestic| D2a2{Want to Transfer Buyer's Bank Risk to Own Bank?}
    D2a1 -->|Yes, Don't Want Cross-Border Risk| D4[Letter of Credit Confirmation]
    D2a1 -->|No, Accept Foreign Risk| D2b{Does Seller Produce Goods or Act as Middleman?}
    D2a2 -->|Yes, Don't Trust Buyer's Bank| D4
    D2a2 -->|No, Trust Buyer's Bank| D2b
    D4 --> D2b
    D2b -->|Produces Own Goods| D2b1{Need Payment Redirection?}
    D2b1 -->|Yes| D2b2{What Type of Payment Redirection?}
    D2b2 -->|Repay Bank Directly / Pay Third Party Supplier / Simplify Payment Routing| D5[Assignment of Proceeds under Letter of Credit]
    D2b1 -->|No| D3{Pre-Shipment Financing Needed?}
    D5 --> D3
    D2b -->|Acts as Middleman| D2b3{Want to Transfer LC to Supplier?}
    D2b3 -->|Yes| D2b4{Is LC Transferable?}
    D2b4 -->|Yes, LC is Transferable| D6[Letter of Credit Transferring]
    D2b4 -->|No, LC Not Transferable| D2b1{Need Payment Redirection?}
    D2b3 -->|No| D2b1{Need Payment Redirection?}

    D3 -->|Yes| D3a{Need Working Capital for Raw Materials/Production/Packaging/Shipment?}
    D3a -->|Yes| D7[Packing Credit for Exporters]
    D7 --> D2d{Post-Shipment Services/Loans?}
    D3 -->|No| D2d{Post-Shipment Services/Loans?}

    D2d -->|Yes| D8{Payment Terms?}
    D8 -->|Sight LC| D9[Export Bill under Letter of Credit]
    D8 -->|Usance LC| D10[Export Bill under Letter of Credit]
    D10 --> D8b{Need Working Capital Before Maturity?}
    D8b -->|Yes| D10a[Bill Receivable under Letter of Credit]
    D8b -->|No| D10b[Wait for Maturity Payment]

    %% Styling
    classDef coreProduct fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    classDef financing fill:#f3e5f5,stroke:#4a148c,stroke-width:2px
    classDef service fill:#e8f5e8,stroke:#1b5e20,stroke-width:2px

    class C2,D2,D9,D10,C4,C5,D7,D10a,D4,D5,D6 coreProduct
```

## Product Categories

### Buyer Products

#### Core Service

- **Letter of Credit Issuance/Amendment** - Base LC product for buyers

#### Post-Shipment Financing

- **Trust Receipt Loan under Letter of Credit** - Buyer financing when bank has title to goods
- **P/N under Letter of Credit Buyer** - Buyer financing when buyer has title to goods

### Seller Products

#### Core Service

- **Letter of Credit Advising/Amendment Advising** - Base LC product for sellers
- **Export Bill under Letter of Credit** - Core post-shipment document service (ALL sellers need this)

#### Pre-Shipment Services

- **Letter of Credit Confirmation** - Transfer foreign/cross-border risk to local bank
- **Assignment of Proceeds under Letter of Credit** - Payment redirection only (seller remains responsible for LC terms)
- **Letter of Credit Transferring** - Middleman trading solution (transfers LC obligations)
- **Packing Credit for Exporters** - Pre-shipment working capital

#### Post-Shipment Financing

- **Bill Receivable under Letter of Credit** - Seller financing for usance LCs

## Decision Logic

### Primary Decision Points:

- **Client Role** - Buyer, Seller, or Trading Company
- **Core LC Need** - Whether basic LC services are required
- **Timing** - Pre-shipment vs. post-shipment needs
- **Risk Profile** - Need for additional guarantees
- **Cash Flow** - Financing requirements and timing
- **Goods Ownership** - Who controls the goods at arrival

### Key Considerations:

- **Core products** are prerequisites for other services
- **Pre-shipment services** focus on risk mitigation and working capital
- **Post-shipment financing** addresses cash flow gaps after shipment
- **Transferable LC** serves a specific middleman business model
- **Assignment of Proceeds** is a payment routing service, not financing

This decision tree ensures clients receive the appropriate combination of LC services based on their role, timing needs, and risk tolerance.
