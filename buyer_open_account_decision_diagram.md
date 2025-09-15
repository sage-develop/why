# Buyer Open Account Decision Diagram

## Decision Flow for Buyers Using Open Account Payment Method

```mermaid
flowchart TD
    Start([Buyer is using Open Account payment method])
    Start --> Q1{Can the buyer pay the seller on the due date?}

    Q1 -->|Yes| End1[The buyer continues with standard Open Account terms.<br/>No additional financing products needed.]
    Q1 -->|No| Product1[P/N under Open Account - Buyer]

    Product1 --> End2[The buyer receives pre-shipment financing to meet payment obligations.<br/>This completes the financing solution for Open Account transactions.]

    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    class Product1 productBox
```

## Product Details

### P/N under Open Account - Buyer

- **Type**: Pre-shipment financing for buyers
- **Purpose**: Provides financing when the buyer cannot pay the seller on the due date
- **Application**: Used in Open Account payment arrangements where buyers need working capital support

## Key Decision Point

**Primary Question**: "Can the buyer pay the seller on the due date?"

- This is the critical decision point that determines whether additional financing is needed
- Based on the buyer's cash flow and payment capability assessment
