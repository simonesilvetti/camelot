from simulation.node import Node


class Edge:
    def __init__(self, father: Node, son: Node, probability: float):
        self.father = father
        self.son = son
        self.probability = probability

    def get_father(self) -> Node:
        return self.father

    def get_son(self) -> Node:
        return self.son

    def get_probability(self) -> float:
        return self.probability

    def __eq__(self, __value):
        return super().__eq__(__value)


