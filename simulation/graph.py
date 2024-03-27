from typing import List

from simulation.edge import Edge
from simulation.node import Node


class Graph:
    def __init__(self, root: Node = None, nodes: List[Node] = None, edges: List[Edge] = None):
        self.root = root
        self.nodes = set() if nodes is None else set(nodes)
        self.edges = set() if edges is None else set(edges)
        if self.root is not None:
            self.nodes.add(self.root)

    @classmethod
    def from_list(cls, root: str, edge_list: (str, str, int)):
        dictionary_of_nodes = {root: Node(root)}
        edges = []
        for x in edge_list:
            for i in range(2):
                if x[i] not in dictionary_of_nodes:
                    dictionary_of_nodes[x[i]] = Node(x[i])
            edge = Edge(dictionary_of_nodes[x[0]], dictionary_of_nodes[x[1]], x[2])
            edges.append(edge)
        nodes = list(dictionary_of_nodes.values())
        return cls(dictionary_of_nodes[root], nodes, edges)

    def add_node(self, node: Node):
        self.nodes.add(node)
        if len(self.nodes) == 1:
            self.root = node

    def add_edge(self, edge: Edge):
        self.edges.add(edge)

    def get_root(self):
        return self.root

    def __eq__(self, other: 'Graph'):
        return self.nodes == other.nodes and self.edges == other.edges and self.root == other.root
