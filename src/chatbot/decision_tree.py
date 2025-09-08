from enum import Enum
from pydantic import BaseModel
from src.chatbot.session import ConsultationSession


class NodeType(Enum):
    PREPROCESSING = "preprocessing"  # preprocessing node
    START = "start"  # root node of DAG
    DECISION = "decision"  # decision node
    PRODUCT = "product"  # product node
    END = "end"  # terminal node


class DecisionNode(BaseModel):
    node_id: str
    node_type: NodeType
    question: str
    choices: list[str]
    children: dict[str, str]
    products: list[str] = []


class GlobalMarketsDecisionTree:
    """
    Handles the Global Markets decision tree logic based on the DAG structure.
    Ensures both FX and Interest Rate branches are traversed completely.
    """

    def __init__(self):
        self.nodes = self._build_decision_tree()  # TODO: This should be dynamic
        self.fx_branch_products = set()
        self.ir_branch_products = set()
        self.fx_completed = False
        self.ir_completed = False

    def _build_decision_tree(self) -> dict[str, DecisionNode]:
        """
        Build the complete decision tree from the DAG structure.
        Based on the DAG in product_recommendation_decision_dag.md
        """
        nodes = {}

        # Start node
        nodes["start"] = DecisionNode(
            node_id="start",
            node_type=NodeType.START,
            question="Welcome to Global Markets Product Consultation",
            choices=["Begin consultation"],
            children={"Begin consultation": "client_type"},
        )

        # Client Type (FX Branch Start)
        nodes["client_type"] = DecisionNode(
            node_id="client_type",
            node_type=NodeType.DECISION,
            question="What is the client's business activity?",
            choices=[
                "Importer (Needs to buy foreign currency)",
                "Exporter (Receives foreign currency)",
                "Both Importer & Exporter",
            ],
            children={
                "Importer (Needs to buy foreign currency)": "importer_flow",
                "Exporter (Receives foreign currency)": "exporter_flow",
                "Both Importer & Exporter": "natural_hedge",
            },
        )

        # Natural Hedge Check
        nodes["natural_hedge"] = DecisionNode(
            node_id="natural_hedge",
            node_type=NodeType.DECISION,
            question="Do foreign currency payments and receipts cancel out?",
            choices=["Yes", "No"],
            children={"Yes": "no_fx_needed", "No": "net_position"},
        )

        nodes["no_fx_needed"] = DecisionNode(
            node_id="no_fx_needed",
            node_type=NodeType.END,
            question="Natural hedge exists - No FX products needed",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
        )

        nodes["net_position"] = DecisionNode(
            node_id="net_position",
            node_type=NodeType.DECISION,
            question="What is your net FX position after netting?",
            choices=[
                "Net Importer (Need to buy foreign currency)",
                "Net Exporter (Need to sell foreign currency)",
            ],
            children={
                "Net Importer (Need to buy foreign currency)": "importer_flow",
                "Net Exporter (Need to sell foreign currency)": "exporter_flow",
            },
        )

        # Importer Flow
        nodes["importer_flow"] = DecisionNode(
            node_id="importer_flow",
            node_type=NodeType.DECISION,
            question="Is required currency supported? (Major currencies + MYR, KRW, VND)",
            choices=["Yes", "No"],
            children={"Yes": "hedge_decision_importer", "No": "currency_not_supported"},
        )

        # Exporter Flow
        nodes["exporter_flow"] = DecisionNode(
            node_id="exporter_flow",
            node_type=NodeType.DECISION,
            question="Is received currency supported? (Major currencies + MYR, KRW, VND)",
            choices=["Yes", "No"],
            children={"Yes": "hedge_decision_exporter", "No": "currency_not_supported"},
        )

        nodes["currency_not_supported"] = DecisionNode(
            node_id="currency_not_supported",
            node_type=NodeType.END,
            question="Currency not supported - Cannot provide service",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
        )

        # Hedge Decisions
        nodes["hedge_decision_importer"] = DecisionNode(
            node_id="hedge_decision_importer",
            node_type=NodeType.DECISION,
            question="Want to hedge FX volatility/risk?",
            choices=["Yes", "No"],
            children={"Yes": "hedge_proportion_importer", "No": "fx_spot_buy"},
        )

        nodes["hedge_decision_exporter"] = DecisionNode(
            node_id="hedge_decision_exporter",
            node_type=NodeType.DECISION,
            question="Want to hedge FX volatility/risk?",
            choices=["Yes", "No"],
            children={"Yes": "hedge_proportion_exporter", "No": "fx_spot_sell"},
        )

        # FX Spot Products (Terminal for non-hedge path)
        nodes["fx_spot_buy"] = DecisionNode(
            node_id="fx_spot_buy",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Spot - Bank Sells (Client buys foreign currency)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Sells"],
        )

        nodes["fx_spot_sell"] = DecisionNode(
            node_id="fx_spot_sell",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Spot - Bank Buys (Client sells foreign currency)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Buys"],
        )

        # Hedge Proportion
        nodes["hedge_proportion_importer"] = DecisionNode(
            node_id="hedge_proportion_importer",
            node_type=NodeType.DECISION,
            question="What proportion to hedge?",
            choices=["Partial hedging needed", "Full hedging needed"],
            children={
                "Partial hedging needed": "partial_hedge_importer",
                "Full hedging needed": "hedge_product_importer",
            },
        )

        nodes["hedge_proportion_exporter"] = DecisionNode(
            node_id="hedge_proportion_exporter",
            node_type=NodeType.DECISION,
            question="What proportion to hedge?",
            choices=["Partial hedging needed", "Full hedging needed"],
            children={
                "Partial hedging needed": "partial_hedge_exporter",
                "Full hedging needed": "hedge_product_exporter",
            },
        )

        # Partial Hedge (leads to both spot and hedge products)
        nodes["partial_hedge_importer"] = DecisionNode(
            node_id="partial_hedge_importer",
            node_type=NodeType.DECISION,
            question="For partial hedging, you need both spot and hedge products. Certain about date and amount for hedged portion?",
            choices=["Yes", "No"],
            children={"Yes": "fx_forward_sell_partial", "No": "fx_call_option_partial"},
        )

        nodes["partial_hedge_exporter"] = DecisionNode(
            node_id="partial_hedge_exporter",
            node_type=NodeType.DECISION,
            question="For partial hedging, you need both spot and hedge products. Certain about date and amount for hedged portion?",
            choices=["Yes", "No"],
            children={"Yes": "fx_forward_buy_partial", "No": "fx_put_option_partial"},
        )

        # Hedge Product Selection
        nodes["hedge_product_importer"] = DecisionNode(
            node_id="hedge_product_importer",
            node_type=NodeType.DECISION,
            question="Certain about date and amount?",
            choices=["Yes", "No"],
            children={"Yes": "fx_forward_sell_full", "No": "fx_call_option_full"},
        )

        nodes["hedge_product_exporter"] = DecisionNode(
            node_id="hedge_product_exporter",
            node_type=NodeType.DECISION,
            question="Certain about date and amount?",
            choices=["Yes", "No"],
            children={"Yes": "fx_forward_buy_full", "No": "fx_put_option_full"},
        )

        # Forward Products
        nodes["fx_forward_sell_partial"] = DecisionNode(
            node_id="fx_forward_sell_partial",
            node_type=NodeType.PRODUCT,
            question="Recommended products: FX Spot - Bank Sells (for unhedged portion) + FX Forward Contract - Bank Sells (for hedged portion)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Sells", "FX Forward Contract - Bank Sells"],
        )

        nodes["fx_forward_sell_full"] = DecisionNode(
            node_id="fx_forward_sell_full",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Forward Contract - Bank Sells",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Forward Contract - Bank Sells"],
        )

        nodes["fx_forward_buy_partial"] = DecisionNode(
            node_id="fx_forward_buy_partial",
            node_type=NodeType.PRODUCT,
            question="Recommended products: FX Spot - Bank Buys (for unhedged portion) + FX Forward Contract - Bank Buys (for hedged portion)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Buys", "FX Forward Contract - Bank Buys"],
        )

        nodes["fx_forward_buy_full"] = DecisionNode(
            node_id="fx_forward_buy_full",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Forward Contract - Bank Buys",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Forward Contract - Bank Buys"],
        )

        # Option Products
        nodes["fx_call_option_partial"] = DecisionNode(
            node_id="fx_call_option_partial",
            node_type=NodeType.PRODUCT,
            question="Recommended products: FX Spot - Bank Sells (for unhedged portion) + FX Call Option (for hedged portion)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Sells", "FX Call Option"],
        )

        nodes["fx_call_option_full"] = DecisionNode(
            node_id="fx_call_option_full",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Call Option (Right to buy foreign currency)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Call Option"],
        )

        nodes["fx_put_option_partial"] = DecisionNode(
            node_id="fx_put_option_partial",
            node_type=NodeType.PRODUCT,
            question="Recommended products: FX Spot - Bank Buys (for unhedged portion) + FX Put Option (for hedged portion)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Spot - Bank Buys", "FX Put Option"],
        )

        nodes["fx_put_option_full"] = DecisionNode(
            node_id="fx_put_option_full",
            node_type=NodeType.PRODUCT,
            question="Recommended product: FX Put Option (Right to sell foreign currency)",
            choices=["Continue to Interest Rate consultation"],
            children={"Continue to Interest Rate consultation": "ir_check"},
            products=["FX Put Option"],
        )

        # Interest Rate Branch
        nodes["ir_check"] = DecisionNode(
            node_id="ir_check",
            node_type=NodeType.DECISION,
            question="Does client want to hedge Interest Rate risk?",
            choices=["Yes", "No"],
            children={"Yes": "currency_match", "No": "ir_complete"},
        )

        nodes["currency_match"] = DecisionNode(
            node_id="currency_match",
            node_type=NodeType.DECISION,
            question="Same currency as FX exposure?",
            choices=["Yes", "No"],
            children={"Yes": "irs_product", "No": "ccs_product"},
        )

        nodes["irs_product"] = DecisionNode(
            node_id="irs_product",
            node_type=NodeType.PRODUCT,
            question="Recommended product: Interest Rate Swap (Single currency)",
            choices=["Complete consultation"],
            children={"Complete consultation": "consultation_complete"},
            products=["Interest Rate Swap"],
        )

        nodes["ccs_product"] = DecisionNode(
            node_id="ccs_product",
            node_type=NodeType.PRODUCT,
            question="Recommended product: Cross Currency Swap (Multi-currency)",
            choices=["Complete consultation"],
            children={"Complete consultation": "consultation_complete"},
            products=["Cross Currency Swap"],
        )

        nodes["ir_complete"] = DecisionNode(
            node_id="ir_complete",
            node_type=NodeType.END,
            question="No IR hedging needed",
            choices=["Complete consultation"],
            children={"Complete consultation": "consultation_complete"},
        )

        # Final node
        nodes["consultation_complete"] = DecisionNode(
            node_id="consultation_complete",
            node_type=NodeType.END,
            question="Consultation Complete",
            choices=["Start new consultation"],
            children={"Start new consultation": "start"},
        )

        return nodes

    def get_node(self, node_id: str) -> DecisionNode | None:
        """Get a node by its ID."""
        return self.nodes.get(node_id)

    def get_next_node(self, current_node_id: str, choice: str) -> str | None:
        """Get the next node ID based on current node and choice."""
        node = self.get_node(current_node_id)
        if node and choice in node.children:
            return node.children[choice]
        return None

    def is_fx_branch_complete(self, node_id: str) -> bool:
        """Check if we've reached a terminal point in the FX branch."""
        return node_id == "ir_check"

    def is_ir_branch_complete(self, node_id: str) -> bool:
        """Check if we've reached a terminal point in the IR branch."""
        return node_id == "consultation_complete"
