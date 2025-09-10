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
