from simulation.edge import Edge
from simulation.node import Node


class TestEdge:

    def set_up(self):
        self.node = Node("A")

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

    def test_get_probability(self):
        father = Node("father")
        son = Node("son")

        edge = Edge(father, son, 1.0)

        assert 1.0 == edge.get_probability()
