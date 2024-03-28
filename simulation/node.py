import numpy as np


class Generator:
    def generate(self):
        pass


class RandomTimeGenerator(Generator):

    def __init__(self, mean):
        self.mean = mean

    def generate(self):
        return abs(np.random.normal(loc=self.mean))

    def __hash__(self):
        return hash(self.mean)


class NoneGenerator(Generator):
    def generate(self):
        return


class Node:
    def __init__(self, name: str, generator: Generator = NoneGenerator()):
        self.name = name
        self.generator = generator
        self.outgoing_edges = set()

    def get_name(self):
        return self.name

    def add_outgoing_edge(self, edge):
        self.outgoing_edges.add(edge)

    def get_outgoing_edges(self):
        return self.outgoing_edges

    def is_terminal(self):
        return not self.outgoing_edges

    def generate(self):
        return self.generator.generate()

    def __eq__(self, other):
        return self.name == other.get_name() and self.generator == other.generator

    def __hash__(self):
        return hash((self.name, self.generator))

    def __repr__(self):
        return self.name
