import pickle

import numpy as np

import tensorflow as tf
from model import classifier

# Churn Predictor
class Predictor():
  def __init__(self):
    self.device = "cuda" if tf.test.is_gpu_available() else "cpu"

    # load model weights
    self.predictor = classifier

    self.predictor.load_weights("models/model")

    # load scaler
    with open('scalers/scaler.pickle', 'rb') as handle:
        self.scaler = pickle.load(handle)

    # load encoders
    with open('encoders/encoder1.pickle', 'rb') as handle:
        self.encoder1 = pickle.load(handle)

    with open('encoders/encoder2.pickle', 'rb') as handle:
        self.encoder2 = pickle.load(handle)

  def predict(self, input_data):
    # classes
    classes = {True : "Customer will churn! :heavy_multiplication_x:", False: "Customer will not churn! :heavy_check_mark:"}
    # image name
    image_names = {True: "churn", False: "not_churn"}
    # encode data
    input_data[0][1] = self.encoder1.transform([input_data[0][1]])[0]
    input_data[0][2] = self.encoder2.transform([input_data[0][2]])[0]
    # scale data
    transformed_data = self.scaler.transform(input_data)
    # predict
    pred = classifier.predict(transformed_data) > 0.5

    return classes[pred[0][0]], image_names[pred[0][0]]
