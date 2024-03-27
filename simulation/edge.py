from simulation.node import Node


class Edge:
    def __init__(self, father: Node, son: Node, probability: float):
        self.father = father
        self.son = son
        self.probability = probability

    def __eq__(self, other):
        return self.get_father() == other.get_father() and self.get_son() == other.get_son() and self.get_probability() == other.get_probability()

    def get_father(self) -> Node:
        return self.father

    def get_son(self) -> Node:
        return self.son

    def get_probability(self) -> float:
        return self.probability




