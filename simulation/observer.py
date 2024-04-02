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


class PatientObserver:

    def __init__(self, csv_name):
        self.csv_name = csv_name
        with open(self.csv_name, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Name", "Activity", "Hemoglobin", "Sodium", "Potassium", "Dose"])

    def update(self, node_name, node_data):
        with open(self.csv_name, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if isinstance(node_data, str):
                writer.writerow([node_data, node_name])
            else:
                writer.writerow([node_data[0], node_name, *node_data[1:-1]])
