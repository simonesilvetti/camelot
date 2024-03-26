from simulation.edge import Edge
from simulation.graph import Graph
from simulation.node import Node
from simulation.simulator import Simulator

root = Node('A')
terminal = Node('T')
nodes = [root, terminal]

edges = [Edge(root, root, 0.1), Edge(root, terminal, 0.9)]

graph = Graph(nodes, edges)

simulator = Simulator(graph)

simulator.simulate(root)
