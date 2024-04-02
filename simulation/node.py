import numpy as np


class Human:
    def __init__(self, name: str):
        self.name = name
        self.hemo = abs(np.random.normal(14.9, 5))
        self.sodium = abs(np.random.normal(140, 5))
        self.pot = abs(np.random.normal(4.5, 5))

        self.hemo_int_count = 0
        self.hemo_inib_count = 0
        self.sodium_int_count = 0
        self.sodium_inib_count = 0
        self.pot_int_count = 0
        self.pot_inib_count = 0

        self.dose=0

    def take_drug(self, name, diff):
        match name:
            case "hemo_int":
                self.dose = (1 / (1 + self.hemo_int_count)) * diff
                self.hemo += self.dose
                self.hemo_int_count += 1
            case "hemo_inib":
                self.dose = (1 / (1 + self.hemo_inib_count)) * diff
                self.hemo -= self.dose
                self.hemo_inib_count += 1
            case "sodium_int":
                self.dose = (1 / (1 + self.sodium_int_count)) * diff
                self.sodium += self.dose
                self.sodium_int_count += 1
            case "sodium_inib":
                self.dose =  (1 / (1 + self.sodium_inib_count)) * diff
                self.sodium -= self.dose
                self.sodium_inib_count += 1
            case "pot_int":
                self.dose =  (1 / (1 + self.pot_int_count)) * diff
                self.pot += self.dose
                self.pot_int_count += 1
            case "pot_inib":
                self.dose = (0.5 / (1 + self.pot_inib_count)) * diff
                self.pot -= self.dose
                self.pot_inib_count += 1

    def is_responsive(self):
        if self.hemo_int_count >= 10 or self.hemo_inib_count >= 10 or self.sodium_int_count >= 10 or self.sodium_inib_count >= 10 or self.pot_int_count >= 10 or self.pot_inib_count >= 10:
            return False
        else:
            return True

    def get_name(self):
        return self.name

    def get_hemo(self):
        return self.hemo

    def get_sodium(self):
        return self.sodium

    def get_pot(self):
        return self.pot

    def get_dose(self):
        return self.dose


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

""""
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

"""


class NoneGenerator(Generator):
    def __init__(self, case):
        self.case = case

    def generate(self):
        return self.case.get_name()


class DrugGenerator(Generator):
    def __init__(self, human):
        self.human = human

    def generate(self):
        return self.human.get_name(), None, None, None, self.human.get_dose(), None


class Exam(Generator):
    def __init__(self, human: Human):
        self.human = human

    def generate(self):
        return self.human.get_name(), self.human.get_hemo(), self.human.get_sodium(), self.human.get_pot(), None, self.human.is_responsive()


class Updater:
    def update(self):
        pass


class NoneUpdater(Updater):
    def update(self):
        return


class HemoIntegrator(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        low_threshold = 13.2
        diff = np.clip(low_threshold - self.human.get_hemo(), 0, np.inf)
        self.human.take_drug('hemo_int', diff)


class HemoInibitor(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        high_threshold = 16.6
        diff = np.clip(self.human.get_hemo() - high_threshold, 0, np.inf)
        self.human.take_drug('hemo_inib', diff)


class SodiumIntegrator(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        low_threshold = 135
        diff = np.clip(low_threshold - self.human.get_sodium(), 0, np.inf)
        self.human.take_drug('sodium_int', diff)


class SodiumInibitor(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        high_threshold = 145
        diff = np.clip(self.human.get_sodium() - high_threshold, 0, np.inf)
        self.human.take_drug('sodium_inib', diff)


class PotIntegrator(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        low_threshold = 3.5
        diff = np.clip(low_threshold - self.human.get_pot(), 0, np.inf)
        self.human.take_drug('pot_int', diff)


class PotInibitor(Updater):
    def __init__(self, human: Human):
        self.human = human

    def update(self):
        high_threshold = 5.5
        diff = np.clip(self.human.get_pot() - high_threshold, 0, np.inf)
        self.human.take_drug('pot_inib', diff)


class Node:
    def __init__(self, name: str, generator: Generator, updater: Updater = NoneUpdater()):
        self.name = name
        self.generator = generator
        self.updater = updater
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

    def update(self):
        self.updater.update()

    def __eq__(self, other):
        return self.name == other.get_name() and self.generator == other.generator

    def __hash__(self):
        return hash((self.name, self.generator))

    def __repr__(self):
        return self.name
