import random

from simulation.graph import Graph
from simulation.node import Node


class Simulator:

    def __init__(self, graph: Graph):
        self.node = graph.get_root()
        self.observers = []

    def notify(self, node: Node):
        for observer in self.observers:
            observer.update(node)

    def add_observer(self, observer):
        self.observers.append(observer)

    def get_node(self):
        return self.node

    def step(self):
        edges = list(self.node.get_outgoing_edges())
        x = [0] * len(edges)
        x[0] = edges[0].get_probability()
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].get_probability()

        rand = random.uniform(0, x[-1])
        for i in range(len(x)):
            if x[i] >= rand:
                self.node = edges[i].get_son()
                return

    def simulate(self):
        self.notify(self.node)
        while not self.node.is_terminal():
            self.step()
            self.notify(self.node)
