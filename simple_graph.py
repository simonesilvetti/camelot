from simulation.graph import Graph
from simulation.observer import Observer
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
graph = Graph.from_list('A', [('A', 'A', 5), ('A', 'T', 1)])

simulator = Simulator(graph)
simulator.add_observer(Observer('simple.csv'))

simulator.simulate()
