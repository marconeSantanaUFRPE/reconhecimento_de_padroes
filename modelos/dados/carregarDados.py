import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt

def carregarDadosRotulos():
    X = pd.read_csv('csv/dataframe.csv')
    y = X['classe']
    del X['id']
    del X['tempoGasto']
    del X['totalsub']
    # sns.pairplot(X,hue='classe',palette='Dark2')
    del X['classe']
    # plt.show()

    print(X.head())


    return X,y


def carregarTreinoTeste():
    X,y = carregarDadosRotulos()
    Xtrain, Xtest, y_train, y_test = train_test_split(X, y, stratify = y, random_state = 42, train_size = 0.8)
    print('Dimensões dos conjuntos')
    print(Xtrain.shape)
    print(Xtest.shape)
    return Xtrain, Xtest, y_train, y_test 
    
