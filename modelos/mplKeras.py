from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Activation, Dense
from keras import optimizers
from dados.carregarDados import carregarTreinoTeste
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
import numpy as np


model = Sequential()
X_train, X_test, y_train, y_test = carregarTreinoTeste()


print('X_train:',np.shape(X_train))
print('y_train:',np.shape(y_train))
print('X_test:',np.shape(X_test))
print('y_test:',np.shape(y_test))
# First layers: 16 neurons/perceptrons that takes the input and uses 'sigmoid' activation function.

model.add(Dense(units = 16 , activation = 'sigmoid', input_shape = (20,))) 
# Second layer: 1 neuron/perceptron that takes the input from the 1st layers and gives output as 0 or 1.Activation used is 'Hard Sigmoid'

model.add(Dense(50, input_shape = (20, )))
model.add(Activation('relu'))    # use relu
model.add(Dense(50))
model.add(Activation('relu'))    # use relu
model.add(Dense(50))
model.add(Activation('relu'))    # use relu
model.add(Dense(50))
model.add(Activation('relu'))    # use relu
model.add(Dense(10))
model.add(Activation('softmax'))
model.add(Dense(1, activation = 'hard_sigmoid'))

sgd = keras.optimizers.SGD(learning_rate=0.5, momentum=0.9, nesterov=True)
model.compile(loss = 'binary_crossentropy', optimizer = 'sgd', metrics = ['accuracy'])

history = model.fit(X_train, y_train, batch_size = 256, validation_split = 0.3, epochs = 200, verbose = 3)

loss_and_metrics = model.evaluate(X_test, y_test)
print('Loss = ',loss_and_metrics[0])
print('Accuracy = ',loss_and_metrics[1])
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.legend(['training', 'validation'], loc = 'upper left')
plt.show()