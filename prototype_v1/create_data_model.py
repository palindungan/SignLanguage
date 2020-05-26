import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os


def main():
    IMG_SAVE_PATH = 'image_data'  # lokasi dataset

    CLASS_MAP = {
        'nol': 0,
        'satu': 1,
        'dua': 2,

    }

    # IMG_SAVE_PATH = 'image_data'
    #
    # CLASS_MAP = {
    #     "rock": 0,
    #     "paper": 1,
    #     "scissors": 2,
    #     "none": 3
    # }
    #
    # NUM_CLASSES = len(CLASS_MAP)


main()
