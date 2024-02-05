import csv

file_path = 'C:\\Users\\skupi\\Downloads\\GIT\\PYTHON\\BA\\Results.csv'

with open(file_path, 'r') as file:
    
    csv_reader = csv.reader(file)

    for row in csv_reader:
        for value in row:
            print(value, end=' ')
        print()