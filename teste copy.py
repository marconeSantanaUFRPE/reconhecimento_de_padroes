# manual nested cross-validation for random forest on a classification dataset
from numpy import mean
import pandas as pd
from numpy import std
from sklearn.datasets import make_classification
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
# create dataset
baseDados = pd.read_csv('csv/dataframe.csv')
y = baseDados['classe'].to_numpy()
del baseDados['classe']
del baseDados['tempoGasto']
del baseDados['totalsub']

del baseDados['id']
print(baseDados)
X = baseDados.to_numpy()

# configure the cross-validation procedure
cv_outer = KFold(n_splits=10, shuffle=True, random_state=1)
# enumerate splits
outer_results = list()
for train_ix, test_ix in cv_outer.split(X):
  # split data
  X_train, X_test = X[train_ix, :], X[test_ix, :]
  y_train, y_test = y[train_ix], y[test_ix]
  # configure the cross-validation procedure
  cv_inner = KFold(n_splits=3, shuffle=True, random_state=1)
  # define the model
  model = DecisionTreeClassifier(criterion='entropy', random_state=1)
  # define search space
  space = dict()
  space['min_samples_leaf'] = [1, 5, 10, 15, 20]
  space['max_depth'] = [1,2,3,5,8,13,21,34,55]
  space['min_impurity_decrease'] = [0.001,0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5]
  # define search
  search = GridSearchCV(model, space, scoring='accuracy', cv=cv_inner, refit=True)
  # execute search
  result = search.fit(X_train, y_train)
  # get the best performing model fit on the whole training set
  best_model = result.best_estimator_
  # evaluate model on the hold out dataset
  yhat = best_model.predict(X_test)
  # evaluate the model
  acc = accuracy_score(y_test, yhat)
  # store the result
  outer_results.append(acc)
  # report progress
print('>acc=%.3f, est=%.3f, cfg=%s' % (acc, result.best_score_, result.best_params_))
# summarize the estimated performance of the model
print('Accuracy: %.3f (%.3f)' % (mean(outer_results), std(outer_results)))
