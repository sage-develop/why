from pydantic import BaseModel, Field
from enum import Enum


class LCType(str, Enum):
    SIGHT = "sight"
    USANCE = "usance"


class TransactionType(str, Enum):
    INTERNATIONAL = "international"
    DOMESTIC = "domestic"


class BLIssuedUnder(str, Enum):
    BUYER_NAME = "buyer_name"
    BANK_NAME = "bank_name"


class ClientRole(str, Enum):
    BUYER = "buyer"
    SELLER = "seller"


class ClientInfo(BaseModel):
    """Basic client information to determine role and applicable decision trees."""

    role: ClientRole | None = Field(
        None,
        description="Whether the client is a buyer, seller, or both in trade finance transactions",
    )


# lc_seller_post_shipment.md
class SellerPostShipmentLCDecision(BaseModel):
    """Seller Post-shipment LC attributes parsed from client information used to preanswer decision tree nodes."""

    lc_type: LCType | None = Field(None, description="LC type choice")
    needs_sight_financing: bool | None = Field(
        None, description="Needs sight financing"
    )
    needs_usance_financing: bool | None = Field(
        None, description="Needs usance financing"
    )


# lc_seller_preshipment.md
class SellerPreShipmentLCDecision(BaseModel):
    """Seller Pre-shipment LC attributes parsed from client information used to preanswer decision tree nodes."""

    worried_about_counterparty_risk: bool | None = Field(
        None,
        description="Whether seller is worried about counterparty risk or counterparty sovereign risk",
    )
    is_middleman: bool | None = Field(
        None, description="Whether seller is a middleman who doesn't make goods"
    )
    lc_is_transferable: bool | None = Field(
        None, description="Whether the LC is transferable"
    )
    wants_to_transfer_lc: bool | None = Field(
        None, description="Whether seller wants to transfer LC to supplier"
    )
    wants_to_assign_proceeds: bool | None = Field(
        None, description="Whether seller wants to redirect payments to third parties"
    )
    needs_preshipment_working_capital: bool | None = Field(
        None, description="Whether seller needs pre-shipment working capital"
    )


# lc_buyer_preshipment.md
class BuyerPreShipmentDecision(BaseModel):
    """Buyer pre-shipment LC attributes - only user choices."""

    # User choice attributes from edges
    transaction_type: TransactionType | None = Field(
        None, description="Transaction type choice"
    )
    bl_received_by_bank: bool | None = Field(
        None, description="Bank received original B/L"
    )
    wants_immediate_claim: bool | None = Field(
        None, description="Wants to claim goods immediately"
    )
    lc_type_buyer: LCType | None = Field(None, description="Buyer's LC type")
    lc_type_after_guarantee: LCType | None = Field(
        None, description="LC type after guarantee"
    )
    needs_buyer_financing: bool | None = Field(
        None, description="Buyer needs financing"
    )
    bl_issued_under: BLIssuedUnder | None = Field(
        None, description="Who B/L is issued under"
    )
    shipping_guarantee_used: bool | None = Field(
        None, description="Shipping guarantee used"
    )
    guarantee_issued_under: BLIssuedUnder | None = Field(
        None, description="Who guarantee issued under"
    )
    guarantee_used_after_pn: bool | None = Field(
        None, description="Guarantee used after P/N"
    )
    guarantee_used_after_endorsement: bool | None = Field(
        None, description="Guarantee used after endorsement"
    )


# class Stage(str, Enum):
#     PRESHIPMENT = "pre-shipment"
#     POSTSHIPMENT = "post-shipment"


# class ComprehensiveTradeFinanceDecision(BaseModel):
#     """Comprehensive trade finance attributes - only user choices, no question identifiers."""

#     # Core identification choices
#     party_role: PartyRole | None = Field(
#         None, description="Whether client is buyer or seller"
#     )
#     seller_stage: Stage | None = Field(None, description="Seller's current stage")
#     buyer_stage: Stage | None = Field(None, description="Buyer's current stage")

#     # Transaction type choices
#     transaction_type: TransactionType | None = Field(
#         None, description="International or domestic transaction"
#     )
#     seller_transaction_type: TransactionType | None = Field(
#         None, description="Seller transaction type"
#     )
#     buyer_transaction_type: TransactionType | None = Field(
#         None, description="Buyer transaction type"
#     )

#     # LC type choices
#     lc_type: LCType | None = Field(None, description="LC type (sight/usance)")
#     seller_lc_type: LCType | None = Field(None, description="Seller's LC type")
#     buyer_lc_type: LCType | None = Field(None, description="Buyer's LC type")
#     lc_type_buyer: LCType | None = Field(None, description="Buyer LC type choice")
#     lc_type_after_guarantee: LCType | None = Field(
#         None, description="LC type after guarantee issued"
#     )

#     # Seller pre-shipment choices
#     has_counterparty_risk_concern: bool | None = Field(
#         None, description="Has concerns about counterparty/sovereign risk"
#     )
#     wants_redirect_payments: bool | None = Field(
#         None, description="Wants to redirect payments to third parties"
#     )
#     is_middleman: bool | None = Field(
#         None, description="Acting as middleman/trading company"
#     )
#     lc_is_transferrable: bool | None = Field(None, description="LC is transferrable")
#     wants_transfer_lc: bool | None = Field(
#         None, description="Wants to transfer LC to supplier"
#     )
#     wants_assign_proceeds_alt: bool | None = Field(
#         None, description="Alternative assignment of proceeds"
#     )
#     needs_preshipment_capital: bool | None = Field(
#         None, description="Needs pre-shipment working capital"
#     )

#     # Seller post-shipment choices
#     needs_sight_financing: bool | None = Field(
#         None, description="Needs financing for sight LC"
#     )
#     needs_usance_financing: bool | None = Field(
#         None, description="Needs financing for usance LC"
#     )

#     # Buyer pre-shipment choices
#     bl_received_by_bank: bool | None = Field(
#         None, description="Bank has received original B/L"
#     )
#     wants_immediate_claim: bool | None = Field(
#         None, description="Wants to claim goods immediately"
#     )
#     needs_buyer_financing: bool | None = Field(
#         None, description="Buyer needs financing"
#     )
#     bl_issued_under: BLIssuedUnder | None = Field(
#         None, description="Who B/L is issued under"
#     )
#     shipping_guarantee_used: bool | None = Field(
#         None, description="Shipping guarantee was used"
#     )
#     guarantee_issued_under: BLIssuedUnder | None = Field(
#         None, description="Who guarantee is issued under"
#     )
#     guarantee_used_after_pn: bool | None = Field(
#         None, description="Shipping guarantee used after P/N"
#     )
#     guarantee_used_after_endorsement: bool | None = Field(
#         None, description="Shipping guarantee used after endorsement"
#     )
#     needs_ownership_transfer: bool | None = Field(
#         None, description="Needs ownership transfer"
#     )

#     # Comprehensive attributes from multiple flows
#     has_counterparty_risk: bool | None = Field(
#         None, description="Has counterparty risk concerns (comprehensive flow)"
#     )
