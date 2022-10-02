import matplotlib.pyplot as plt
import pandas as pd

from sklearn import datasets
from sklearn.decomposition import PCA

baseDados = pd.read_csv('csv/dataframe.csv')
print(baseDados)
y = baseDados['classe'].to_numpy()
del baseDados['classe']
del baseDados['intervalo']
del baseDados['responsavel']
del baseDados['totalsub']
del baseDados['prioridade']
del baseDados['minutos']
del baseDados['estimativa']

del baseDados['id']
X = baseDados.to_numpy().reshape(4914,58)
target_names = ['classe', 'regular']
pca = PCA(n_components=2)
X_r = pca.fit(X).transform(X)



# Percentage of variance explained for each components
print(
    "explained variance ratio (first two components): %s"
    % str(pca.explained_variance_ratio_)
)

plt.figure()
colors = ["navy", "turquoise"]
lw = 2

for color, i, target_name in zip(colors, [0, 1], target_names):
    plt.scatter(
        X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=0.8, lw=lw, label=target_name
    )
plt.legend(loc="best", shadow=False, scatterpoints=1)
plt.title("PCA Teste")


plt.show()