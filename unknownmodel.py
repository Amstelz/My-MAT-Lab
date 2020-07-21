from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
import sys
import numpy
import pickle
import csv

#load dataset
f=open("CsvData/unknowndata.csv", "r")
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
filename = 'Model/PDF2IMG-finalized_model_LR.sav'
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

