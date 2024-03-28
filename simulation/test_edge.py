from simulation.edge import Edge
from simulation.node import Node


class TestEdge:

    def test_get_father(self):
        father = Node("father")
        son = Node("son")

        edge = Edge(father, son, 1.0)

        assert edge.get_father() == father

    def test_get_son(self):
        father = Node("father")
        son = Node("son")

        edge = Edge(father, son, 1.0)

        assert edge.get_son() == son



    def test_edge_equals(self):
        father = Node("father")
        son = Node("son")
        edge_1 = Edge(father, son, 0.5)
        edge_2 = Edge(father, son, 0.5)
        assert edge_1 == edge_2

    def test_edge_not_equals(self):
        father = Node("father")
        son_1 = Node("son1")
        son_2 = Node("son2")
        edge_1 = Edge(father, son_1, 0.5)
        edge_2 = Edge(father, son_2, 0.5)
        assert edge_1 != edge_2

    def test_get_probability_fixed(self):
        father = Node("father")
        son = Node("son")

        edge = Edge(father, son, 1.0)

        assert 1.0 == edge.get_probability()

    def test_get_probability_computed(self):
        father = Node("father")
        son = Node("son")
        edge = Edge(father, son, 5, 2)
        assert edge.get_probability(4) == 13

