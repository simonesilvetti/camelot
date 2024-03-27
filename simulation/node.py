class Node:
    def __init__(self, name : str):
        self.name = name
        self.incomingEdges = []
        self.outgoingEdges = []

    def __eq__(self, other):
        return self.get_name() == other.get_name()

    def __hash__(self):
        return hash(self.name)

    def get_name(self):
        return self.name

    def addIncomingEdge(self, edge):
        self.incomingEdges.append(edge)

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.append(edge)

    def getOutGoingEdges(self):
        return self.outgoingEdges

    def isTerminal(self):
        return not self.outgoingEdges
