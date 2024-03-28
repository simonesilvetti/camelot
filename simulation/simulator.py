from datetime import datetime, timedelta

import random
import numpy as np

from simulation.graph import Graph
from simulation.node import Node


class Simulator:
    observer = Observer()

    def __init__(self, graph: Graph, time: datetime = datetime.now()):
        self.node = graph.get_root()
        self.time = time
        self.observers = []

    def notify(self, node: Node):
        for observer in self.observers:
            observer.update(node, self.time)

    def add_observer(self, observer):
        self.observers.append(observer)

    def get_node(self):
        return self.node

    def step(self):
        time_elapsed = abs(np.random.normal(loc=1.0))
        self.time += timedelta(hours=time_elapsed)
        edges = list(self.node.get_outgoing_edges())
        x = [0] * len(edges)
        x[0] = edges[0].get_probability(time_elapsed)
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].get_probability(time_elapsed)

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
