from typing import List

from simulation.edge import Edge
from simulation.node import Node


# def checkProbabilities(nodes):
#     for node in nodes:
#         p = 0
#         for edge in node.getOutGoingEdges():
#             p += edge.get_probability()
#         if p != 1:
#             print(f"Incorrect probability assignments on node {node.getName()}")
#             return False
#     return True


class Graph:
    def __init__(self, nodes: List[Node] = None, edges: List[Edge] = None):
        self.nodes = [] if nodes is None else nodes
        self.edges = [] if edges is None else edges

    def add_node(self, node: Node):
        self.nodes.append(node)

    def add_edge(self, father: Node, son: Node, probability: float):
        edge = Edge(father, son, probability)
        father = edge.get_father()
        son = edge.get_son()

        if father.addOutgoingEdge(edge):
            son.addIncomingEdge(edge)
            self.edges.append(edge)

    def __eq__(self, __value: 'Graph'):
        return self.nodes == __value.nodes and self.edges == __value.edges

class GraphFactory:

    @staticmethod
    def create_from_list(edge_list):
        pass



