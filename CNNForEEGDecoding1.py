'''Configuring layers for signal processing and classification tasks using TensorFlow/Keras'''
'''Deep Learning with Convolutinonal Neural Networks for EEG Decoding and Visualization'''
'''https://onlinelibrary.wiley.com/doi/full/10.1002/hbm.23730'''
'''This study applies CNNs to decode EEG signals for brain-computer interface applications with accuracy exceeding 90% in classifying cognitive states'''

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(channels, time_steps, 1)),
    MaxPooling2D(pool_size=(2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X_train, y_train, epochs=10, validation_data=(X_val, y_val))
