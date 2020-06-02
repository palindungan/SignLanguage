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
    'none': 0,
    'one-hand-A': 1,
    'one-hand-B': 2,
    'one-hand-C': 3,
    'one-hand-D': 4
}

NUM_CLASSES = len(CLASS_MAP)  # jumlah total list label


def mapper(key):  # fungsi untuk mengambil nilai
    return CLASS_MAP[key]


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
    # directory = label name
    path = os.path.join(IMG_SAVE_PATH, directory)  # merujuk pada lokasi folder pada setiap label
    if not os.path.isdir(path):  # validasi jika alamat bukan merujuk pada folder
        continue  # semua proses dibawahnya akan dilewati(skip) dan kembali ke perulangan selanjutnya
    for item in os.listdir(path):  # perulangan sebanyak isi didalam folder (disetiap folder label)
        # item = setiap file didalam label
        if item.startswith('.'):  # validasi jika ada file hidden
            continue  # semua proses dibawahnya akan dilewati(skip) dan kembali ke perulangan selanjutnya
        img = cv2.imread(os.path.join(path, item))  # membaca file dengan lokasi setiap item
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # mengubah format warna dari BGR ke RGB
        img = cv2.resize(img, (227, 227))  # mengatur ukuran gambar lebar * tinggi
        dataset.append(img, directory)  # menambah urutan array berupa [[[array1] , 'label1'], [[array2] , 'label2']]

'''
dataset = [
    [[...], 'none'],
    [[...], 'one-hand-A'],
    [[...], 'one-hand-B'],
    [[...], 'one-hand-C'],
    [[...], 'one-hand-D']
    ...
]
'''

data, labels = zip(*dataset)  # data = semua_array, labels = semua_label --> memecah variabel menjadi 2 sub variabel
labels = list(map(mapper, labels))  # map -> mengembalikan nilai dari fungsi mapper yang diberi key labels

'''
labels: one-hand-A, one-hand-B, one-hand-B, one-hand-C, one-hand-D...
'''

# one hot encode the labels
labels = np_utils.to_categorical(labels)  # Mengubah vektor kelas (integer) ke matriks kelas biner.

'''
one hot encoded: [0,1,0,0,0], [0,0,1,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]...
'''

# mendefinisikan model CNN
model = get_model()
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])

# memulai training data
model.fit(np.array(data), np.array(labels), epochs=10)

# menyimpan hasil training data menjadi model untuk digunakan selanjutnya
model.save('modelSignLanguageV1')
