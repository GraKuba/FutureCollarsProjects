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


# FROM THE TERMINAL INPUT FIGURE OUT, WHICH OUTPUT TO APPLY
if sys.argv[3] == 'file.pickle':
    name = 'pickle'
    binary = 'b'
elif sys.argv[3] == 'file.json':
    name = 'json'
    binary = ''
else:
    name = 'csv'
    binary = ''

# TAKE INPUT FROM THE TERMINAL AND APPLY CHANGES
data = Manager(file, sys.argv[3], name).downloadFile()
data[int(sys.argv[3])][int(sys.argv[4])] = sys.argv[5]

# SAVE DATA IN THE FILE OF THE TYPE GIVEN IN TERMINAL
Manager.writeFile(data, binary)
