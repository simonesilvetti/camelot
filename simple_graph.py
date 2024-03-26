from Graph import Graph
from Node import Node
from Simulator import Simulator

graph = Graph()

root = Node('A')
terminal = Node('T')

graph.addNode(root)
graph.addNode(terminal)
graph.addEdge(root, root, 0.1)
graph.addEdge(root, terminal, 0.9)

simulator = Simulator(graph)

simulator.simulate(root)


