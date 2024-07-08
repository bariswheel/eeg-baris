'''Long Short-Term Memory Networks for EEG-Based Brain-Computer Interfaces'''
'''Using LSTM to model time-related(temporal) dependencies in EEG signals, for tasks like'''
'''mental state classification and continuous control in BCIs.'''
'''Achieves accuracy around 80-90% in tasks requiring real-time prediction and control'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

model = Sequential([
    LSTM(64, input_shape=(time_steps, channels)),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
