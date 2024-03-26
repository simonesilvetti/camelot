from simulation.graph import Graph
from simulation.node import Node
from simulation.simulator import Simulator

graph = Graph()

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

graph.add_node(A)
graph.add_node(B)
graph.add_node(C)
graph.add_node(D)

graph.add_edge(A, A, 0.5)
graph.add_edge(A, B, 0.5)
graph.add_edge(B, B, 0.5)
graph.add_edge(B, C, 0.5)
graph.add_edge(C, D, 1)

simulator = Simulator(graph)

simulator.simulate(A)

