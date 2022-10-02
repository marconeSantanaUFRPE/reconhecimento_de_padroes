from knn import knnTuning
from randomForest import tuningRandomForest
from decisionTree import tuningDecisionTree
from svm import tuningSvm

from dados.carregarDados import carregarTreinoTeste

X_train, X_test, y_train, y_test = carregarTreinoTeste()


# knnTuning(X_train, X_test, y_train, y_test)
# tuningRandomForest(X_train, X_test, y_train, y_test)
# tuningDecisionTree(X_train, X_test, y_train, y_test)
# tuningSvm(X_train, X_test, y_train, y_test)



