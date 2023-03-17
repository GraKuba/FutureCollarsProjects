# IMPORTS 
import sys
import pickle
import csv
import json

# FILE PATH FOR THE DOWNLOAD
file = '/Users/kubagrabarczyk/Desktop/python recap/input.csv'
tempData = []
with open(file, 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(' '.join(line))
    for line in reader:
        tempData.append(line)


# output = "/Users/kubagrabarczyk/Desktop/python recap/output.csv"
# with open(output, 'w') as f:
#     writer = csv.writer(f)
#     for line in tempData:
#         writer.writerow(line)
