from dados.carregarDados import carregarTreinoTeste
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
import os.path
from metricas.metricas import imprimirMetricas

basedir = os.path.abspath(os.path.dirname(__file__))



def tuningSvm( X_train, X_test, y_train, y_test):
    hyperparameters = {'C': [0.1, 1, 10, 100, 1000,10000], 
                'gamma': [1, 0.1, 0.01, 0.001, 0.0001,0.00001],
                'kernel': ["rbf","linear", "poly", "sigmoid", "precomputed"],
                'degree':[1,2,3,4,5,6,7]
                
                } 
    svm = SVC()

    grid_search = GridSearchCV(estimator=svm, 
                            param_grid=hyperparameters, 
                            cv=10, n_jobs=-1, verbose=3, scoring = "accuracy",refit=True)

    best_model = grid_search.fit(X_train,y_train)
    arquivo =  open(basedir + "/tuning/svm.txt", "w") 
    best_score = best_model.best_score_
    best_params = best_model.best_params_
    for key, value in best_params.items(): 
        arquivo.write('%s:%s\n' % (key, value))
    arquivo.write("\n")
    arquivo.write(str (best_score))
    arquivo.close()


    print(best_model.best_score_)
    print(best_model.best_params_)
    print(classification_report(y_test, best_model.predict(X_test)))


def bestSvm(X_train, X_test, y_train, y_test):

                
    svm = SVC(C=1,gamma=0.1,kernel="rbf",probability=True)
    svm.fit(X_train,y_train)

    imprimirMetricas(X_train, X_test, y_train, y_test, svm, 'svm')





if __name__ == "__main__":
    X_train, X_test, y_train, y_test = carregarTreinoTeste()
    bestSvm(X_train, X_test, y_train, y_test)
    #tuningSvm(X_train, X_test, y_train, y_test)