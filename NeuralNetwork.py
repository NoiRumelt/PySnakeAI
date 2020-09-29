import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation
import numpy as np

'''physical_devices = tf.config.experimental.list_physical_devices('GPU')
print("NUM of GPU available: ", len(physical_devices))
tf.config.experimental.set_memory_growth(physical_devices[0], True)'''

def create_model():
    # [TODO]
    # create keras model
    model = Sequential()
    model.add(Dense(32, input_shape=(32,)))
    model.add(Activation('relu'))
    model.add(Dense(20, input_shape=(32,)))
    model.add(Activation('relu'))
    model.add(Dense(12, input_shape=(20,)))
    model.add(Activation('relu'))
    model.add(Dense(4, input_shape=(12,)))
    model.add(Activation('sigmoid'))

    model.compile(loss='mse',optimizer='adam')

    return model


def predict_action(vision_vector, model: Sequential()):
    # The height, dist and pipe_height must be between 0 to 1 (Scaled by SCREENHEIGHT)

    # [TODO]
    # Feed in features to the neural net
    # Reshape input
    # Get prediction from model
    vision_vector = np.transpose(vision_vector)
    output_prob = model.predict(vision_vector, 1)
    return output_prob


