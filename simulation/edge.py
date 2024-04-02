from simulation.node import Node
import numpy as np


class Score:
    def score(self, data) -> float:
        pass


class LinearScore(Score):
    def __init__(self, m: float, q: float):
        self.m = m
        self.q = q

    def score(self, data) -> float:
        return self.m * data + self.q

    def __eq__(self, other):
        return self.m == other.m and self.q == other.q

    def __hash__(self):
        return hash((self.m, self.q))


"""""
class ExamScore(Score):
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def score(self, data) -> float:
        return self.x * data[1] + self.y * data[2] + self.z * data[3]

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self):
        return hash((self.x, self.y, self.z))
"""


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
    def score(self,data):
        if data[-1]:
            return 0
        else:
            return np.inf


class ConstantScore(Score):

    def score(self, data) -> float:
        return 1

    def __eq__(self, __value):
        return True

    def __hash__(self):
        return hash(1)


class Edge:
    def __init__(self, father: Node, son: Node, score: Score = ConstantScore()):
        self.father = father
        self.son = son
        self.score = score
        self.father.add_outgoing_edge(self)

    def __eq__(self, other):
        return self.father == other.get_father() and self.son == other.get_son() and self.score == other.score

    def get_father(self) -> Node:
        return self.father

    def get_son(self) -> Node:
        return self.son

    def get_score(self, data) -> float:
        return self.score.score(data)

    def __hash__(self):
        return hash((self.father, self.son, self.score))
