import keras
import numpy as np
import pandas as pd
import cv2
from matplotlib import pyplot as plt
from keras.models import Sequential 
from keras.layers import Conv2D,MaxPooling2D, Dense,Flatten, Dropout
from keras.datasets import mnist 
import matplotlib.pyplot as plt
from keras.utils import np_utils
from keras.optimizers import SGD


# PREPROCESSING DATA ------------------------------------------------------------------
data_test = pd.read_csv("./data/sign_mnist_test/sign_mnist_test.csv")
data_train = pd.read_csv("./data/sign_mnist_train/sign_mnist_train.csv")

labels = data_train['label']
data_train.drop('label', axis=1, inplace=True)
labels_test = data_test['label']
data_test.drop('label', axis=1, inplace=True)


X_train = np.array(data_train.iloc[:,:])
X_train = np.array([np.reshape(i, (28,28)) for i in X_train])
X_test = np.array(data_test.iloc[:,:])
X_test = np.array([np.reshape(i, (28,28)) for i in X_test])

print(X_train, X_test)

num_classes = 26

y_train = np.array(labels).reshape(-1)
y_test = np.array(labels_test).reshape(-1)

y_train = np.eye(num_classes)[y_train]
y_test = np.eye(num_classes)[y_test]

X_train = X_train.reshape((27455, 28, 28, 1))
X_test = X_test.reshape((7172, 28, 28, 1))


# CNN ---------------------------------------------------------------------
classifier = Sequential()
classifier.add(Conv2D(filters=8, kernel_size=(3,3),strides=(1,1),padding='same',input_shape=(28,28,1),activation='relu', data_format='channels_last'))
classifier.add(MaxPooling2D(pool_size=(2,2)))
classifier.add(Conv2D(filters=16, kernel_size=(3,3),strides=(1,1),padding='same',activation='relu'))
classifier.add(Dropout(0.5))
classifier.add(MaxPooling2D(pool_size=(4,4)))
classifier.add(Dense(128, activation='relu'))
classifier.add(Flatten())
classifier.add(Dense(26, activation='softmax'))

classifier.compile(optimizer='SGD', loss='categorical_crossentropy', metrics=['accuracy'])
classifier.fit(X_train, y_train, epochs=50, batch_size=100)

accuracy = classifier.evaluate(x=X_test,y=y_test,batch_size=32)
print("Accuracy: ",accuracy[1])

classifier.save('CNNmodel.h5')
