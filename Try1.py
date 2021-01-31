#import pandas
import csv
import re

biglist=[]
pizzas= []

with open ("./data/a_example", 'r') as csv_file:
    #data = csv_file.read().replace('\n', '')
    header=csv_file.readline()
    next(csv_file)
    for row in csv_file:
        row = row.rstrip("\n")
        li = list(row.split(" ")) 
        li.pop(0)
        biglist= biglist+li
        pizzas.append(li)
print(biglist)
print(pizzas)
print(header)
biglist = list(dict.fromkeys(biglist))
print(biglist)
