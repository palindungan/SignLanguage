import cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import os

IMG_SAVE_PATH = 'image_data'  # lokasi absolute path --> home untuk semua dataset

CLASS_MAP = {  # label dan index id (key:value)
    'one-hand-A': 0,
    'one-hand-B': 1,
    'one-hand-C': 2,
    'one-hand-D': 3
}

NUM_CLASSES = len(CLASS_MAP)  # jumlah total list label


def mapper(val):  # fungsi untuk mengambil nilai
    return CLASS_MAP[val]


def get_model():  # design pembuatan model CNN
    model = Sequential([
        SqueezeNet(input_shape=(227, 227, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(NUM_CLASSES, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model


# load data dari folder
dataset = []
for directory in os.listdir(IMG_SAVE_PATH):  # melakukan perulangan sebanyak list direktori yang ada pada IMG_SAVE_PATH
    path = os.path.join(IMG_SAVE_PATH, directory)  # merujuk pada lokasi folder pada setiap label
    if not os.path.isdir(path):  # validasi jika alamat bukan merujuk pada folder
        continue  # semua proses dibawahnya akan dilewati(skip) dan kembali ke perulangan selanjutnya
    for item in os.listdir(path):  # perulangan sebanyak isi didalam folder (disetiap folder label)
        if item.startswith('.'):  # validasi jika ada file kosong
            continue  # semua proses dibawahnya akan dilewati(skip) dan kembali ke perulangan selanjutnya

