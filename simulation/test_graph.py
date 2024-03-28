from simulation.edge import Edge, ConstantScore
from simulation.graph import Graph
from simulation.node import Node


class TestGraph:

    def test_add_edge(self):
        node_a = Node("A")
        node_b = Node("B")
        edge = Edge(node_a, node_b, 0.5)
        graph = Graph()

        graph.add_edge(edge)

        assert graph.edges == {Edge(node_a, node_b, 0.5)}

    def test_create_from_list(self):
        node_a = Node('A')
        node_b = Node('B')
        node_c = Node('C')
        construction_list = [(node_a, node_b, ConstantScore()), (node_a, node_c, ConstantScore())]

        graph = Graph.from_list(node_a, construction_list)

        edge_a_b = Edge(node_a, node_b)
        edge_a_c = Edge(node_a, node_c)
        edges = [edge_a_b, edge_a_c]
        assert graph == Graph(node_a, edges)
