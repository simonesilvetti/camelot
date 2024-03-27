import random

from simulation.graph import Graph
from simulation.observer import Observer


class Simulator:
    
    observer = Observer()

    def __init__(self, graph: Graph):
        self.graph = graph
        self.state = graph.get_root()
        
    def notify(self):
        self.observer.update(self.state)

    def step(self):
        edges = list(self.state.getOutGoingEdges())
        x = [0] * len(edges)
        x[0] = edges[0].get_probability()
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].get_probability()

        rand = random.uniform(0, x[-1])
        for i in range(len(x)):
            if x[i] >= rand:
                return edges[i].get_son()

    def simulate(self):
        self.notify()
        while not self.state.isTerminal():
            self.state = self.step()
            self.notify()
        print("simulation ended")
