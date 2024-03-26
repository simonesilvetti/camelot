class Edge:
    def __init__(self, father, son, probability):
        self.father = father
        self.son = son
        self.probability = probability

    def getFather(self):
        return self.father

    def getSon(self):
        return self.son

    def getProbability(self):
        return self.probability

