from sklearn.neighbors import KNeighborsClassifier
from dados.carregarDados import carregarTreinoTeste, carregarDadosRotulos
from sklearn.metrics import precision_recall_curve,auc,accuracy_score, precision_score,recall_score,f1_score,classification_report,roc_auc_score
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
import os.path
from metricas.metricas import imprimirMetricas
import pandas as pd
import matplotlib.pyplot as plt

basedir = os.path.abspath(os.path.dirname(__file__))



def knnTuning(X_train, X_test, y_train, y_test):
    
    n_neighbors = list(range(1,50))

    hyperparameters = { 'n_neighbors' : n_neighbors,
               'weights' : ['uniform','distance'],
               'metric' : ['minkowski','euclidean','manhattan']}

    knn_2 = KNeighborsClassifier()
    clf = GridSearchCV(knn_2, hyperparameters, cv=10,verbose=3)
    #clf = RandomizedSearchCV(knn_2, hyperparameters, cv=10, n_iter=500, scoring='accuracy',random_state=1)

    best_model = clf.fit(X_train,y_train)
    arquivo =  open(basedir + "/tuning/knn.txt", "w") 
    best_score = best_model.best_score_
    best_params = best_model.best_params_
    for key, value in best_params.items(): 
        arquivo.write('%s:%s\n' % (key, value))
    arquivo.write("\n")
    arquivo.write(str (best_score))
    arquivo.close()

    print('Best leaf_size:', best_model.best_estimator_.get_params()['leaf_size'])
    print('Best p:', best_model.best_estimator_.get_params()['p'])
    print('Best n_neighbors:', best_model.best_estimator_.get_params()['n_neighbors'])
    print('Best weights:', best_model.best_estimator_.get_params()['weights'])
    print(classification_report(y_test, best_model.predict(X_test)))

def bestKnn(X_train, X_test, y_train, y_test):

    '''leaf_size:1
        n   _neighbors:24
        p:1
        weights:distance'''
    knn = KNeighborsClassifier(n_neighbors=24,weights='distance',metric='manhattan')
    knn.fit(X_train,y_train)
    imprimirMetricas(X_train, X_test, y_train, y_test, knn, 'knn')





if __name__ == "__main__":

    Xtrain, Xtest, y_train, y_test = carregarTreinoTeste()
    bestKnn(Xtrain, Xtest, y_train, y_test)
    #knnTuning(Xtrain, Xtest, y_train, y_test)

