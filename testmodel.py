#!/usr/bin/python3
# -*- coding: utf-8 -*-
import pandas as pd
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import sys
import numpy
import pickle
import csv

def classifaction_report_csv(report):
    report_data = []
    lines = report.split('\n')
    row = {}
    row_data = lines[2].split('      ')
    row['class'] = row_data[2]
    row['precision'] = row_data[3]
    row['recall'] = row_data[4]
    row['f1_score'] = row_data[5]
    row['support'] = row_data[6]
    report_data.append(row)
    for line in lines[3:-5]:
        row = {}
        row_data = line.split('      ')
        row['class'] = row_data[1]
        row['precision'] = row_data[2]
        row['recall'] = row_data[3]
        row['f1_score'] = row_data[4]
        row['support'] = row_data[5]
        report_data.append(row)
    dataframe = pd.DataFrame.from_dict(report_data)
    dataframe.to_csv('CsvData/report.csv', index = False)

#load dataset
f=open("CsvData/testdata.csv", "r")
names = []
for n in range (1296):
  if len(str((n+1))) == 1:
    fill = 'a000' + str((n+1))
  elif len(str((n+1))) == 2:
    fill = 'a00' + str((n+1))
  elif len(str((n+1))) == 3:
    fill = 'a0' + str((n+1))
  else:
    fill = 'a' + str((n+1))
  names.append(fill)
names.append('class')
dataset = read_csv(f, names=names)

# load the model from disk
filename = 'Model/finalized_model_LR.sav'
loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X, y)
#print(result)

# Split-out validation dataset
array = dataset.values
X = array[:,0:1296]
Y = array[:,1296]

# Test model
res = loaded_model.predict(X)


#print res
new_res = []
str =''
for name in res:
    str = str + name
print(str)

text_file = open("result/testresult.txt", "w")
n = text_file.write(str)
text_file.close()

print(accuracy_score(Y, res))
print(confusion_matrix(Y, res))
print(classification_report(Y, res))

data = confusion_matrix(Y, res)
confusion = [] 
for row in data:
  confusion.append(list(row))

with open('CsvData/confusion matrix.csv', mode='w', newline='',encoding='utf8') as file:
    writer = csv.writer(file)
    writer.writerows(confusion)

#pd.DataFrame(report_dict)
report = classification_report(Y, res)
classifaction_report_csv(report)


#data.reshape(100,300)
#numpy.set_printoptions(threshold=sys.maxsize)
#print(data)

