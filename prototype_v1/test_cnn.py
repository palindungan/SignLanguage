from keras.models import load_model
import cv2
import numpy as np
import sys

filePath = sys.argv[1]  # berisi argument dengan index ke-1 merujuk pada alamat file

REV_CLASS_MAP = {  # reverse dari variable CLASS_MAP
    0: 'none',
    1: 'one-hand-A',
    2: 'one-hand-B',
    3: 'one-hand-C',
    4: 'one-hand-D',
}


def mapper(key):  # fungsi untuk mengambil nilai
    return REV_CLASS_MAP[key]


model = load_model('modelSignLanguageV1.h5')

# menyiapkan gambar
img = cv2.imread(filePath)  # membaca file dengan lokasi
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # mengubah format warna dari BGR ke RGB
img = cv2.resize(img, (227, 227))  # mengatur ukuran gambar lebar * tinggi

# predict the move made
pred = model.predict(np.array([img]))
move_code = np.argmax(pred[0])
move_name = mapper(move_code)

print('prediksi : {}'.format(move_name))
