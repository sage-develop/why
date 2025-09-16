# Seller Post-Shipment Open Account Decision Diagram - Enhanced

```mermaid
flowchart TD
    Start@{ label: "<span style=\"color:\">Open Account Seller</span><br style=\"--tw-scale-x:\"><span style=\"color:\">Post-shipment Decision Diagram</span>" } --> Q1{"Does seller need immediate financing<br>instead of waiting until<br>the payment due date?"}
    Q1 -- Yes --> Q2@{ label: "Is the seller comfortable taking<br>the risk if this buyer<br>doesn't pay, or<br>prefer the bank to take that risk?" }
    Q1 -- No --> Q3{"Does the seller want to help<br>the buyers/distributors<br>with financing to strengthen<br>business relationships?"}
    Q2 -- Comfortable with the risk --> Q4{"Does seller want to sell<br>invoice to the bank for immediate cash,<br>or get financing against it?"}
    Q2 -- Prefer the bank takes the risk --> P4["NRF - Non-Recourse Financing"]
    Q4 -- Sell the invoice for cash --> P2["CBP - Clean Bill Purchased"]
    Q4 -- Get financing against it --> Q5@{ label: "Does seller want the bank's standard<br>financing option?" }
    Q5 -- Yes, keep it simple --> P1["P/N under Open Account"]
    Q5 -- Wants more flexible terms --> P3["DRF - Direct Recourse Financing"]
    Q3 -- Yes --> P5["Distributor Financing"]
    Q3 -- No --> End1(["Wait for buyer payment<br>at due date.<br>No additional products needed."])
    P1 --> End2(["Standard financing complete.<br>The seller receives immediate funds<br>and repay when buyer pays."])
    P2 --> End3@{ label: "The bank buys seller's invoice.<br>The seller get instant cash.<br>The bank collect from the buyer." }
    P3 --> End4@{ label: "The bank advance funds to the seller.<br>If buyer doesn't pay,<br>the seller refund the bank with flexible terms." }
    P4 --> End5@{ label: "The bank finance seller's receivables<br>and assume all buyer risk.<br>The seller have no liability." }
    P5 --> End6(["Seller arranges the program.<br>The buyers get financing<br>to strengthen partnerships."])

    Start@{ shape: stadium}
    Q2@{ shape: diamond}
    Q5@{ shape: diamond}
    End3@{ shape: stadium}
    End4@{ shape: stadium}
    End5@{ shape: stadium}
     P4:::newProductBox
     P2:::newProductBox
     P1:::productBox
     P3:::newProductBox
     P5:::newProductBox
     Q2:::newDecisionBox
     Q3:::newDecisionBox
     Q4:::newDecisionBox
     Q5:::newDecisionBox
     End3:::newEndBox
     End4:::newEndBox
     End5:::newEndBox
     End6:::newEndBox
    classDef productBox fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    classDef newProductBox fill:#ffebee,stroke:#c62828,stroke-width:2px,color:#c62828
    classDef newDecisionBox fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#d81b60
    classDef newEndBox fill:#fce4ec,stroke:#d81b60,stroke-width:2px,color:#c62828
```

## Decision Points Summary

### 1. Immediate Financing Need

**Question:** "Do you need immediate financing instead of waiting until the payment due date?"

**Decision Criteria:**

- **Yes**: Proceed to assess risk appetite and financing preferences
- **No**: Consider helping downstream partners or wait for payment

### 2. Risk Appetite Assessment

**Question:** "Are you comfortable taking the risk if this buyer doesn't pay, or would you prefer us to take that risk?"

**Decision Criteria:**

- **Comfortable with risk**: Explore P/N, CBP, or DRF options
- **Prefer bank takes risk**: Use NRF - Non-Recourse Financing

### 3. Transaction Structure Preference

**Question:** "Would you prefer to sell us your invoice for immediate cash, or get financing against it?"

**Decision Criteria:**

- **Sell invoice for cash**: Use CBP - Clean Bill Purchased
- **Get financing against it**: Choose between P/N or DRF

### 4. Financing Complexity Preference

**Question:** "Do you want our standard financing option?"

**Decision Criteria:**

- **Yes, keep it simple**: Use P/N under Open Account
- **Want more flexible terms**: Use DRF - Direct Recourse Financing

### 5. Downstream Partner Support

**Question:** "Would you like to help your buyers/distributors with financing to strengthen your business relationships?"

**Decision Criteria:**

- **Yes**: Use Distributor Financing
- **No**: Simply wait for payment at due date

## Product Details

### P/N under Open Account (Seller)

- **Type**: Post-shipment financing for sellers
- **Usage**: When the seller doesn't want to wait until due date, they can go to their bank for immediate financing using P/N under Open Account (Seller)
- **Outcome**: Seller receives immediate funds and the transaction flow is complete

### CBP - Clean Bill Purchased _(NEW)_

- **Type**: Post-shipment financing for sellers
- **Usage**: Seller ships goods → Creates payment bill → Bank buys bill for cash, giving the seller instant money → Bank collects from buyer later
- **Key Feature**: Seller sells their bill (IOU) to the bank for instant money
- **Risk**: Bank purchases bills without documents of title to goods attached

### DRF - Direct Recourse Financing _(NEW)_

- **Type**: Post-shipment financing for sellers
- **Usage**: Bank gives the seller money in advance, but if the buyer doesn't pay, the seller must refund the bank
- **Key Feature**: Get the money now but if the buyer doesn't pay, the risk returns to the seller
- **Risk**: Seller retains ultimate responsibility for buyer default

### NRF - Non-Recourse Financing _(NEW)_

- **Type**: Post-shipment financing for sellers
- **Usage**: Bank finances receivables and assumes the risk of buyer default (exporter has no liability)
- **Key Feature**: Bank buys your future payment and takes buyer risk
- **Best For**: "We want immediate cash from our receivables but don't want to worry about buyer default"

### Distributor Financing _(NEW)_

- **Type**: Financing program for sellers to help their buyers
- **Usage**: Sellers arrange the program, buyers receive the financing
- **Key Questions**: "Do your buyers (who buy from you for resale) need financing?"
- **Purpose**: Help downstream partners (buyers/distributors) and strengthen business relationships
