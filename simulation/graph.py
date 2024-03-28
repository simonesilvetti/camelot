from typing import List, Tuple

from simulation.edge import Edge, Score
from simulation.node import Node


class Graph:
    def __init__(self, root: Node = None, edges: List[Edge] = None):
        self.root = root
        self.edges = set() if edges is None else set(edges)

    @classmethod
    def from_list(cls, root: Node, edge_content_list: List[Tuple[Node, Node, Score]]):
        edges = []
        for father, son, score in edge_content_list:
            edges.append(Edge(father, son, score))
        return cls(root, edges)

    def set_root_node(self, root: Node):
        self.root = root

    def add_edge(self, edge: Edge):
        self.edges.add(edge)

    def get_root(self):
        return self.root

    def __eq__(self, other: 'Graph'):
        return self.edges == other.edges and self.root == other.root
