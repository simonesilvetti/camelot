from Edge import Edge

class Graph:
    def __init__(self):
        self.node = None
        self.terminal = None
        self.edges = []

    def addNode(self, node):
        self.node = node

    def addTerminal(self, node):
        self.terminal = node

    def addEdge(self, father, son, probability):
        edge = Edge(father, son, probability)
        father = edge.getFather()
        son = edge.getSon()

        if father.addOutgoingEdge(edge):
            son.addIncomingEdge(edge)
            self.edges.append(edge)

    def getNode(self):
        return self.node

    def getTerminal(self):
        return self.terminal
