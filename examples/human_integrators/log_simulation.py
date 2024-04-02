import numpy as np

from examples.human_integrators.human_integrators import Human, DrugGenerator, Exam, HemoIntegrator, HemoInibitor, \
    SodiumIntegrator, SodiumInibitor, PotIntegrator, PotInibitor, HigherThresholdScore, LowerThresholdScore, \
    RecoveredScore, NonResponsiveScore
from simulation.edge import ConstantScore
from simulation.graph import Graph
from simulation.node import Node, NoneUpdater, NoneGenerator, TimedGenerator
from simulation.observer import DataCollector
from simulation.simulator import Simulator

data_collector = DataCollector(["Activity", "Case ID", "Hemoglobin", "Sodium", "Potassium", "Dose"])

for i in range(100):
    human = Human(str(i))

    exam = Node("Exam", TimedGenerator(Exam(human), lambda: np.random.normal(loc=1)), NoneUpdater())

    hemo_int = Node("hemo_int", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                    HemoIntegrator(human))
    hemo_inib = Node("hemo_nib", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                     HemoInibitor(human))
    sodium_int = Node("sodium_int", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                      SodiumIntegrator(human))
    sodium_inib = Node("sodium_inib", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                       SodiumInibitor(human))
    pot_int = Node("pot_int", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                   PotIntegrator(human))
    pot_inib = Node("pot_inib", TimedGenerator(DrugGenerator(human), lambda: np.random.normal(loc=48)),
                    PotInibitor(human))

    recovered = Node("recovered", TimedGenerator(NoneGenerator(human), lambda: 0), NoneUpdater())

    non_responsive = Node("Non responsive", TimedGenerator(NoneGenerator(human), lambda: 0), NoneUpdater())

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

    simulator.add_observer(data_collector)

    simulator.simulate()
data_collector.to_csv('integrators_log.csv')
