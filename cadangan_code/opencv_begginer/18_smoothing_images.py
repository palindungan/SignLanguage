import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg')  # untuk membaca gambar dan disimpan dalam variable
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)  # konversi warna dari BGR ke RGB

size_kernel = 5  # ukuran matrik kernel -> penentu tingkat blurr (harus ganjil kecuali 1)
kernel = np.ones((size_kernel, size_kernel), np.float32) / (size_kernel * size_kernel)  # rumus k

dst = cv.filter2D(img, -1, kernel)  # fungsi blurring dengan filter 2D (teknik homogeneus filter)
blur = cv.blur(img, (size_kernel, size_kernel))  # fungsi blurring dengan method blur / averaging
gblur = cv.GaussianBlur(img, (size_kernel, size_kernel), 0)  # fungsi blurring dengan algoritma GaussianBlur
median = cv.medianBlur(img, size_kernel)  # fungsi blurring yang cocok untuk salt and papper noise (median theory)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75) # untuk meningkatkan edge (sharp) dan noise removal

titles = ['img', '2D Convolution', 'blur', 'gblur', 'median', 'bilateralFilter']  # array berisikan string judul dari sub plot(image)
images = [img, dst, blur, gblur, median, bilateralFilter]  # array berisikan gambar yang akan ditampilkan

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)  # membuat subplot(plot didalam plot) (x, y, z) dengan x baris y kolom , dan indeks z
    plt.imshow(images[i])  # akan menampilkan images dengan indeks array
    plt.title(titles[i])  # memberi judul pada gambar
    plt.xticks([])  # menyembunyikan garis koordinak sumbu x
    plt.yticks([])  # menyembunyikan garis koordinak sumbu y

plt.show()  # memnampilkan semua plot
