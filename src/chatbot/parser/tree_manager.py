from pathlib import Path
from ..decision_tree import DecisionNode, NodeType
from .mermaid_parser import MermaidDecisionTreeParser


class MultiDecisionTreeManager:
    """
    Manages multiple decision trees loaded from mermaid files.
    Provides interface for traversing across multiple trees.
    """

    def __init__(self):
        self.parser = MermaidDecisionTreeParser()

        # {tree_name -> {node_id -> DecisionNode}}
        self.trees: dict[str, dict[str, DecisionNode]] = {}
        # tree_name -> metadata
        self.tree_metadata: dict[str, dict[str, str]] = {}

    def load_trees_from_directory(self, directory: Path) -> None:
        """
        Load all mermaid (.md) files from a directory.

        Args:
            directory: Path to directory containing mermaid files
        """
        if not directory.exists():
            raise FileNotFoundError(f"Directory not found: {directory}")

        # Find all .md files in the directory
        mermaid_files = list(directory.glob("*.md"))

        if not mermaid_files:
            # Also check in the root directory
            mermaid_files = list(directory.parent.glob("*decision*.md"))

        self.load_trees_from_files(mermaid_files)

    def load_trees_from_files(self, file_paths: list[Path]) -> None:
        """
        Load decision trees from specified mermaid files.

        Args:
            file_paths: list of paths to mermaid files
        """
        for file_path in file_paths:
            if file_path.exists():
                tree_name = file_path.stem
                try:
                    tree_nodes = self.parser.parse_file(file_path)
                    if tree_nodes:  # Only add if we successfully parsed nodes
                        self.trees[tree_name] = tree_nodes
                        self.tree_metadata[tree_name] = {
                            "source_file": str(file_path),
                            "node_count": len(tree_nodes),
                        }
                        print(
                            f"Loaded decision tree '{tree_name}' with {len(tree_nodes)} nodes"
                        )
                    else:
                        print(f"Warning: No nodes found in {file_path}")
                except Exception as e:
                    print(f"Error parsing {file_path}: {e}")
            else:
                print(f"Warning: File not found: {file_path}")

    def get_all_trees(self) -> dict[str, dict[str, DecisionNode]]:
        """Get all loaded decision trees."""
        return self.trees

    def get_tree(self, tree_name: str) -> dict[str, DecisionNode] | None:
        """Get a specific decision tree by name."""
        return self.trees.get(tree_name)

    def get_tree_names(self) -> list[str]:
        """Get names of all loaded decision trees."""
        return list(self.trees.keys())

    def get_all_decision_nodes(self) -> list[DecisionNode]:
        """
        Get all decision nodes from all loaded trees.
        Used by PreAnswerExtractor to analyze client information across all trees.
        """
        all_nodes = []
        for tree_nodes in self.trees.values():
            all_nodes.extend(tree_nodes.values())
        return all_nodes

    def get_decision_nodes_by_type(self, node_type: NodeType) -> list[DecisionNode]:
        """Get all nodes of a specific type from all trees."""
        nodes = []
        for tree_nodes in self.trees.values():
            for node in tree_nodes.values():
                if node.node_type == node_type:
                    nodes.append(node)
        return nodes

    def get_node(
        self, node_id: str, tree_name: str | None = None
    ) -> DecisionNode | None:
        """
        Get a specific node by ID.

        Args:
            node_id: The node ID to search for
            tree_name: Optional tree name to search in. If None, searches all trees.

        Returns:
            DecisionNode if found, None otherwise
        """
        if tree_name:
            tree = self.get_tree(tree_name)
            return tree.get(node_id) if tree else None
        else:
            # Search across all trees
            for tree_nodes in self.trees.values():
                if node_id in tree_nodes:
                    return tree_nodes[node_id]
            return None

    def get_next_node_id(
        self, current_node_id: str, choice: str, tree_name: str | None = None
    ) -> str | None:
        """
        Get the next node ID based on current node and choice.

        Args:
            current_node_id: Current node ID
            choice: User's choice
            tree_name: Optional tree name to search in

        Returns:
            Next node ID if found, None otherwise
        """
        current_node = self.get_node(current_node_id, tree_name)
        if current_node and choice in current_node.children:
            return current_node.children[choice]
        return None

    def find_start_nodes(self) -> list[tuple[str, DecisionNode]]:
        """
        Find all start nodes across all trees.

        Returns:
            list of (tree_name, start_node) tuples
        """
        start_nodes = []
        for tree_name, tree_nodes in self.trees.items():
            for node in tree_nodes.values():
                if node.node_type == NodeType.START:
                    start_nodes.append((tree_name, node))
        return start_nodes

    def get_tree_summary(self) -> dict[str, dict]:
        """Get summary information about all loaded trees."""
        summary = {}
        for tree_name, tree_nodes in self.trees.items():
            node_types = {}
            for node in tree_nodes.values():
                node_type = node.node_type.value
                node_types[node_type] = node_types.get(node_type, 0) + 1

            summary[tree_name] = {
                "total_nodes": len(tree_nodes),
                "node_types": node_types,
                "source_file": self.tree_metadata.get(tree_name, {}).get(
                    "source_file", "Unknown"
                ),
            }

        return summary

    def validate_trees(self) -> dict[str, list[str]]:
        """
        Validate all loaded trees for common issues.

        Returns:
            dictionary mapping tree_name -> list of validation issues
        """
        issues = {}

        for tree_name, tree_nodes in self.trees.items():
            tree_issues = []

            # Check for start nodes
            start_nodes = [
                n for n in tree_nodes.values() if n.node_type == NodeType.START
            ]
            if len(start_nodes) == 0:
                tree_issues.append("No start node found")
            elif len(start_nodes) > 1:
                tree_issues.append(
                    f"Multiple start nodes found: {[n.node_id for n in start_nodes]}"
                )

            # Check for orphaned nodes (no incoming edges)
            referenced_nodes = set()
            for node in tree_nodes.values():
                referenced_nodes.update(node.children.values())

            orphaned = []
            for node_id, node in tree_nodes.items():
                if node_id not in referenced_nodes and node.node_type != NodeType.START:
                    orphaned.append(node_id)

            if orphaned:
                tree_issues.append(f"Orphaned nodes (no incoming edges): {orphaned}")

            # Check for broken references
            broken_refs = []
            for node in tree_nodes.values():
                for choice, next_node_id in node.children.items():
                    if next_node_id not in tree_nodes:
                        broken_refs.append(
                            f"{node.node_id} -> {next_node_id} (choice: {choice})"
                        )

            if broken_refs:
                tree_issues.append(f"Broken node references: {broken_refs}")

            # Check for nodes with no choices (non-terminal)
            no_choices = []
            for node in tree_nodes.values():
                if not node.choices and node.node_type not in [
                    NodeType.END,
                    NodeType.PRODUCT,
                ]:
                    no_choices.append(node.node_id)

            if no_choices:
                tree_issues.append(f"Non-terminal nodes with no choices: {no_choices}")

            if tree_issues:
                issues[tree_name] = tree_issues

        return issues

    def get_conflicting_node_ids(self) -> dict[str, list[str]]:
        """
        Find node IDs that exist in multiple trees (potential conflicts).

        Returns:
            dictionary mapping node_id -> list of tree_names containing that node_id
        """
        node_locations = {}
        conflicts = {}

        for tree_name, tree_nodes in self.trees.items():
            for node_id in tree_nodes.keys():
                if node_id not in node_locations:
                    node_locations[node_id] = []
                node_locations[node_id].append(tree_name)

        # Find conflicts (node_ids in multiple trees)
        for node_id, tree_names in node_locations.items():
            if len(tree_names) > 1:
                conflicts[node_id] = tree_names

        return conflicts
