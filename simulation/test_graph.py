from simulation.edge import Edge
from simulation.graph import Graph
from simulation.node import Node


class TestGraph:

    def test_add_node(self):
        node = Node("node")
        graph = Graph()

        graph.add_node(node)

        assert graph == Graph([Node("node")])

    def test_add_edge(self):
        node_a = Node("A")
        node_b = Node("B")
        graph = Graph()

        graph.add_node(node_a)
        graph.add_node(node_b)
        graph.add_edge(node_a, node_b, 0.5)

        assert graph.edges[0] == Edge(node_a, node_b, 0.5)
