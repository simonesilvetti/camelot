from simulation.edge import ConstantScore
from examples.human_integrators.human_integrators import HigherThresholdScore, PatientObserver
from simulation.graph import Graph
from simulation.node import Node, RandomExamGenerator, RandomTimeGenerator
from simulation.simulator import Simulator

exam = Node("Exams", RandomExamGenerator())

surgery = Node("Surgery", RandomTimeGenerator(2))

pharmacological_therapy = Node("Pharmacological Therapy", RandomTimeGenerator(48))

manipulation = Node("Manipulation", RandomTimeGenerator(0.5))

recovery = Node("Recovery")

graph = Graph.from_list(exam, [(exam, surgery, HigherThresholdScore(1, 2, 3)), (exam, pharmacological_therapy, HigherThresholdScore(3, 1, 2)), (exam, manipulation, HigherThresholdScore(2, 3, 1)), (exam, recovery, HigherThresholdScore(1, 1, 1)), (surgery, exam, ConstantScore()), (pharmacological_therapy, exam, ConstantScore()), (manipulation, exam, ConstantScore())])

simulator = Simulator(graph)

simulator.add_observer((PatientObserver('output/patient.csv')))

simulator.simulate()

