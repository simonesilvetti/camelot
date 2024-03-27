from simulation.edge import Edge
from simulation.graph import Graph
from simulation.node import Node


class TestGraph:

    def test_add_node(self):
        node = Node("node")
        graph = Graph()

        graph.add_node(node)

        assert graph == Graph(Node("node"))

    def test_add_edge(self):
        node_a = Node("A")
        node_b = Node("B")
        edge = Edge(node_a, node_b, 0.5)
        graph = Graph()

        graph.add_node(node_a)
        graph.add_node(node_b)
        graph.add_edge(edge)

        assert graph.edges == {Edge(node_a, node_b, 0.5)}

    def test_create_from_list(self):
        construction_list = [('A', 'B', 0.9), ('A', 'C', 0.1), ('B', 'B', 0.5), ('B', 'C', 0.5)]
        graph = Graph.from_list('A', construction_list)

        node_a = Node('A')
        node_b = Node('B')
        node_c = Node('C')
        nodes = [node_a, node_b, node_c]

        edge_a_b = Edge(node_a, node_b, 0.9)
        edge_a_c = Edge(node_a, node_c, 0.1)
        edge_b_b = Edge(node_b, node_b, 0.5)
        edge_b_c = Edge(node_b, node_c, 0.5)
        edges = [edge_a_b, edge_a_c, edge_b_b, edge_b_c]

        assert graph == Graph(node_a, nodes, edges)

