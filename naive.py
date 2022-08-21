import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


baseDados = pd.read_csv('new_base.csv')
y = baseDados['atrasado'].to_numpy()
del baseDados['atrasado']
del baseDados['id']
print(baseDados)
X = baseDados.to_numpy().reshape(4914,64)
Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.8)


gnb = GaussianNB()
gnb.fit(Xtrain,y_train)
y_pred = gnb.predict(Xtest)


print(accuracy_score(y_test, y_pred))
# # arquivo = open("result.txt", "w")
# # for x in predict:
# #     arquivo.write(str(x)+"\n")
