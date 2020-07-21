from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
import pickle
#load dataset
f=open("CsvData/traindata.csv", "r")
print("Already Get TrainData")
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

# Split-out validation dataset
array = dataset.values
X = array[:,0:1296]
y = array[:,1296]
X_train, X_validation, Y_train, Y_validation = train_test_split(X, y, test_size=0.20, random_state=1)

# Make predictions on validation dataset
model = LogisticRegression(solver='liblinear', multi_class='ovr')
#model = KNeighborsClassifier()
model.fit(X_train, Y_train)
predictions = model.predict(X_validation)

# Evaluate predictions
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# save the model to disk
filename = "Model/PDF2IMG-finalized_model_LR.sav"
#filename = "Model/finalized_model_KNN.sav"
pickle.dump(model, open(filename, 'wb'))
print("Already Dump Model File")
