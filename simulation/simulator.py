import random
from datetime import datetime

from simulation.graph import Graph
from simulation.node import Node


class Simulator:

    def __init__(self, graph: Graph, time: datetime = datetime.now()):
        self.node = graph.get_root()
        self.time = time
        self.observers = []

    def __notify(self, node: Node, data):
        for observer in self.observers:
            observer.update(node, data)

    def add_observer(self, observer):
        self.observers.append(observer)

    def get_node(self):
        return self.node

    def __step(self):
        data = self.node.generate()
        edges = list(self.node.get_outgoing_edges())
        x = [0] * len(edges)
        x[0] = edges[0].get_score(data)
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].get_score(data)

        rand = random.uniform(0, x[-1])
        for i in range(len(x)):
            if x[i] >= rand:
                self.node = edges[i].get_son()
                return data

    def simulate(self):
        data = self.node.generate()
        self.__notify(self.node.get_name(), data)
        while not self.node.is_terminal():
            data = self.__step()
            self.__notify(self.node, data)
