import csv


class FileObserver:

    def __init__(self, csv_name):
        self.csv_name = csv_name
        with open(self.csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Activity"])

    def update(self, node):
        node = node.get_name()
        with open(self.csv_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([node])


class PrintObserver:

    def update(self, node):
        print(node)
