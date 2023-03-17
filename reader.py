# IMPORTS 
import sys
import pickle
import csv
import json

# FILE PATH FOR THE DATA DOWNLOAD AND ESSENTIAL CLASSES
file = '/Users/kubagrabarczyk/Desktop/python recap/input.csv'

class Manager:
    def __init__(self, inFile, outFile, name):
        self.inFile = inFile
        self.outFile = outFile
        self.name = name

    def downloadFile(self): # OPEN THE FILE AND DOWNLOAD ALL DATA
        with open(self.inFile, 'r') as f:
            tempData = []
            reader = csv.reader(f)
            for line in reader:
                tempData.append(line) 
        return tempData

    def writeFile(self, data,b= None):
        with open(self.outFile, 'w'+b) as f:
            if self.name == 'json' or 'pickle':
                self.name.dump(data, f)
            else:
                writer = csv.writer(f)
                for line in data:
                    writer.writerow(line) 

    def fileChange(self, data):
        for command in data:
            data[command[2][command[3] = command[4]
        return data 


if len(sys.argv) > 1: # DOWNLOAD CHANGES FROM THE CONSOLE
    i = 0
    changesList = []
    changes = []
    for item in sys.argv:
        i += 1
        if i > 1:
            changes.append(item)
            if len(changes) == 5:
                changesList.append(changes)
                changes = []

        

with open(file, 'r') as f:
    tempData = []
    reader = csv.reader(f)
    for line in reader:
        tempData.append(line)
# PRINT OUT INPUT.CSV CONTENTS ONTO THE CONSOLE
    for line in reader:
        print(' '.join(line))



# output = "/Users/kubagrabarczyk/Desktop/python recap/output.csv"
# with open(output, 'w') as f:
#     writer = csv.writer(f)
#     for line in tempData:
#         writer.writerow(line)
