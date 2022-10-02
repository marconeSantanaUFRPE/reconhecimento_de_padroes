from sklearn.neural_network import MLPClassifier
from dados.carregarDados import carregarTreinoTeste
from sklearn.model_selection import GridSearchCV
import os.path
from metricas.metricas import imprimirMetricas

basedir = os.path.abspath(os.path.dirname(__file__))



X_train, X_test, y_train, y_test = carregarTreinoTeste()



mpl = MLPClassifier(early_stopping=True, hidden_layer_sizes=80,
                               learning_rate_init=0.13774366805055854,
                               max_iter=701, momentum=0.6361707266412173)
hyperparameters = {
    'hidden_layer_sizes': [(10,30,10),(20,)],
    'activation': ['tanh', 'relu'],
    'solver': ['sgd', 'adam'],
    'alpha': [0.0001, 0.05],
    'learning_rate': ['constant','adaptive'],
}

# grid_search = GridSearchCV(mlp, hyperparameters, cv=10, verbose=3, n_jobs=-1)

best_model = mpl.fit(X_train, y_train)
# arquivo =  open(basedir + "/tuning/mlp.txt", "w") 
# best_score = best_model.best_score_
# best_params = best_model.best_params_
# for key, value in best_params.items(): 
#     arquivo.write('%s:%s\n' % (key, value))
# arquivo.write("\n")
# arquivo.write(str (best_score))
# arquivo.close()

imprimirMetricas(X_train, X_test, y_train, y_test,best_model)

