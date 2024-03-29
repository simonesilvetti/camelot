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


"""
class RandomExamGenerator(Generator):

    def generate(self):
        return 1, abs(np.random.normal()), abs(np.random.normal()), abs(np.random.normal())

    def __hash__(self):
        return 1
"""


class Human(Generator):

    def __init__(self, hemo, sodium, pot):
        self.hemo = hemo
        self.sodium = sodium
        self.pot = pot

    def generate(self):
        return self.hemo, self.sodium, self.pot

    def update(self, node_name, node_data):
        match node_name:
            case "hemo_int":
                self.hemo += 0.5 * node_data
            case "hemo_inib":
                self.hemo -= 0.5 * node_data
            case "sodium_int":
                self.sodium += 0.5 * node_data
            case "sodium_inib":
                self.sodium -= 0.5 * node_data
            case "pot_int":
                self.pot += 0.5 * node_data
            case "pot_inib":
                self.pot -= 0.5 * node_data


class CorrectorGenerator(Generator):
    def generate(self):
        return self.name, self.value

    def __init__(self, name, value):
        self.name = name
        self.value = value


class RandomExamGenerator(Generator):

    def generate(self):
        return 1, abs(np.random.normal(14.9)), abs(np.random.normal(140)), abs(np.random.normal(4.5))

    def __hash__(self):
        return 1


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
