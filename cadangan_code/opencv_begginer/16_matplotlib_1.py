import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 1) # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(bgr), -1(unchange)

cv.imshow('image', img) # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

img = cv.cvtColor(img, cv.COLOR_BGR2RGB) # konversi warna dari BGR ke RGB

plt.imshow(img) # akan menampilkan images dengan indeks array 0-5
plt.xticks([]) # menyembunyikan garis koordinak sumbu x
plt.yticks([]) # menyembunyikan garis koordinak sumbu y
plt.show() # memnampilkan semua plot

cv.waitKey(0) # menunggu keyboard delay ms
cv.destroyAllWindows() # menutup semua windows yang ada
