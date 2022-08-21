from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


baseDados = pd.read_csv('csv/dataframe.csv')
y = baseDados['atrasado'].to_numpy()
del baseDados['atrasado']
del baseDados['id']
print(baseDados)
X = baseDados.to_numpy().reshape(4914,64)
Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 0, train_size = 0.8)

maiorAccuracy =0
mairK = 0
# k = 7 maior accuracy
for x in range(1,100):
    knn = KNeighborsClassifier(n_neighbors=x)
    knn.fit(Xtrain,y_train)
    y_pred = knn.predict(Xtest)
    accuracy = accuracy_score(y_test, y_pred)
    print(str(x) + " -> " + str(accuracy))
    if(accuracy> mairK):
        mairK = accuracy
        maiorAccuracy = x
    
print(str(maiorAccuracy) + "->" + str(mairK))



