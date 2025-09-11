from pydantic import BaseModel, Field
from enum import Enum


class NodeType(Enum):
    DECISION = "decision"  # decision node
    END = "end"  # terminal node (this could be a product node)


# Example single decision tree
class SellerPostShipmentLCDecision(BaseModel):
    """Seller Post-shipment LC attributes parsed from client information used to preanswer decision tree nodes."""

    lc_type: str | None = None
    is_sight_lc: bool | None = None
    is_usance_lc: bool | None = None
    needs_financing: bool | None = None
    use_export_bill: bool | None = None
    wait_for_sight_payment: bool | None = None
    use_bill_receivable: bool | None = None
    wait_for_usance_payment: bool | None = None
    transaction_completed: bool | None = None


class DecisionTreeNode(BaseModel):
    """A decision tree node parsed from a mermaid decision tree file."""

    # e.g. "B", "C", "E", "node_123"
    node_id: str = Field(description="The decision tree node ID")

    # e.g. NodeType.DECISION, NodeType.END
    node_type: NodeType = Field(description="The type of the decision node")

    # e.g. "SellerPostShipmentLC", "GlobalMarkets"
    tree_name: str = Field(description="Name/identifier of the decision tree")

    # e.g. "is_sight_lc", "needs_financing", "use_export_bill"
    attr_name: str | None = Field(description="The attribute of the decision tree node")

    # e.g. "What type of LC are you using?", "Do you need financing?"
    question: str | None = Field(description="The question of the decision tree node")

    # e.g. [node_c, node_d] for a binary decision
    children: list["DecisionTreeNode"] = Field(
        default_factory=list, description="Child nodes"
    )

    # e.g. [{"label": "Sight LC", "value": "sight_lc", "target": "C"},
    #       {"label": "Yes", "value": "yes", "target": "G"}]
    edges: list[dict[str, str]] = Field(
        default_factory=list, description="Edge labels and targets from this node"
    )


class DecisionTree(BaseModel):
    """A decision tree parsed from a mermaid decision tree file."""

    tree_name: str = Field(description="Name/identifier of the decision tree")
    nodes: list[DecisionTreeNode] = Field(description="The nodes of the decision tree")
    context: str = Field(description="The context of the decision tree")
