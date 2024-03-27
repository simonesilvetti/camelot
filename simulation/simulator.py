import random

from simulation.graph import Graph


class Simulator:

    def __init__(self, graph: Graph):
        self.graph = graph

    def step(self, node):
        edges = node.getOutGoingEdges()
        x = [0] * len(edges)
        x[0] = edges[0].get_probability()
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].get_probability()

        rand = random.uniform(0, x[-1])
        for i in range(len(x)):
            if x[i] >= rand:
                return edges[i].get_son()

    def simulate(self):
        state = self.graph.get_root()
        print(state.getName())
        while not state.isTerminal():
            state = self.step(state)
            print(state.getName())
        print("simulation ended")
