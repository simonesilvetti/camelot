from typing import List, Tuple

from simulation.edge import Edge
from simulation.node import Node


class Graph:
    def __init__(self, root: Node = None, edges: List[Edge] = None):
        self.root = root
        self.edges = set() if edges is None else set(edges)

    @classmethod
    def from_list(cls, root: str, edge_content_list: List[Tuple[str, str, float, float]]):
        dictionary_of_nodes = {root: Node(root)}
        edges = []
        for edge_content in edge_content_list:
            for i in range(2):
                if edge_content[i] not in dictionary_of_nodes:
                    dictionary_of_nodes[edge_content[i]] = Node(edge_content[i])
            edge = Edge(dictionary_of_nodes[edge_content[0]], dictionary_of_nodes[edge_content[1]], edge_content[2], edge_content[3])
            edges.append(edge)
        return cls(dictionary_of_nodes[root], edges)

    def set_root_node(self, root: Node):
        self.root = root

    def add_edge(self, edge: Edge):
        self.edges.add(edge)

    def get_root(self):
        return self.root

    def __eq__(self, other: 'Graph'):
        return self.edges == other.edges and self.root == other.root
