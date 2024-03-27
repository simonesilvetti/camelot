from simulation.edge import Edge
from simulation.graph import Graph
from simulation.node import Node
from simulation.simulator import Simulator

""""
root = Node('A')
terminal = Node('T')
nodes = [root, terminal]

edges = [Edge(root, root, 0.5), Edge(root, terminal, 0.5)]

graph = Graph(nodes, edges)

simulator = Simulator(graph)

simulator.simulate(root)
"""
root = Node('A')
graph = Graph.from_list([('A', 'A', 0.5), ('A', 'T', 0.5)])

simulator = Simulator(graph)
simulator.simulate()
