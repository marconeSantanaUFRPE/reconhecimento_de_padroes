from randomForest import bestRandomForest
from knn import bestKnn
from dados.carregarDados import carregarTreinoTeste

X_train, X_test, y_train, y_test = carregarTreinoTeste()
print("------------------------------------------")
print('Best Random Forest')
bestRandomForest(X_train, X_test, y_train, y_test)
print("------------------------------------------")
print("Best KNN")
bestKnn(X_train, X_test, y_train, y_test)
print("------------------------------------------")
