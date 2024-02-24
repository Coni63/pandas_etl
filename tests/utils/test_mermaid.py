from __future__ import annotations

from pandas_etl.utils.mermaid import generate_graph
from pandas_etl.utils.mermaid import generate_sequence
from pandas_etl.utils.mermaid import graph_to_mermaid


TEST_PLAN = {
    "extract": [
        {"source1": {"name": "A"}},
        {"source2": {"name": "B"}},
    ],
    "transform": [
        # transformation with target
        {"transformer1": {"source": "A", "target": "C", "name": "A-C"}},
        {"transformer1": {"source": "A", "target": "F", "name": "A-F"}},
        # transformation without target
        {"transformer2": {"source": "B", "name": "B-B"}},
        # transformation with left and right and target
        {"transformer3": {"left": "C", "right": "B", "target": "E", "name": "BC-E"}},
        # transformation with left and right without target
        {"transformer3": {"left": "E", "right": "C", "name": "EC-E"}},
        # transformation with sources
        {"transformer4": {"sources": ["E", "F"], "target": "G", "name": "EF-G"}},
        # transformation with sources without target
        {"transformer5": {"sources": ["G", "F"], "name": "GF-G"}},
    ],
    "load": [
        {"loader1": {"source": "G", "name": "save G"}},
        {"loader2": {"source": "C", "name": "save C"}},
    ],
}


def test_generate_sequence():
    seq = generate_sequence()
    assert next(seq) == "A"
    assert next(seq) == "B"

    while next(seq) != "Z":
        pass

    assert next(seq) == "AA"
    assert next(seq) == "AB"

    while next(seq) != "AZ":
        pass

    assert next(seq) == "BA"
    assert next(seq) == "BB"


def test_generate_graph():
    graph = generate_graph(TEST_PLAN)
    assert len(graph) == 2
    assert len(graph[0].children) == 2
    assert len(graph[0].children[1].children) == 2


def test_graph_to_mermaid():
    graph = generate_graph(TEST_PLAN)
    mermaid = graph_to_mermaid(graph)
    assert len(mermaid) == 14
    assert mermaid[0] == "graph TD"
    assert mermaid[1] == "	A[(A)] --> C(A-C)"  # loader node
    assert mermaid[3] == "	B[(B)] --> E(B-B)"  # transfer node
    assert mermaid[6] == "	C --> K[(save C)]"  # saver node
