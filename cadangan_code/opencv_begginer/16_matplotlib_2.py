import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', 0)  # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan 255 (per B G R)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # jika kurang / sama dari 127 maka akan 255 , jika lebih maka akan 0 (per B G R)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC) # jika kurang / sama dari 50 maka akan tetap , jika lebih maka akan menjadi 50 (per B G R)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan tetap (per B G R)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # jika kurang / sama dari 127 maka akan tetap , jika lebih maka akan 0 (per B G R)

titles = ['Original', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV'] # array berisikan string judul dari sub plot(image)
images = [img, th1, th2, th3, th4, th5] # array berisikan gambar yang akan ditampilkan

for i in range(6): # sesuai jumlah gambar
    plt.subplot(2, 3, i + 1) # membuat subplot(plot didalam plot) dengan 2 baris 3 kolom , dan indeks 1-6
    plt.imshow(images[i], 'gray') # akan menampilkan images dengan indeks array 0-5
    plt.title(titles[i]) # memberi judul pada gambar
    plt.xticks([]) # menyembunyikan garis koordinak sumbu x
    plt.yticks([]) # menyembunyikan garis koordinak sumbu y

plt.show() # memnampilkan semua plot
