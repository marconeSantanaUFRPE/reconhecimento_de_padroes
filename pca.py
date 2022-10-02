import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pandas as pd


baseDados = pd.read_csv('csv/dataframe.csv')
y = baseDados['classe']
del baseDados['id']
del baseDados['classe']
del baseDados['tempoGasto']
del baseDados['totalsub']
X = baseDados

pca = PCA(n_components=2)

pca_dataframe = pca.fit(X)

print(pca.explained_variance_ratio_)

print(pca.explained_variance_ratio_.sum())

print(pca.explained_variance_ratio_)