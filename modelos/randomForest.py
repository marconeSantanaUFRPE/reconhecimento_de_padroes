from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_recall_curve,auc,accuracy_score, precision_score,recall_score,f1_score,classification_report,roc_auc_score
from dados.carregarDados import carregarTreinoTeste
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, cross_val_score
from sklearn.model_selection import RandomizedSearchCV
import pandas as pd
import numpy as np
from metricas.metricas import imprimirMetricas
import os.path
basedir = os.path.abspath(os.path.dirname(__file__))


def tuningRandomForest(X_train, X_test, y_train, y_test):
    # Number of trees in random forest
    n_estimators = [int(x) for x in np.linspace(start = 200, stop = 2000, num = 10)]
    # Number of features to consider at every split
    max_features = ['auto', 'sqrt']
    # Maximum number of levels in tree
    max_depth = [int(x) for x in np.linspace(10, 440, num = 11)]
    max_depth.append(None)
    # Minimum number of samples required to split a node
    min_samples_split = [2, 5, 10,12,15]
    # Minimum number of samples required at each leaf node
    min_samples_leaf = [1, 2, 4,6,8]
    # Method of selecting samples for training each tree
    bootstrap = [True, False]
    
    criterion = ["gini", "entropy", "log_loss"]

    randomForest = RandomForestClassifier()
    hyperparameters = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf,
               'bootstrap': bootstrap,
               'criterion':criterion
               }

    
    random_search = RandomizedSearchCV(estimator = randomForest, param_distributions = hyperparameters, 
                    n_iter = 100, cv = 5, verbose=2, random_state=42, n_jobs = -1)

    best_model = random_search.fit(X_train,y_train)
    
    best_model.best_estimator_

    arquivo =  open(basedir + "/tuning/randomForest.txt", "w") 
    arquivo.write("random_search")

    best_score = best_model.best_score_
    best_params = best_model.best_params_
    for key, value in best_params.items(): 
        arquivo.write('%s:%s\n' % (key, value))
    arquivo.write("\n")
    arquivo.write(str (best_score))
    print(best_model.best_score_)
    print(best_model.best_params_)
    print(classification_report(y_test, best_model.predict(X_test)))

    arquivo.write("\n")
    arquivo.write("-----------------------------------------------")
    arquivo.write("grid_search")

    grid_search = GridSearchCV(estimator=randomForest, 
                           param_grid=hyperparameters, 
                           cv=10, n_jobs=-1, verbose=3, scoring = "accuracy",refit=True)

    best_model = grid_search.fit(X_train,y_train)
    best_score = best_model.best_score_
    best_params = best_model.best_params_
    for key, value in best_params.items(): 
        arquivo.write('%s:%s\n' % (key, value))
    arquivo.write("\n")
    arquivo.write(str (best_score))

    arquivo.close()

def bestRandomForest(X_train, X_test, y_train, y_test):
    n_estimators=1800
    min_samples_split=2
    min_samples_leaf=2
    max_features="auto"
    max_depth=74
    criterion="entropy"
    bootstrap=True
    clf = RandomForestClassifier(n_estimators=n_estimators,criterion=criterion, 
            max_depth=max_depth ,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,
            max_features='sqrt', bootstrap=bootstrap)
    clf = clf.fit(X_train, y_train)
    imprimirMetricas(X_train, X_test, y_train, y_test, clf, "RandomForest")



def randomForest(X_train, X_test, y_train, y_test):

    clf = RandomForestClassifier(n_estimators=10,criterion="entropy", max_depth=None,min_samples_split=2, random_state=0)
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    classification_r = classification_report(y_test, y_pred)
    print(classification_r)


    # calculando a acuracia, precisao e cobertura
    acuracia = accuracy_score(y_test, y_pred)
    precisao = precision_score(y_test, y_pred)
    cobertura = recall_score(y_test, y_pred)

    # calculando a curva
    y_prob = clf.predict_proba(X_test)[:, 1] # probabilidades para a 2a classe


    curva_precisao, curva_cobertura, thresholds = precision_recall_curve(y_test, y_prob)

    # calculando a área sob a curva
    auc_precisao_cobertura = auc(curva_cobertura, curva_precisao)

    # imprimindo
    print(f"Acurácia de teste = {acuracia}")
    print(f"AUC = {auc_precisao_cobertura}")
    print(f"Precisão = {precisao}, cobertura = {cobertura}")

    ''' Plotando curva '''
    plt.plot(curva_cobertura, curva_precisao)
    plt.show()



if __name__ == "__main__":

    X_train, X_test, y_train, y_test = carregarTreinoTeste()
    # randomForest()

    #tuningRandomForest(X_train, X_test, y_train, y_test)

    bestRandomForest(X_train, X_test, y_train, y_test)