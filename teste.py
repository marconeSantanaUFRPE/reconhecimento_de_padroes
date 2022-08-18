from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


baseDados = pd.read_csv('base_flowup/bruto2.csv')
y = baseDados['atrasado'].to_numpy()
del baseDados['atrasado']
del baseDados['id']
print(baseDados)
X = baseDados.to_numpy().reshape(7927,6)
Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.8)


knn = KNeighborsClassifier(n_neighbors=15)
knn.fit(Xtrain,y_train)
y_pred = knn.predict(Xtest)


print(accuracy_score(y_test, y_pred))
# # arquivo = open("result.txt", "w")
# # for x in predict:
# #     arquivo.write(str(x)+"\n")
