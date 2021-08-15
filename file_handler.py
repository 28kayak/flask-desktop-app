import csv 

def calculate(csv_file):
    #allocate data as list
    data = []
    with open(csv_file, newline='') as f:
        reader = csv.reader(f)
        for row in reader: 
            data.append(row)
        print(data)
    return data
