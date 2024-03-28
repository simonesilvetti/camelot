class Node:
    def __init__(self, name: str):
        self.name = name
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
        return self.get_name() == other.get_name()

    def __hash__(self):
        return hash(self.name)

    def __repr__(self):
        return self.name
