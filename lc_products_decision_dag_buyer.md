# Letter of Credit Products Decision Diagram - Buyer Pre-shipment

This decision diagram shows the flow for buyers in pre-shipment stage when using Letter of Credit payment method.

## Decision Flow

```mermaid
flowchart TD
    START([Buyer using LC Payment Method]) --> LC[Letter of Credit Issuance]

    LC --> BL_STATUS{Has B/L arrived at<br/>buyer's bank?}

    BL_STATUS -->|No, but buyer needs goods immediately| SG[Shipping Guarantee Issuance]
    BL_STATUS -->|Yes| BL_NAME{Under whose name<br/>is B/L issued?}

    SG --> SG_GOODS[Buyer claims goods immediately<br/>using Shipping Guarantee]
    SG_GOODS --> WAIT_BL[Wait for original B/L to arrive]
    WAIT_BL --> BL_NAME

    BL_NAME -->|Buyer's name| LC_TYPE_BUYER{LC Type:<br/>Sight LC or Usance LC?}
    BL_NAME -->|Buyer's bank name| LC_TYPE_BANK{LC Type:<br/>Sight LC or Usance LC?}

    LC_TYPE_BUYER -->|Sight LC| CALC_SIGHT_BUYER[Calculate financing gap<br/>using Sight LC formula]
    LC_TYPE_BUYER -->|Usance LC| CALC_USANCE_BUYER[Calculate financing gap<br/>using Usance LC formula]

    CALC_SIGHT_BUYER --> NEED_FINANCE_BUYER{Does buyer need<br/>financing?}
    CALC_USANCE_BUYER --> NEED_FINANCE_BUYER

    NEED_FINANCE_BUYER -->|Yes| PN[P/N under Letter of Credit]
    NEED_FINANCE_BUYER -->|No| CHECK_SG_BUYER{Was Shipping Guarantee<br/>Issuance used?}

    PN --> CHECK_SG_PN{Was Shipping Guarantee<br/>Issuance used?}

    CHECK_SG_PN -->|Yes| EXCHANGE_PN[Exchange B/L for<br/>Shipping Guarantee]
    CHECK_SG_PN -->|No| END_PN[Trade finance flow completed.<br/>Buyer can proceed with goods clearance.]

    CHECK_SG_BUYER -->|Yes| EXCHANGE_BUYER[Exchange B/L for<br/>Shipping Guarantee]
    CHECK_SG_BUYER -->|No| END_BUYER[Trade finance flow completed.<br/>Buyer can proceed with goods clearance.]

    LC_TYPE_BANK -->|Sight LC| CALC_SIGHT_BANK[Calculate financing gap<br/>using Sight LC formula]
    LC_TYPE_BANK -->|Usance LC| CALC_USANCE_BANK[Calculate financing gap<br/>using Usance LC formula]

    CALC_SIGHT_BANK --> NEED_FINANCE_BANK{Does buyer need<br/>financing?}
    CALC_USANCE_BANK --> NEED_FINANCE_BANK

    NEED_FINANCE_BANK -->|Yes| TR[Trust Receipt Loan under Letter of Credit]
    NEED_FINANCE_BANK -->|No| ES[Endorsement Services]

    TR --> ES_AFTER_TR[Endorsement Services]

    ES --> CHECK_SG_ES{Was Shipping Guarantee<br/>Issuance used?}
    ES_AFTER_TR --> CHECK_SG_TR{Was Shipping Guarantee<br/>Issuance used?}

    CHECK_SG_ES -->|Yes| EXCHANGE_ES[Exchange B/L for<br/>Shipping Guarantee]
    CHECK_SG_ES -->|No| END_ES[Trade finance flow completed.<br/>Buyer has ownership and can proceed with goods clearance.]

    CHECK_SG_TR -->|Yes| EXCHANGE_TR[Exchange B/L for<br/>Shipping Guarantee]
    CHECK_SG_TR -->|No| END_TR[Trade finance flow completed.<br/>Buyer has ownership and can proceed with goods clearance.]

    EXCHANGE_PN --> END_EXCHANGE_PN[Trade finance flow completed.<br/>Goods delivered and Shipping Guarantee settled.]
    EXCHANGE_BUYER --> END_EXCHANGE_BUYER[Trade finance flow completed.<br/>Goods delivered and Shipping Guarantee settled.]
    EXCHANGE_ES --> END_EXCHANGE_ES[Trade finance flow completed.<br/>Goods delivered, ownership transferred, and Shipping Guarantee settled.]
    EXCHANGE_TR --> END_EXCHANGE_TR[Trade finance flow completed.<br/>Goods delivered, ownership transferred, and Shipping Guarantee settled.]

    classDef product fill:#e1f5fe
    class LC,SG,PN,TR,ES,ES_AFTER_TR product
```

## Products Covered

### Mandatory Products

- **Letter of Credit Issuance**: Base LC product mandatory when buyer and seller agree to use LC payment method

### Optional Products Based on Situation

- **Shipping Guarantee Issuance**: When buyer's bank hasn't received original B/L but buyer needs goods immediately
- **P/N under Letter of Credit (Buyer)**: Financing when B/L is at buyer's bank and issued under buyer's name
- **Trust Receipt Loan under Letter of Credit**: Financing when B/L is at buyer's bank and issued under buyer's bank's name
- **Endorsement Services**: Required when B/L is issued under buyer's bank's name to transfer ownership to buyer

## Key Decision Points

1. **B/L Receipt**: Whether buyer's bank has received the original Bill of Lading
2. **B/L Ownership**: Under whose name the B/L is issued (buyer vs buyer's bank)
3. **LC Type**: Whether using Sight LC or Usance LC for financing calculations
4. **Financing Need**: Based on financing gap calculation results
5. **Shipping Guarantee Usage**: Whether Shipping Guarantee Issuance was used earlier in the flow

## Flow Conclusions

The diagram shows multiple ending scenarios:

- **Simple completion**: When no additional financing or services are needed
- **Exchange completion**: When Shipping Guarantee was used and needs to be exchanged with B/L
- All flows conclude with either completing the trade finance process or proceeding with trade settlement
