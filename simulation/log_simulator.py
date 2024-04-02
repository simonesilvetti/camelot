from simulation.simulator import Simulator
import random
import string


class LogSimulator:
    def __init__(self, simulator: Simulator):
        self.simulator = simulator

    def simulate(self, num_of_traces):
        for trace in range(num_of_traces):
            case_name = ''.join(random.choice(string.ascii_lowercase) for i in range(5))



