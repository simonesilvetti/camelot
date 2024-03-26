from Graph import Graph
from Node import Node
from Edge import Edge

graph = Graph()

root = Node('A')
terminal = Node('T')

graph.addNode(root)
graph.addTerminal(terminal)
graph.addEdge(root, root, 0.5)
graph.addEdge(root, terminal, 0.5)

print(graph.getNode().getName())
print(graph.getTerminal().getName())


