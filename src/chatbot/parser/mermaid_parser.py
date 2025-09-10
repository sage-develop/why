import re
from pathlib import Path
from src.chatbot.decision_tree import DecisionNode, NodeType


class MermaidDecisionTreeParser:
    """
    Parser for Mermaid flowchart files to extract decision tree structure.
    Converts mermaid DAG syntax into DecisionNode objects for the chatbot system.
    """

    def __init__(self):
        # Regex patterns for parsing mermaid syntax
        self.node_pattern = re.compile(
            r"(\w+)\s*(?:\[\"([^\"]*)\"\]|\[([^\]]*)\]|{\"([^\"]*)\"}|{([^}]*)})"
        )
        self.edge_pattern = re.compile(r"(\w+)\s*-->\s*(?:\|([^|]*)\|)?\s*(\w+)")
        self.class_def_pattern = re.compile(r"class\s+([^\\s]+)\s+(\w+)")

    def parse_file(self, file_path: Path) -> dict[str, DecisionNode]:
        """
        Parse a mermaid decision tree file and return DecisionNode objects.

        Args:
            file_path: Path to the mermaid file

        Returns:
            dictionary mapping node_id -> DecisionNode
        """
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        return self.parse_content(content)

    def parse_content(self, content: str) -> dict[str, DecisionNode]:
        """
        Parse mermaid content and extract decision tree structure.

        Args:
            content: Raw mermaid file content (flowchart only)

        Returns:
            dictionary mapping node_id -> DecisionNode
        """
        # Since files contain only flowchart content, use content directly
        flowchart_content = content

        # Parse nodes and their labels/types
        nodes = self._parse_nodes(flowchart_content)

        # Parse edges and build relationships
        edges = self._parse_edges(flowchart_content)

        # Parse class definitions to determine node types
        node_classes = self._parse_node_classes(flowchart_content)

        # Build DecisionNode objects
        decision_nodes = self._build_decision_nodes(nodes, edges, node_classes)

        return decision_nodes

    def _parse_nodes(self, content: str) -> dict[str, str]:
        """
        Parse node definitions and extract node labels.

        Returns:
            dictionary mapping node_id -> node_label
        """
        nodes = {}
        lines = content.split("\n")

        for line in lines:
            # Skip class definitions and other non-node lines
            if line.strip().startswith("class ") or line.strip().startswith("classDef"):
                continue

            # Look for node definitions (both standalone and in edges)
            # Handle different mermaid node syntaxes

            # Pattern 1: node_id["label"] or node_id[label]
            node_matches = re.findall(
                r"(\w+)\s*\[\"([^\"]*)\"\]|(\w+)\s*\[([^\]]*)\]", line
            )
            for match in node_matches:
                if match[0] and match[1]:  # quoted label
                    nodes[match[0]] = (
                        match[1].replace("<br/>", " ").replace("<br>", " ")
                    )
                elif match[2] and match[3]:  # unquoted label
                    nodes[match[2]] = (
                        match[3].replace("<br/>", " ").replace("<br>", " ")
                    )

            # Pattern 2: node_id{"label"} or node_id{label} (decision nodes)
            decision_matches = re.findall(
                r"(\w+)\s*\{\"([^\"]*)\"\}|(\w+)\s*\{([^}]*)\}", line
            )
            for match in decision_matches:
                if match[0] and match[1]:  # quoted label
                    nodes[match[0]] = (
                        match[1].replace("<br/>", " ").replace("<br>", " ")
                    )
                elif match[2] and match[3]:  # unquoted label
                    nodes[match[2]] = (
                        match[3].replace("<br/>", " ").replace("<br>", " ")
                    )

        return nodes

    def _parse_edges(self, content: str) -> list[(str, str, str)]:
        """
        Parse edge definitions to build node relationships.

        Returns:
            list of tuples (from_node, edge_label, to_node)
        """
        edges = []
        lines = content.split("\n")

        for line in lines:
            # Skip class definitions
            if line.strip().startswith("class ") or line.strip().startswith("classDef"):
                continue

            # Pattern: from_node -->|edge_label| to_node
            # or: from_node --> to_node
            edge_matches = re.findall(r"(\w+)\s*-->\s*(?:\|([^|]*)\|)?\s*(\w+)", line)

            for match in edge_matches:
                from_node, edge_label, to_node = match
                edge_label = edge_label.strip() if edge_label else ""
                edges.append((from_node, edge_label, to_node))

        return edges

    def _parse_node_classes(self, content: str) -> dict[str, str]:
        """
        Parse class definitions to determine node types.

        Returns:
            dictionary mapping node_id -> class_name
        """
        node_classes = {}
        lines = content.split("\n")

        for line in lines:
            if line.strip().startswith("class "):
                # Pattern: class Nodelist className
                match = re.match(r"class\s+([\w,]+)\s+(\w+)", line.strip())
                if match:
                    node_list, class_name = match.groups()
                    # Handle comma-separated node list
                    for node_id in node_list.split(","):
                        node_classes[node_id.strip()] = class_name.strip()

        return node_classes

    def _build_decision_nodes(
        self,
        nodes: dict[str, str],
        edges: list[(str, str, str)],
        node_classes: dict[str, str],
    ) -> dict[str, DecisionNode]:
        """
        Build DecisionNode objects from parsed mermaid data.

        Args:
            nodes: node_id -> label mapping
            edges: list of (from_node, edge_label, to_node) tuples
            node_classes: node_id -> class_name mapping

        Returns:
            dictionary mapping node_id -> DecisionNode
        """
        decision_nodes = {}

        # Build children mapping and choices for each node
        for node_id, label in nodes.items():
            # Find all outgoing edges from this node
            outgoing_edges = [
                (edge_label, to_node)
                for from_node, edge_label, to_node in edges
                if from_node == node_id
            ]

            # Build children dict and choices list
            children = {}
            choices = []
            products = []

            for edge_label, to_node in outgoing_edges:
                if edge_label:  # Edge has a label (represents a choice)
                    children[edge_label] = to_node
                    choices.append(edge_label)
                else:  # Edge has no label (automatic transition)
                    # For nodes without choice labels, use the target node's label as choice
                    target_label = nodes.get(to_node, to_node)
                    # Clean up the target label for use as a choice
                    choice_text = self._clean_choice_text(target_label)
                    children[choice_text] = to_node
                    choices.append(choice_text)

            # Determine node type based on class or heuristics
            node_type = self._determine_node_type(node_id, label, node_classes)

            # Extract products from product nodes
            if node_type == NodeType.PRODUCT:
                products = self._extract_products_from_label(label)

            # Create DecisionNode
            decision_nodes[node_id] = DecisionNode(
                node_id=node_id,
                node_type=node_type,
                question=label,
                choices=choices,
                children=children,
                products=products,
            )

        return decision_nodes

    def _determine_node_type(
        self, node_id: str, label: str, node_classes: dict[str, str]
    ) -> NodeType:
        """Determine the node type based on class definitions or heuristics."""

        # Check class definitions first
        class_name = node_classes.get(node_id, "").lower()

        if class_name == "startnode":
            return NodeType.START
        elif class_name == "decisionnode":
            return NodeType.DECISION
        elif class_name == "productnode":
            return NodeType.PRODUCT
        elif class_name == "endnode":
            return NodeType.END
        elif class_name == "warningnode":
            return NodeType.END  # Treat warnings as end nodes

        # Heuristic-based detection if no class is defined
        label_lower = label.lower()

        # Start nodes
        if any(
            word in label_lower for word in ["start", "begin", "welcome", "assessment"]
        ):
            return NodeType.START

        # Product nodes (contain "recommend" or product names)
        if "recommend:" in label_lower or "recommended" in label_lower:
            return NodeType.PRODUCT

        # End nodes
        if any(
            phrase in label_lower
            for phrase in [
                "complete",
                "finished",
                "not supported",
                "cannot provide",
                "no",
                "needed",
            ]
        ) and not any(phrase in label_lower for phrase in ["question", "decision"]):
            return NodeType.END

        # Default to decision for questions
        return NodeType.DECISION

    def _extract_products_from_label(self, label: str) -> list[str]:
        """Extract product names from a product node label."""
        products = []

        # Look for products after "Recommend:" or "Recommended"
        if "recommend:" in label.lower():
            product_section = label.split(":", 1)[1] if ":" in label else label
        else:
            product_section = label

        # Split by bullet points or line breaks
        product_lines = re.split(r"[•\n]", product_section)

        for line in product_lines:
            line = line.strip()
            if line and not line.lower().startswith("recommend"):
                # Clean up the product name
                product = re.sub(r"\([^)]*\)", "", line).strip()  # Remove parentheses
                if product:
                    products.append(product)

        return products

    def _clean_choice_text(self, text: str) -> str:
        """Clean up text to be used as a choice option."""
        # Remove HTML-like tags
        text = re.sub(r"<[^>]+>", "", text)
        # Remove extra whitespace
        text = " ".join(text.split())
        # Limit length
        if len(text) > 100:
            text = text[:97] + "..."
        return text

    def parse_multiple_files(
        self, file_paths: list[Path]
    ) -> dict[str, dict[str, DecisionNode]]:
        """
        Parse multiple mermaid files and return trees organized by file.

        Args:
            file_paths: list of paths to mermaid files

        Returns:
            dictionary mapping filename -> {node_id -> DecisionNode}
        """
        trees = {}

        for file_path in file_paths:
            tree_name = file_path.stem  # Use filename without extension as tree name
            trees[tree_name] = self.parse_file(file_path)

        return trees
