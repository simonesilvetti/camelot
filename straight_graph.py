from simulation.edge import Edge
from simulation.graph import Graph
from simulation.node import Node
from simulation.observer import Observer
from simulation.simulator import Simulator

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

edge_1 = Edge(A, A, 0.5)
edge_2 = Edge(A, B, 0.5)
edge_3 = Edge(B, B, 0.5)
edge_4 = Edge(B, C, 0.5)
edge_5 = Edge(C, D, 1)

graph = Graph(A, [A, B, C, D], [edge_1, edge_2, edge_3, edge_4, edge_5])

simulator = Simulator(graph)
simulator.add_observer(Observer('straight.csv'))

simulator.simulate()
