from simulation.edge import Edge, LinearScore
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
        edge_1 = Edge(father, son)
        edge_2 = Edge(father, son)
        assert edge_1 == edge_2

    def test_edge_not_equals(self):
        father = Node("father")
        son_1 = Node("son1")
        son_2 = Node("son2")
        edge_1 = Edge(father, son_1)
        edge_2 = Edge(father, son_2)
        assert edge_1 != edge_2

    def test_get_probability_fixed(self):
        father = Node("father")
        son = Node("son")

        edge = Edge(father, son)

        assert 1.0 == edge.get_score(1)

    def test_get_probability_computed(self):
        father = Node("father")
        son = Node("son")
        edge = Edge(father, son, LinearScore(2, 5))
        assert edge.get_score(4) == 13

    def test(self):
        assert {LinearScore(2, 5), 2, 3} == {LinearScore(2, 5), 2, 3}
