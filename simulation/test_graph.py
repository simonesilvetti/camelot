from simulation.graph import Graph
from simulation.node import Node


def test_add_node():
    node = Node("node")
    graph = Graph()

    graph.add_node(node)

    assert graph == Graph([Node("node")])


def test_add_edge():
    node = Node("node")
    graph = Graph()

    graph.add_node(node)

    assert graph == Graph([Node("node")])
