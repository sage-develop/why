# Letter of Credit Products - Buyer/Importer Decision Diagram

## Overview

This decision diagram covers all LC-related products offered by the bank specifically for buyers/importers. It starts with core LC issuance services and then branches based on shipment status, document availability, title ownership, and financing requirements.

## Decision Flow

```mermaid
flowchart TD
    Start(["Buyer LC Payment Method"]) --> Pre["Pre-shipment"]
    Pre --> LC_Issuance["Letter of Credit Issuance"]
    LC_Issuance --> BL_Arrived@{ label: "Has the original B/L<br>arrived at buyer's bank?" }
    BL_Arrived -- No --> Shipping_Guarantee["Shipping Guarantee Issuance"]
    Shipping_Guarantee --> Claim_Goods["Buyer claims goods immediately"]
    Claim_Goods --> BL_Wait["Wait for original B/L to arrive"]
    BL_Wait --> BL_Name_Check{"In whose name is<br>the B/L issued?"}
    BL_Arrived -- Yes --> BL_Name_Check
    BL_Name_Check -- Buyer's name --> LC_Type_PN{"LC type:<br>Sight or Usance?"}
    BL_Name_Check -- Buyer's bank's name --> LC_Type_TR{"LC type:<br>Sight or Usance?"}
    LC_Type_PN -- Sight LC --> Calc_Gap_PN_Sight["Calculate financing gap<br>using Sight LC formula"]
    LC_Type_PN -- Usance LC --> Calc_Gap_PN_Usance["Calculate financing gap<br>using Usance LC formula"]
    LC_Type_TR -- Sight LC --> Calc_Gap_TR_Sight["Calculate financing gap<br>using Sight LC formula"]
    LC_Type_TR -- Usance LC --> Calc_Gap_TR_Usance["Calculate financing gap<br>using Usance LC formula"]
    Calc_Gap_PN_Sight --> Need_Finance_PN{"Does buyer need<br>financing?"}
    Calc_Gap_PN_Usance --> Need_Finance_PN
    Calc_Gap_TR_Sight --> Need_Finance_TR{"Does buyer need<br>financing?"}
    Calc_Gap_TR_Usance --> Need_Finance_TR
    Need_Finance_PN -- Yes --> PN_LC["P/N under Letter of Credit (Buyer)"]
    PN_LC --> Check_Shipping_PN{"Was Shipping Guarantee<br>used earlier?"}
    Need_Finance_TR -- Yes --> TR_LC["Trust Receipt Loan under Letter of Credit"]
    TR_LC --> Endorsement["Endorsement Services"]
    Endorsement --> Check_Shipping_TR{"Was Shipping Guarantee<br>used earlier?"}
    Need_Finance_PN -- No --> Wait_Payment_PN["Wait for LC payment<br>at maturity"]
    Need_Finance_TR -- No --> Wait_Payment_TR["Wait for LC payment<br>at maturity"]
    Wait_Payment_PN --> Check_Shipping_PN
    Wait_Payment_TR --> Check_Shipping_TR
    Check_Shipping_PN -- Yes --> Exchange_SG_PN["Exchange B/L for<br>Shipping Guarantee"]
    Check_Shipping_TR -- Yes --> Exchange_SG_TR["Exchange B/L for<br>Shipping Guarantee"]
    Check_Shipping_PN -- No --> Complete_PN["Transaction completed.<br>Buyer has goods and financing."]
    Check_Shipping_TR -- No --> Complete_TR["Transaction completed.<br>Buyer has goods ownership."]
    Exchange_SG_PN --> Complete_PN
    Exchange_SG_TR --> Complete_TR

    BL_Arrived@{ shape: diamond}
     LC_Issuance:::product
     Shipping_Guarantee:::product
     PN_LC:::product
     TR_LC:::product
     Endorsement:::product
    classDef product fill:#e1f5fe,stroke:#01579b,stroke-width:2px,color:#000
```

## Product Categories

### Core Service

- **Letter of Credit Issuance/Amendment** - Base LC product for buyers/importers

### Post-Shipment Services & Financing

- **Trust Receipt Loan under Letter of Credit** - Buyer financing when bank has title to goods via B/L
- **P/N under Letter of Credit Buyer** - Buyer financing when buyer has title to goods via B/L
- **Shipping Guarantee Issuance** - Service when buyer needs goods released before bank receives original B/L
- **Endorsement Services** - Service to transfer ownership from bank to buyer (when bank had title)
- **Exchange B/L for Shipping Guarantee** - Service to replace temporary shipping guarantee with original B/L

## Decision Logic

### Primary Decision Points:

1. **Document Status** - Whether the buyer's bank has received the original B/L
2. **Immediate Release** - Whether buyer wants goods released before B/L arrival (Shipping Guarantee)
3. **Payment Terms** - Whether LC is Sight or Usance (when B/L received)
4. **Title Ownership** - Whether bank or buyer has title to goods via Bill of Lading
5. **Financing Needs** - Whether buyer needs working capital to handle goods
6. **Shipping Guarantee Settlement** - Whether to exchange B/L for previously issued Shipping Guarantee

### Key Considerations:

- **LC Issuance/Amendment** is the prerequisite core service for all buyers
- **Early Shipping Guarantee** option available when bank hasn't received B/L but buyer needs goods released immediately
- **Title ownership** (via B/L) determines the type of financing available:
  - Bank has title → Trust Receipt Loan → Endorsement Services
  - Buyer has title → P/N under Letter of Credit Buyer
- **Early document timing** creates the option for Shipping Guarantee when buyer needs goods released before bank receives original B/L
- **Shipping Guarantee closure** is required when guarantee was used - B/L must be exchanged to close the bank's liability
- **Financing decisions** are made after establishing title ownership

### Flow Logic:

The decision tree follows the natural sequence of international trade:

1. LC is issued for the transaction
2. Check if bank has received original B/L
   - If No: Decide whether to release goods immediately (Shipping Guarantee) or wait for B/L
3. If B/L received: Determine payment terms (Sight or Usance LC)
4. Determine who has title to the goods
5. Provide appropriate services and financing based on title ownership:
   - Bank has title → Financing decision → Trust Receipt or Endorsement → Was Shipping Guarantee used? → Exchange if needed → Claim goods
   - Buyer has title → Financing decision → P/N or Wait for Maturity → Was Shipping Guarantee used? → Exchange if needed → Claim goods

This ensures buyers receive services that match their exact position in the trade cycle and cash flow requirements.
