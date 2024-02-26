from __future__ import annotations

from collections import deque
from typing import Generator


class Node:
    def __init__(self, key: str, description: str):
        self.key = key
        self.description = description
        self.children: list[Node] = []
        self.source = False
        self.terminate = False


def _integer_to_letter(n):
    """Converts a positive integer to an Excel column name."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result  # Convert remainder to corresponding letter
    return result


def generate_sequence():
    """Generates a sequence of Excel column names from start to end."""
    i = 1
    while True:
        yield _integer_to_letter(i)
        i += 1


def _get_parents(transformer: dict, leaves: dict) -> list[Node]:
    """
    Get the parent(s) node(s) of the transformer.

    Args:
        transformer (dict): The transformer parameters.
        leaves (dict): The leaves dictionary.

    Returns:
        list[Node]: The parent(s) node(s).
    """
    if "source" in transformer:
        source_name = transformer["source"]
        return [leaves[source_name]]
    elif "left" in transformer:
        left_name = transformer["left"]
        right_name = transformer["right"]
        return [leaves[left_name], leaves[right_name]]
    elif "sources" in transformer:
        return [leaves[source_name] for source_name in transformer["sources"]]
    else:
        raise ValueError("Missing parent information (source | left & right | sources key).")


def _get_target(transformer: dict, seq: Generator[str, None, None], leaves: dict) -> Node:
    """
    Get the target node of the transformer.
    Update the leaves dictionary with the new mermaid ID.

    Args:
        transformer (dict): The transformer parameters.
        seq (Generator[str, None, None]): The sequence generator.
        leaves (dict): The leaves dictionary.

    Returns:
        Node: The target node.
    """
    if "target" in transformer:
        target_name = transformer["target"]
    elif "source" in transformer:
        target_name = transformer["source"]
    elif "left" in transformer:
        target_name = transformer["left"]
    elif "sources" in transformer:
        target_name = transformer["sources"][0]

    dataset_name = transformer["name"]

    child = Node(next(seq), dataset_name)
    leaves[target_name] = child

    return child


def generate_graph(plan: dict) -> list[Node]:
    """
    Given a plan, generate a graph of nodes.

    Args:
        plan (dict): The plan.

    Returns:
        list[Node]: The root nodes.
    """
    roots: list[Node] = []
    leaves: dict[str, Node] = {}
    seq = generate_sequence()

    for extractor in plan["extract"]:
        _, extractor = list(extractor.items())[0]

        dataset_name = extractor["name"]

        node = Node(next(seq), dataset_name)
        node.source = True
        roots.append(node)
        leaves[dataset_name] = node

    for transformer in plan.get("transform", []):
        _, transformer = list(transformer.items())[0]

        parents = _get_parents(transformer, leaves)
        child = _get_target(transformer, seq, leaves)

        for parent in parents:
            parent.children.append(child)

    for loader in plan.get("load", []):
        _, loader = list(loader.items())[0]

        dataset_name = loader["source"]
        parent = leaves[dataset_name]
        child = Node(next(seq), loader["name"])
        child.terminate = True
        parent.children.append(child)

    return roots


def graph_to_mermaid(roots: list[Node]) -> list[str]:
    """
    Given a graph of nodes, generate a mermaid diagram.

    Args:
        roots (list[Node]): The root nodes.

    Returns:
        list[str]: The mermaid diagram.
    """
    done = set()

    rows = ["graph TD"]
    Q = deque(roots)
    while Q:
        node = Q.popleft()

        for child in node.children:
            edge = (node.key, child.key)
            if edge in done:
                continue
            done.add(edge)

            if node.source:
                left = f"\t{node.key}[({node.description})]"
            else:
                left = f"\t{node.key}"

            if child.terminate:
                right = f"{child.key}[({child.description})]"
            else:
                right = f"{child.key}({child.description})"

            rows.append(f"{left} --> {right}")
            Q.append(child)

    return rows


def generate_mermaid(plan: dict, target_path: str):
    """
    Generate a mermaid diagram from the plan.

    Args:
        plan (dict): The plan.
        target_path (str): The path to save the mermaid diagram.
    """
    roots = generate_graph(plan)
    rows = graph_to_mermaid(roots)
    with open(target_path, "w") as file:
        file.write("\n".join(rows))
