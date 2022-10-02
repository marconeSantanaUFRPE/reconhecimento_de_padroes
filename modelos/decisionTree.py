from sklearn.tree import DecisionTreeClassifier
from dados.carregarDados import carregarTreinoTeste, carregarDadosRotulos
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score,classification_report,roc_auc_score
from dados.carregarDados import carregarTreinoTeste
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from metricas.metricas import imprimirMetricas 
import numpy as np
import os.path

basedir = os.path.abspath(os.path.dirname(__file__))



def tuningDecisionTree(X_train, X_test, y_train, y_test):

    decisionTree = DecisionTreeClassifier()
    max_depth = [int(x) for x in np.linspace(10, 400, num = 10)]
    max_depth.append(None)
    min_samples_leaf = [1,2,3,4,5,10,20]
    min_samples_split = [2,4,6,8,10,11,15]
    hyperparameters = {
    'min_samples_leaf':min_samples_leaf,
    'min_samples_split':min_samples_split,
    'max_depth': max_depth,
    'min_samples_leaf': [2,3, 5, 10, 15 ,20],
    'criterion': ["entropy","gini","log_loss"],
    "min_impurity_decrease": [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7,0.8]
    }

    grid_search = GridSearchCV(estimator=decisionTree, 
                           param_grid=hyperparameters, 
                           cv=10, n_jobs=-1, verbose=3, scoring = "accuracy",refit=True)

    best_model = grid_search.fit(X_train, y_train)
    arquivo =  open(basedir + "/tuning/decisionTree.txt", "w") 
    best_score = best_model.best_score_
    best_params = best_model.best_params_
    for key, value in best_params.items(): 
        arquivo.write('%s:%s\n' % (key, value))
    arquivo.write("\n")
    arquivo.write(str (best_score))
    arquivo.close()


    best_model.best_estimator_

    print(best_model.best_score_)
    print(best_model.best_params_)
    print(classification_report(y_test, best_model.predict(X_test)))

def best_decisionTree(X_train, X_test, y_train, y_test):
    '''
    criterion:entropy
    max_depth:10
    min_impurity_decrease:0.005
    min_samples_leaf:2
    ''' 
    clf = DecisionTreeClassifier(
        criterion="entropy",max_depth= 10, min_impurity_decrease=0.005,min_samples_leaf=50)
    
    clf = clf.fit(X_train,y_train)

    imprimirMetricas(X_train, X_test, y_train, y_test, clf,"DecisionTree")



if __name__ == "__main__":
    X_train, X_test, y_train, y_test = carregarTreinoTeste()

    tuningDecisionTree(X_train, X_test, y_train, y_test)
    # decisionTree()
    # best_decisionTree(X_train, X_test, y_train, y_test)