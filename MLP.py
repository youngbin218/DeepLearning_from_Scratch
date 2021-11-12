import numpy as np
from keras.layers import Dense
from keras.models import Sequential
from tensorflow.keras import optimizers

model = Sequential()

model.add(Dense(units=2,activation='sigmoid',input_dim=2))
#model.add(Dense(units=12,activation='sigmoid',input_dim=2))
#model.add(Dense(units=3,activation='sigmoid'))

model.add(Dense(units=1,activation='sigmoid'))
#model.add(Dense(units=1,activation='sigmoid', kernel_initializer = "random_uniform", bias_initializer = "random_uniform"))

model.compile(optimizer=optimizers.RMSprop(lr=0.5),loss='binary_crossentropy',metrics=['binary_accuracy'])

print(model.summary())
print(model.get_weights())
