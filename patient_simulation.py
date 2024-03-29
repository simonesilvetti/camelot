from simulation.edge import ExamScore, ConstantScore
from simulation.graph import Graph
from simulation.node import Node, RandomExamGenerator, RandomTimeGenerator
from simulation.observer import PatientObserver
from simulation.simulator import Simulator

exam = Node("Exams", RandomExamGenerator())

surgery = Node("Surgery", RandomTimeGenerator(2))

pharmacological_therapy = Node("Pharmacological Therapy", RandomTimeGenerator(48))

manipulation = Node("Manipulation", RandomTimeGenerator(0.5))

recovery = Node("Recovery")

graph = Graph.from_list(exam, [(exam, surgery, ExamScore(1, 2, 3)), (exam, pharmacological_therapy, ExamScore(3, 1, 2)), (exam, manipulation, ExamScore(2, 3, 1)),(exam, recovery, ExamScore(1, 1, 1)), (surgery, exam, ConstantScore()), (pharmacological_therapy, exam, ConstantScore()), (manipulation, exam, ConstantScore())])

simulator = Simulator(graph)

simulator.add_observer((PatientObserver('output/patient.csv')))

simulator.simulate()

