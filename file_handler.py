import csv 

def calculate(csv_file):
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader: 
            print(row)