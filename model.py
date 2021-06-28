from keras.models import Sequential
from keras.layers import Dense, Dropout

# Churn Predictor Model - DNN
classifier = Sequential()
classifier.add(Dense(units = 32, activation = 'relu', input_dim = 10))
classifier.add(Dense(units = 16, activation = 'relu'))
classifier.add(Dense(units = 8, activation = 'relu'))
classifier.add(Dropout(0.4))
classifier.add(Dense(units = 1, activation = 'sigmoid'))

# compile model
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])
