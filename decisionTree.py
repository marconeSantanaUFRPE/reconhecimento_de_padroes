from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score



baseDados = pd.read_csv('csv/new_base.csv')
y = baseDados['atrasado'].to_numpy()
del baseDados['atrasado']
del baseDados['id']
print(baseDados)
X = baseDados.to_numpy().reshape(4914,64)
Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.8)


clf = DecisionTreeClassifier(random_state=0,criterion='entropy',max_depth= 15)
clf.fit(Xtrain,y_train)
y_pred = clf.predict(Xtest)

print(accuracy_score(y_test, y_pred))

