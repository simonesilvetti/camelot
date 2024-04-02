from simulation.edge import LowerThresholdScore, HigherThresholdScore, ConstantScore, RecoveredScore, NonResponsiveScore
from simulation.graph import Graph
from simulation.node import Node, Human, Exam, NoneUpdater, HemoIntegrator, NoneGenerator, HemoInibitor, \
    SodiumIntegrator, SodiumInibitor, PotIntegrator, PotInibitor, DrugGenerator

from simulation.observer import PatientObserver
from simulation.simulator import Simulator

observer = PatientObserver('output/integrators_log.csv')


for i in range(1000):
    human = Human(str(i))

    exam = Node("Exam", Exam(human), NoneUpdater())

    hemo_int = Node("hemo_int", DrugGenerator(human), HemoIntegrator(human))
    hemo_inib = Node("hemo_nib", DrugGenerator(human), HemoInibitor(human))
    sodium_int = Node("sodium_int", DrugGenerator(human), SodiumIntegrator(human))
    sodium_inib = Node("sodium_inib", DrugGenerator(human), SodiumInibitor(human))
    pot_int = Node("pot_int", DrugGenerator(human), PotIntegrator(human))
    pot_inib = Node("pot_inib", DrugGenerator(human), PotInibitor(human))

    recovered = Node("recovered", NoneGenerator(human), NoneUpdater())

    non_responsive = Node("Non responsive", NoneGenerator(human), NoneUpdater())

    edge_list = [(exam, hemo_int, LowerThresholdScore(13.2, 1)), (exam, hemo_inib, HigherThresholdScore(16.6, 1)),
                 (exam, sodium_int, LowerThresholdScore(135, 2)), (exam, sodium_inib, HigherThresholdScore(145, 2)),
                 (exam, pot_int, LowerThresholdScore(3.5, 3)), (exam, pot_inib, HigherThresholdScore(5.5, 3)),
                 (hemo_int, exam, ConstantScore()), (hemo_inib, exam, ConstantScore()),
                 (sodium_int, exam, ConstantScore()),
                 (sodium_inib, exam, ConstantScore()), (pot_int, exam, ConstantScore()),
                 (pot_inib, exam, ConstantScore()),
                 (exam, recovered, RecoveredScore()), (exam, non_responsive, NonResponsiveScore())]

    graph = Graph.from_list(exam, edge_list)

    simulator = Simulator(graph)

    simulator.add_observer(observer)

    simulator.simulate()
