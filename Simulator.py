import random
import numpy as np
from Graph import Graph
from Node import Node


class Simulator:

    def __init__(self,graph):
        self.graph = graph

    def addNode(self, name):
        self.graph.addNode(Node(name))

    def addEdge(self, father, son, probability):
        self.graph.addEdge(father, son, probability)

    def step(self, node):
        edges = node.getOutGoingEdges()
        x = [0] * len(edges)
        x[0] = edges[0].getProbability()
        for i in range(1, len(x)):
            x[i] = x[i - 1] + edges[i].getProbability()

        rand = random.uniform(0, 1)
        for i in range(len(x)):
            if x[i] >= rand:
                return edges[i].getSon()

    def simulate(self,start):
        state = start
        print(state.getName())
        while not state.isTerminal():
            state = self.step(state)
            print(state.getName())
        print("simulation ended")
