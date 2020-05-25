desc = '''
*script untuk mengumpulkan data gambar dengan lebel tertentu.

Cara Running : - python gather_images.py <nama_label> <jumlah_sampel>

*script akan menyimpan gambar didalam folder sesuai <nama_label> dengan <jumlah_sampel> yang sudah ditentukan

*hanya sebagian gambar yang berada didalam kotak yang akan disimpan

*tekan 'a' untuk memulai/pause proses mengambilan data gambar
*tekan 'q' untuk keluar dari proses mengambilan data gambar
'''

import cv2
import os
import sys

# validasi awal running program
try:
    # menangkap data argument sesuai dengan urutan index
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])
except:
    print("Argument Missing")
    print(desc)
    exit(-1)  # terjadi kesalahan/error/masalah yang membuat program exit/keluar

IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

'''
IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass
try:
    os.mkdir(IMG_CLASS_PATH)
except FileExistsError:
    print("{} directory already exists.".format(IMG_CLASS_PATH))
    print("All images gathered will be saved along with existing items in this folder")
'''
