from simulation.node import Node


class Edge:
    def __init__(self, father: Node, son: Node, q=1, m=0):
        self.father = father
        self.son = son
        self.m = m
        self.q = q
        self.father.addOutgoingEdge(self)
        self.son.addIncomingEdge(self)

    def __eq__(self, other):
        return self.get_father() == other.get_father() and self.get_son() == other.get_son() and self.get_probability() == other.get_probability()

    def get_father(self) -> Node:
        return self.father

    def get_son(self) -> Node:
        return self.son


    def get_probability(self, time=0) -> float:
        return self.m*time + self.q

    def __hash__(self):
        return hash((self.father, self.son, self.m,self.q))




