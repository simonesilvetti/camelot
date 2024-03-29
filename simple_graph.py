from simulation.edge import LinearScore
from simulation.graph import Graph
from simulation.node import Node, RandomTimeGenerator
from simulation.observer import PrintObserver, FileObserver
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

a = Node("A", RandomTimeGenerator(2))
t = Node("T", RandomTimeGenerator(2))
graph = Graph.from_list(a, [(a, a, LinearScore(30, 5)), (a, t, LinearScore(0, 6))])

simulator = Simulator(graph)
simulator.add_observer(FileObserver('output/simple.csv'))
simulator.add_observer(PrintObserver())

simulator.simulate()
