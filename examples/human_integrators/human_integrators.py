import csv

import numpy as np

from simulation.edge import Score
from simulation.node import Generator, Updater


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

        self.dose = 0

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
                self.dose = (1 / (1 + self.sodium_inib_count)) * diff
                self.sodium -= self.dose
                self.sodium_inib_count += 1
            case "pot_int":
                self.dose = (1 / (1 + self.pot_int_count)) * diff
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


class DrugGenerator(Generator):
    def __init__(self, human: Human):
        self.human = human

    def generate(self):
        return self.human.get_name(), None, None, None, self.human.get_dose(), None


class Exam(Generator):
    def __init__(self, human: Human):
        self.human = human

    def generate(self):
        return self.human.get_name(), self.human.get_hemo(), self.human.get_sodium(), self.human.get_pot(), None, self.human.is_responsive()


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


class HigherThresholdScore(Score):
    def __init__(self, threshold: float, index: int):
        self.index = index
        self.threshold = threshold

    def score(self, data) -> float:
        return np.clip(data[self.index] - self.threshold, 0, np.inf)

    def __eq__(self, other):
        return self.threshold == other.threshold

    def __hash__(self):
        return hash(self.threshold)


class LowerThresholdScore(Score):
    def __init__(self, threshold: float, index: int):
        self.index = index
        self.threshold = threshold

    def score(self, data) -> float:
        return np.clip(self.threshold - data[self.index], 0, np.inf)

    def __eq__(self, other):
        return self.threshold == other.threshold

    def __hash__(self):
        return hash(self.threshold)


class RecoveredScore(Score):
    def score(self, data):
        if 13.2 <= data[1] <= 16.6 and 135 <= data[2] <= 145 and 3.5 <= data[3] <= 5.5:
            return 1
        else:
            return 0


class NonResponsiveScore(Score):
    def score(self, data):
        if data[-1]:
            return 0
        else:
            return np.inf


class PatientObserver:

    def __init__(self, csv_name):
        self.csv_name = csv_name
        with open(self.csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Activity", "Hemoglobin", "Sodium", "Potassium", "Dose"])

    def update(self, node_name, node_data):
        with open(self.csv_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([node_data[0], node_name, *node_data[1:-1]])
