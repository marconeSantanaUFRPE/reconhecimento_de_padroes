from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.ensemble import BaggingClassifier
from metricas.metricas import imprimirMetricas
from dados.carregarDados import carregarTreinoTeste

X_train, X_test, y_train, y_test = carregarTreinoTeste()

n_estimators=1800
min_samples_split=2
min_samples_leaf=2
max_features="auto"
max_depth=74
criterion="entropy"
bootstrap=True
base_estimator = RandomForestClassifier(n_estimators=n_estimators,criterion=criterion, 
        max_depth=max_depth ,min_samples_split=min_samples_split,min_samples_leaf=min_samples_leaf,
        max_features='sqrt', bootstrap=bootstrap)


clf = BaggingClassifier(base_estimator=base_estimator,
                         n_estimators=6, random_state=42).fit(X_train, y_train)
imprimirMetricas(X_train, X_test, y_train, y_test, clf, 'knn')
