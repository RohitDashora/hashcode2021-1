#import pandas
import csv

with open ("./data/a_example") as csv_file:
    csv_reader = csv.reader(csv_file,delimiter = " ")
    for row in csv_reader:
        print(row)

