from typing import List, Tuple

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
    def from_list(cls, root: str, edge_content_list: List[Tuple[str, str, int]]):
        dictionary_of_nodes = {root: Node(root)}
        edges = []
        for edge_content in edge_content_list:
            for i in range(2):
                if edge_content[i] not in dictionary_of_nodes:
                    dictionary_of_nodes[edge_content[i]] = Node(edge_content[i])
            edge = Edge(dictionary_of_nodes[edge_content[0]], dictionary_of_nodes[edge_content[1]], edge_content[2])
            edges.append(edge)
        nodes = list(dictionary_of_nodes.values())
        return cls(dictionary_of_nodes[root], nodes, edges)

    def set_root_node(self, root: Node):
        self.root = root

    def add_edge(self, edge: Edge):
        self.nodes.add(edge.get_son())
        self.nodes.add(edge.get_father())
        self.edges.add(edge)

    def get_root(self):
        return self.root

    def __eq__(self, other: 'Graph'):
        return self.nodes == other.nodes and self.edges == other.edges and self.root == other.root
