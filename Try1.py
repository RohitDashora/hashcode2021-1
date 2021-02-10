#import pandas
import csv
import re
import pandas as pd
import numpy as nm

biglist=[]
pizzas= []

# Split the input file into two - Rohit
# Find number of Unique ingredients - Manisha 
    # We just need number not actual ingridentss
    # use a data structure to hold this data (dataframe)
# produce one file per team type with pizza this can be validated 
# Combinations` -
    # Compute all possible combinations where we can give each team closest number of ingridents to the max-
        # geerate pizza ids (sort by max ingredients)
        # List of Lists - with pop + a running counter + a dict with kes as team and vlaues as pizza ids 
#scoring Module 
    #find max ingridents per team 
    # score
    #produce ourput file


# with open ("./data/a_example", 'r') as csv_file:
#     header=csv_file.readline()
#     #next(csv_file)
#     for row in csv_file:
#         row = row.rstrip("\n")
#         li = list(row.split(" ")) 
#         li.pop(0)
#         biglist= biglist+li
#         pizzas.append(li)
# print(biglist)
# print(pizzas)
# print(header)
# biglist = list(dict.fromkeys(biglist))
# print(biglist)


#data = pd.read_csv("./data/a_example", sep=' ', index_col=0, keep_default_na=False)
#its for file with less data
data = pd.read_csv("./data/a_example", sep=' ', index_col=0,error_bad_lines=False)

# print(data[1].value_counts())
narray = nm.array(data)

print(narray)

df = pd.DataFrame(narray.ravel())

#count of unique value
print(df[0].nunique())
