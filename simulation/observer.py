import csv


class FileObserver:

    def __init__(self, csv_name):
        self.csv_name = csv_name
        with open(self.csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Activity", "Time"])

    def update(self, node_name, node_data):
        with open(self.csv_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([node_name, node_data])


class PrintObserver:

    def update(self, node_name, node_data):
        print(f"Node {node_name} with data {node_data}")



class DataCollector:

    def __init__(self, column_names):
        self.column_names = column_names
        self.data = []

    def update(self, node_name, node_data):
        self.data.append([node_name, *node_data])

    def to_csv(self, csv_name):
        with open(csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.column_names)
            writer.writerows(self.data)
