import numpy as np
import tensorflow as tf

from tensorflow import keras
from keras.models import load_model
from nlu.utils.multi_classification_utils import preProcessInputs

labels = open('nlu\entities.txt', 'r', encoding='utf-8').read().split('\n')
model = load_model('nlu\model.h5')

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
    label2idx[label] = k
    idx2label[k] = label

def classify(text):
    x = np.zeros((1, 75, 256), dtype='float32')

    text = preProcessInputs(text)
    print(text)

    if len(text) > 75:
        text = text[:75]

    for k, ch in enumerate(bytes(text.encode('utf-8'))):
        x[0, k, int(ch)] = 1.0

    out = model.predict(x)
    idx = out.argmax()

    return {"entity" : idx2label[idx], "conf" : max(out[0])}