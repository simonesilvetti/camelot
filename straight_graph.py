from Graph import Graph
from Node import Node
from Simulator import Simulator

graph = Graph()

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')

graph.addNode(A)
graph.addNode(B)
graph.addNode(C)
graph.addNode(D)

graph.addEdge(A, A, 0.5)
graph.addEdge(A, B, 0.5)
graph.addEdge(B, B, 0.5)
graph.addEdge(B, C, 0.5)
graph.addEdge(C, D, 1)

simulator = Simulator(graph)

simulator.simulate(A)

