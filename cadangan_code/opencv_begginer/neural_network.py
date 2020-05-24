import numpy as np


def NN(m1, m2, w1, w2, b):
    z = (m1 * w1) + (m2 * w2) + b
    return z


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

