from Edge import Edge


def checkProbabilities(nodes):
    for node in nodes:
        p = 0
        for edge in node.getOutGoingEdges():
            p += edge.getProbability()
        if p != 1:
            print(f"Incorrect probability assignments on node {node.getName()}")
            return False
    return True

class Graph:
    def __init__(self, nodes, edges):
        if checkProbabilities(nodes):
            self.nodes = nodes
            self.edges = edges

    def addNode(self, node):
        self.nodes.append(node)

    def addEdge(self, father, son, probability):
        edge = Edge(father, son, probability)
        father = edge.getFather()
        son = edge.getSon()

        if father.addOutgoingEdge(edge):
            son.addIncomingEdge(edge)
            self.edges.append(edge)
