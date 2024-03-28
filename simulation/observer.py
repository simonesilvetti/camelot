import csv


class Observer:

    def __init__(self, csv_name):
        self.csv_name = csv_name
        with open(self.csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Activity"])

    def update(self, state):
        print(state.get_node().get_name())
        with open(self.csv_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([state.get_node().get_name()])
