import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /=255
x_test /= 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

#create the model
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

#compile the model
model.compile(loss = 'categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# train the model
history = model.fit(x_train, y_train, batch_size=128, epochs=20, verbose =1, validation_data=(x_test, y_test))

# model evaluate
score = model.evaluate(x_test, y_test, verbose=0)
print('test loss:', score[0])
print('Test accuracy', score[1])

# predict the model
pred = model.predict(x_test)
pred = np.argmax(pred, axis = 1)[:5]
label = np.argmax(y_test, axis = 1)[:5]

