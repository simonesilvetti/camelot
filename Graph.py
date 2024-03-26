from Edge import Edge


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, father, son, probability):
        edge = Edge(father, son, probability)
        father = edge.getFather()
        son = edge.getSon()

        if father.addOutgoingEdge(edge):
            son.addIncomingEdge(edge)
            self.edges.append(edge)
