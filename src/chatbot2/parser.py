import re
import json
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
        # Handle both: B{What type of LC are you using?} and C[Export Bill | attr={"is_product": true}]
        # Use DOTALL flag to handle multi-line nodes
        node_pattern = re.compile(r"(\w+)\s*([{\[])(.*?)([}\]])", re.DOTALL)

        nodes: dict[str, DecisionTreeNode] = {}
        for match in node_pattern.finditer(md_text):
            node_id, bracket_open, content, bracket_close = match.groups()
            node_type = NodeType.DECISION if bracket_open == "{" else NodeType.END

            question_text = None

            # Clean content and look for question text
            clean_content = (
                content.replace("\n", " ").replace("\r", " ").replace("<br/>", " ")
            )

            # Extract question text
            if " | attr=" in clean_content:
                parts = clean_content.split(" | attr=", 1)
                question_text = parts[0].strip()
            else:
                question_text = clean_content.strip()

            nodes[node_id.strip()] = DecisionTreeNode(
                node_id=node_id.strip(),
                node_type=node_type,
                tree_name=tree_name,
                question=question_text,
                children=[],
            )

        # --- Edge pattern ---
        # Handle: "B -->|Sight LC | attr={"lc_type": "sight"}| C" and "A --> B"
        # Capture edge labels and actions
        edge_pattern = re.compile(
            r"(\w+)(?:\s*[{\[].*?[}\]])?\s*-->\s*(?:\|([^|]*?)\s*(?:\|\s*attr=(\{[^}]*\})\s*)?\|\s*)?(\w+)(?:\s*[{\[].*?[}\]])?",
            re.MULTILINE | re.DOTALL,
        )

        incoming_edges: set[str] = set()
        for match in edge_pattern.finditer(md_text):
            source_id, edge_label, edge_actions_str, target_id = match.groups()
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

                # Parse edge actions if present
                edge_actions = {}
                if edge_actions_str:
                    try:
                        edge_actions = json.loads(edge_actions_str.replace("'", '"'))
                    except json.JSONDecodeError as e:
                        print(
                            f"Warning: Could not parse edge actions for {source_id} -> {target_id}: {edge_actions_str}"
                        )

                # Extract target node metadata and add to edge actions
                target_node_match = re.search(
                    rf"{target_id}\[([^\]]*attr=\{{[^}}]*\}}[^\]]*)\]", md_text
                )
                if target_node_match:
                    content = target_node_match.group(1)
                    if " | attr=" in content:
                        parts = content.split(" | attr=", 1)
                        json_str = parts[1].strip()
                        if json_str.endswith("]"):
                            json_str = json_str[:-1]
                        try:
                            target_metadata = json.loads(json_str.replace("'", '"'))
                            edge_actions.update(target_metadata)
                        except json.JSONDecodeError:
                            pass

                # Add actions to edge if any exist
                if edge_actions:
                    edge_info["actions"] = edge_actions

                nodes[source_id].edges.append(edge_info)

                incoming_edges.add(target_id)

        # --- Roots (nodes without incoming edges) ---
        root_nodes: list[DecisionTreeNode] = [
            node for node_id, node in nodes.items() if node_id not in incoming_edges
        ]

        return DecisionTree(tree_name=tree_name, nodes=root_nodes, context=context)
