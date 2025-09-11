import re
from .models import DecisionTreeNode, NodeType, DecisionTree


class MermaidDecisionTreeParser:
    """
    Parser for Mermaid flowchart files to extract decision tree structure.
    Converts Mermaid DAG syntax into DecisionTreeNode objects, linking children directly.
    """

    def parse_mermaid_to_decision_tree(
        self, md_text: str, tree_name: str, context: str = ""
    ) -> DecisionTree:
        """
        Parse a Mermaid .md decision tree into DecisionTree Pydantic model.

        Args:
            md_text: Mermaid markdown text
            tree_name: Name of the decision tree
            context: Optional context for the tree

        Returns:
            DecisionTree instance
        """
        # --- Node pattern ---
        # Handle both: B{What type of LC<br/>are you using? | attr=lc_type} and C[Calculate financing gap<br/>with Sight LC formula | attr=is_sight_lc]
        # Use DOTALL flag to handle multi-line nodes
        node_pattern = re.compile(r"(\w+)\s*([{\[])(.*?)([}\]])", re.DOTALL)

        nodes: dict[str, DecisionTreeNode] = {}
        for match in node_pattern.finditer(md_text):
            node_id, bracket_open, content, bracket_close = match.groups()
            node_type = NodeType.DECISION if bracket_open == "{" else NodeType.END

            # Extract question text and attribute if present in content
            attr_name = None
            question_text = None

            # Clean content and look for question and attribute
            clean_content = (
                content.replace("\n", " ").replace("\r", " ").replace("<br/>", " ")
            )

            if " | attr=" in clean_content:
                parts = clean_content.split(" | attr=")
                if len(parts) >= 2:
                    question_text = parts[0].strip()
                    attr_name = parts[-1].strip()
            else:
                # If no attribute, the entire content is the question
                question_text = clean_content.strip()

            nodes[node_id.strip()] = DecisionTreeNode(
                node_id=node_id.strip(),
                node_type=node_type,
                tree_name=tree_name,
                attr_name=attr_name,
                question=question_text,
                children=[],
            )

        # --- Edge pattern ---
        # Handle both: "B -->|Sight LC| C" and "A --> B"
        # Capture edge labels when present
        edge_pattern = re.compile(
            r"(\w+)(?:\s*[{\[].*?[}\]])?\s*-->\s*(?:\|([^|]*)\|\s*)?(\w+)(?:\s*[{\[].*?[}\]])?",
            re.MULTILINE | re.DOTALL,
        )

        incoming_edges: set[str] = set()
        for match in edge_pattern.finditer(md_text):
            source_id, edge_label, target_id = match.groups()
            source_id = source_id.strip()
            target_id = target_id.strip()
            edge_label = edge_label.strip() if edge_label else None

            if source_id in nodes and target_id in nodes:
                # Add child node
                nodes[source_id].children.append(nodes[target_id])

                # Add edge information
                edge_info = {
                    "label": edge_label or target_id,  # Use target_id as fallback
                    "target": target_id,
                    "value": (
                        edge_label.lower().replace(" ", "_")
                        if edge_label
                        else target_id.lower()
                    ),
                }
                nodes[source_id].edges.append(edge_info)

                incoming_edges.add(target_id)

        # --- Roots (nodes without incoming edges) ---
        root_nodes: list[DecisionTreeNode] = [
            node for node_id, node in nodes.items() if node_id not in incoming_edges
        ]

        return DecisionTree(tree_name=tree_name, nodes=root_nodes, context=context)
