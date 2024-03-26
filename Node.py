class Node:
    def __init__(self, name):
        self.name = name
        self.incomingEdges = []
        self.outgoingEdges = []
        self.outgoingProbabilities = 0

    def __eq__(self,other):
        return self.getName() == other.getName()

    def getName(self):
        return self.name

    def addIncomingEdge(self, edge):
        self.incomingEdges.append(edge)

    def addOutgoingEdge(self, edge):
        probability = edge.getProbability()
        if self.outgoingProbabilities + probability <= 1:
            self.outgoingEdges.append(edge)
            self.outgoingProbabilities += probability
            return True

        return False

    def getOutGoingEdges(self):
        return self.outgoingEdges
