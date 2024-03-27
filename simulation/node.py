class Node:
    def __init__(self, name : str):
        self.name = name
        self.incomingEdges = []
        self.outgoingEdges = []

    def __eq__(self, other):
        return self.getName() == other.getName()

    def __hash__(self):
        return hash(self.name)

    def getName(self):
        return self.name

    def addIncomingEdge(self, edge):
        self.incomingEdges.append(edge)

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.append(edge)

    def getOutGoingEdges(self):
        return self.outgoingEdges

    def isTerminal(self):
        return not self.outgoingEdges
