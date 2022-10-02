import pandas as pd
from sklearn.naive_bayes import GaussianNB
from dados.carregarDados import carregarTreinoTeste
from sklearn.metrics import accuracy_score, precision_score,recall_score,f1_score,classification_report
import numpy as np
from metricas.metricas import imprimirMetricas
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV


X_train, X_test, y_train, y_test = carregarTreinoTeste()

hyperparameters = {'var_smoothing': np.logspace(0,-9, num=100)}

gnb = GaussianNB(var_smoothing=1.873817422860387e-09)
clf = GridSearchCV(gnb, hyperparameters, cv=10,verbose=3)

best_model = gnb.fit(X_train,y_train)
# best_score = best_model.best_score_
# best_params = best_model.best_params_
imprimirMetricas(X_train, X_test, y_train, y_test, gnb, "Naive")
