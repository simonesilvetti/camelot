class Node:
    def __init__(self, name: str, mean_time: float = 1.0):
        self.name = name
        self.mean_time = mean_time
        self.incomingEdges = set()
        self.outgoingEdges = set()

    def get_name(self):
        return self.name

    def add_outgoing_edge(self, edge):
        self.outgoingEdges.add(edge)

    def get_outgoing_edges(self):
        return self.outgoingEdges

    def is_terminal(self):
        return not self.outgoingEdges

    def __eq__(self, other):
        return self.name == other.get_name() and self.mean_time == other.get_mean_time()

    def __hash__(self):
        return hash((self.name,self.mean_time))

    def __repr__(self):
        return self.name

    def get_mean_time(self):
        return self.mean_time

    def addIncomingEdge(self, edge):
        self.incomingEdges.add(edge)

    def addOutgoingEdge(self, edge):
        self.outgoingEdges.add(edge)

    def getOutGoingEdges(self):
        return self.outgoingEdges

    def isTerminal(self):
        return self.outgoingEdges == set()
