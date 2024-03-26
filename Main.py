from Graph import Graph
from Node import Node
from Edge import Edge
from Simulator import Simulator

graph = Graph()

root = Node('A')
terminal = Node('T')

graph.addNode(root)
graph.addTerminal(terminal)
graph.addEdge(root, root, 0.9)
graph.addEdge(root, terminal, 0.1)

print(f"name of root is {graph.getNode().getName()}")
print(f" name of terminal node is {graph.getTerminal().getName()}")

simulator = Simulator(graph)

simulator.simulate()


