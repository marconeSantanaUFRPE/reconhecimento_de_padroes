from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

clf = DecisionTreeClassifier(random_state=0,criterion='gini',max_depth=4)
baseDados = pd.read_csv('base_flowup/teste_arvore_treino.csv')

rotulo = baseDados['atrasado'].to_numpy()
rotulo = rotulo.reshape(4998,)
del baseDados['atrasado']
base = baseDados.to_numpy()
base = base.reshape(4998,3)
var = cross_val_score(clf, base, rotulo, cv=10)
print(var)
clf.fit(base, rotulo)

baseTeste = pd.read_csv('base_flowup/teste_arvore_teste.csv')
del baseTeste['atrasado']
baseTeste = baseTeste.to_numpy()
baseTeste = baseTeste.reshape(2924,3)

predict = clf.predict(baseTeste)
# predict = (knn.predict(baseTeste))
arquivo = open("result.txt", "w")
for x in predict:
    arquivo.write(str(x)+"\n")
