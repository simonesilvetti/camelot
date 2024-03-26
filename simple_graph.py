from Edge import Edge
from Graph import Graph
from Node import Node
from Simulator import Simulator

root = Node('A')
terminal = Node('T')
nodes = [root, terminal]

edges = [Edge(root, root, 0.1), Edge(root, terminal, 0.9)]

graph = Graph(nodes, edges)

simulator = Simulator(graph)

simulator.simulate(root)
