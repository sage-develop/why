# Seller Post-Shipment Open Account Decision Diagram

```mermaid
flowchart TD
    Start([Seller using Open Account<br/>Post-shipment stage]) --> Q1{Does the seller want<br/>immediate financing instead<br/>of waiting until due date?}

    Q1 -->|Yes| P1[P/N under Open Account]
    Q1 -->|No| End1([Wait for buyer payment<br/>at due date.<br/>No additional products needed.])

    P1 --> End2([Financing complete.<br/>Seller receives immediate funds<br/>and repays when buyer pays.])

    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    class P1 productBox
```

## Decision Points Summary

### 1. Immediate Financing Need

**Question:** Does the seller want immediate financing instead of waiting until due date?

**Decision Criteria:**

- **Yes**: Use P/N under Open Account (Seller) when the seller doesn't want to wait until due date and needs immediate financing
- **No**: Wait for buyer payment at the agreed due date without additional products

## Product Details

### P/N under Open Account (Seller)

- **Type**: Post-shipment financing for sellers
- **Usage**: When the seller doesn't want to wait until due date, they can go to their bank for immediate financing using P/N under Open Account (Seller)
- **Outcome**: Seller receives immediate funds and the transaction flow is complete
