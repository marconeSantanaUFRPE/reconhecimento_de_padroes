# automatic nested cross-validation for random forest on a classification dataset
from numpy import mean
from numpy import std
import pandas as pd

from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

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
cv_inner = KFold(n_splits=3, shuffle=True, random_state=1)
# define the model
model = clf = RandomForestClassifier(max_depth=2, random_state=0)
# define search space
hyperparameters = {
    'max_depth': [5,6,10,11,15,16,20,21,25,26,30,31,35,36],
    'min_samples_leaf': [5, 10, 20, 30,40,50,60,70],
    'criterion': ["entropy","gini","log_loss"],
    "min_impurity_decrease": [0.005,0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6,]
    }
# define search
search = GridSearchCV(model, param_grid=hyperparameters, scoring='accuracy', n_jobs=1, cv=cv_inner, refit=True)
# configure the cross-validation procedure
cv_outer = KFold(n_splits=10, shuffle=True, random_state=1)
# execute the nested cross-validation
scores = cross_val_score(search, X, y, scoring='accuracy', cv=cv_outer, n_jobs=-1)
# report performance
print('Accuracy: %.3f (%.3f)' % (mean(scores), std(scores)))