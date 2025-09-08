# Letter of Credit Products - Seller/Exporter Decision Diagram

## Overview

This decision diagram covers all LC-related products offered by the bank specifically for sellers/exporters. It starts with core LC advising services and then branches based on timing requirements (pre-shipment vs post-shipment) and specific business needs.

## Decision Flow

```mermaid
flowchart TD
    A@{ label: "Seller Pre-shipment<br style=\"--tw-scale-x:\">LC Payment Method" } --> B["Letter of Credit Advising"]
    B --> C{"Is this a domestic or<br>international transaction?"}
    C -- Domestic --> D{"Worried about<br>counter party risk?"}
    C -- International --> E{"Worried about counter party<br>sovereign risk?"}
    D -- Yes --> F["Letter of Credit Confirmation"]
    E -- Yes --> F
    D -- No --> G{"Is the seller acting<br>as a middleman?"}
    E -- No --> G
    F --> G
    G -- Yes --> H{"Is the LC transferrable?"}
    G -- No --> I{"Need to redirect payments<br>to third parties?"}
    H -- Yes --> J["Letter of Credit Transferring"]
    H -- No --> K{"Consider Assignment of Proceeds<br>or pay supplier directly?"}
    J --> L["Flow ends here.<br>Middleman has transferred LC responsibility."]
    K -- Assignment of Proceeds --> M["Assignment of Proceeds under Letter of Credit"]
    K -- Pay directly --> N{"Need pre-shipment<br>working capital?"}
    I -- Yes --> M
    I -- No --> N
    M --> N
    N -- Yes --> O["Packing Credit for Exporters"]
    N -- No --> P["Continue to post-shipment<br>products or complete transaction"]
    O --> P

    A@{ shape: rect}
     B:::product
     F:::product
     J:::product
     M:::product
     O:::product
    classDef product fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000s
```

## Product Categories

### Core Service

- **Letter of Credit Advising** - Base LC product for sellers
- **Export Bill under Letter of Credit** - Core post-shipment document service (ALL sellers need this)

### Risk Mitigation Services

- **Letter of Credit Confirmation** - Transfer foreign/cross-border risk to local bank

### Pre-Shipment Services

- **Assignment of Proceeds under Letter of Credit** - Payment redirection only (seller remains responsible for LC terms)
- **Letter of Credit Transferring** - Middleman trading solution (transfers LC obligations)
- **Packing Credit for Exporters** - Pre-shipment working capital

### Post-Shipment Financing

- **Bill Receivable under Letter of Credit** - Seller financing for usance LCs

## Decision Logic

### Primary Decision Points:

1. **Transaction Type** - Domestic vs International (determines risk profile)
2. **Risk Appetite** - Whether to transfer bank/country risk
3. **Timing** - Pre-shipment vs post-shipment needs (key decision point)
4. **Business Model** - Producer vs middleman/trader
5. **Payment Structure** - Payment redirection needs
6. **Financing Needs** - Working capital requirements
7. **Payment Terms** - Sight vs usance LC terms

### Key Considerations:

- **Core products** (Advising and Export Bill) are prerequisites for other services
- **Pre-shipment services** focus on risk mitigation, payment routing, and working capital
- **Post-shipment financing** addresses cash flow gaps after shipment
- **Transferable LC** serves a specific middleman business model
- **Assignment of Proceeds** is a payment routing service, not financing
- **All exporters** will eventually need Export Bill services regardless of other choices

## Flow Logic

The diagram starts with mandatory LC advising services, then branches based on risk appetite and confirmation needs. The key innovation is the clear **Pre-Shipment vs Post-Shipment** decision point that helps structure the conversation and product recommendations based on the client's current business stage and immediate needs.

This separation ensures that relationship managers can:

- Focus discussions on relevant timing-based needs
- Clearly identify whether the client is in planning/production phase (pre-shipment) or has already shipped goods (post-shipment)
- Provide appropriate product recommendations based on the client's current business cycle stage
