import csv

def process_file(filename):
    with open(filename, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)