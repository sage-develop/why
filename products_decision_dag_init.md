# Trade Payment Methods - Initial Decision Tree

## Overview

This is the initial decision flow for determining which trade payment method and related services a client needs. It starts with identifying if the client knows their preferred payment method and then routes them to the appropriate specialized decision diagrams.

## Decision Flow

```mermaid
flowchart TD
    Start(["Trade Payment Methods"]) --> Know{"Does client know what<br>payment method to use?"}
    Know -- No --> PaymentDecision["Trade Payment Methods<br>Decision Diagram"]
    Know -- Yes --> Which{"Which payment method<br>does the client want to use?"}
    Which -- Letter of Credit --> LC_Split@{ label: "What is the client's role in transaction?" }
    Which -- Trade Collection --> TC_Split@{ label: "What is the client's role in transaction?" }
    Which -- Open Account --> OA_Split@{ label: "What is the client's role in transaction?" }
    LC_Split -- Seller/Exporter --> LC_Seller_Split{"When does the client need<br>financing/services?"}
    LC_Split -- Buyer/Importer --> LC_Buyer["LC Buyer Decision Diagram"]
    TC_Split -- Seller/Exporter --> TC_Seller_Split{"When does the client need<br>financing/services?"}
    TC_Split -- Buyer/Importer --> TC_Buyer["Trade Collection<br>Buyer Decision Diagram"]
    OA_Split -- Seller/Exporter --> OA_Seller_Split{"When does the client need<br>financing/services?"}
    OA_Split -- Buyer/Importer --> OA_Buyer["Open Account<br>Buyer Decision Diagram"]
    LC_Seller_Split -- "Pre-shipment" --> LC_Seller_Pre["LC Seller Pre-shipment<br>Decision Diagram"]
    LC_Seller_Split -- "Post-shipment" --> LC_Seller_Post["LC Seller Post-shipment<br>Decision Diagram"]
    TC_Seller_Split -- "Pre-shipment" --> TC_Seller_Pre["Trade Collection Seller<br>Pre-shipment Decision Diagram"]
    TC_Seller_Split -- "Post-shipment" --> TC_Seller_Post["Trade Collection Seller<br>Post-shipment Decision Diagram"]
    OA_Seller_Split -- "Pre-shipment" --> OA_Seller_Pre["Open Account Seller<br>Pre-shipment Decision Diagram"]
    OA_Seller_Split -- "Post-shipment" --> OA_Seller_Post["Open Account Seller<br>Post-shipment Decision Diagram"]

    LC_Split@{ shape: diamond}
    TC_Split@{ shape: diamond}
    OA_Split@{ shape: diamond}
     Start:::endpoint
     Know:::decision
     PaymentDecision:::endpoint
     Which:::decision
     LC_Split:::decision
     TC_Split:::decision
     OA_Split:::decision
     LC_Seller_Split:::decision
     LC_Buyer:::endpoint
     TC_Seller_Split:::decision
     TC_Buyer:::endpoint
     OA_Seller_Split:::decision
     OA_Buyer:::endpoint
     LC_Seller_Pre:::endpoint
     LC_Seller_Post:::endpoint
     TC_Seller_Pre:::endpoint
     TC_Seller_Post:::endpoint
     OA_Seller_Pre:::endpoint
     OA_Seller_Post:::endpoint
    classDef default fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
    classDef decision fill:#ffffff,stroke:#666,stroke-width:2px,color:#000
    classDef endpoint fill:#ffffff,stroke:#333,stroke-width:2px,color:#000
```

## Decision Logic

### Primary Flow:

1. **Initial Assessment**: Determine if client has already identified their preferred payment method
2. **Method Selection**: For clients who know their preference, identify the specific payment method
3. **Role Identification**: Establish whether client is a seller/exporter or buyer/importer
4. **Timing Classification**: For sellers, determine if services are needed pre-shipment or post-shipment

### Key Decision Points:

- **Knowledge Assessment**: Whether client understands payment method options
- **Payment Method**: Letter of Credit, Trade Collection, or Open Account
- **Transaction Role**: Seller/Exporter vs Buyer/Importer perspective
- **Service Timing**: Pre-shipment vs Post-shipment service needs (for sellers)

### Routing Logic:

- **Unknown Payment Method**: Routes to comprehensive payment method decision diagram
- **Letter of Credit Buyer**: Routes to full LC buyer decision flow with all financing and service options
- **Seller Services**: Split by timing (pre/post shipment) for more targeted product recommendations
- **Trade Collection & Open Account**: Routes to specialized decision diagrams for each payment method

This initial tree ensures clients are directed to the most relevant detailed decision diagrams based on their role, payment method preference, and timing needs.
