import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE) # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)

_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV) # membuat mask dengan thresholding binary inverse
v_kernel = np.ones((10,10),np.uint8) # membuat array image dengan size x,y dan tipe uint8

dilation = cv.dilate(mask, v_kernel, iterations=1) # untuk menambah / pelebaran batas dari foreground
erosion = cv.erode(mask, v_kernel, iterations=1) # untuk mengurangi / mengikis batas dari foreground
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, v_kernel) # melakukan fungsi erosi kemudian mendilasi gambar (mask)
closing = cv.morphologyEx(mask, cv.MORPH_CLOSE, v_kernel) # melakukan fungsi dilasi kemudian mengerosi gambar (mask)
m_gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, v_kernel) # melakukan fungsi pengurangan antara dilasi dan erosi
topHat = cv.morphologyEx(mask, cv.MORPH_TOPHAT, v_kernel) # melakukan fungsi pengurangan antara source(mask) dan opening

titles = ['img', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'm_gradient', 'topHat'] # array berisikan string judul dari sub plot(image)
images = [img, mask, dilation, erosion, opening, closing, m_gradient, topHat] # array berisikan gambar yang akan ditampilkan

for i in range(len(images)): # sesuai jumlah gambar
    plt.subplot(2, 4, i + 1) # membuat subplot(plot didalam plot) (x, y, z) dengan x baris y kolom , dan indeks z
    plt.imshow(images[i], 'gray') # akan menampilkan images dengan indeks array
    plt.title(titles[i]) # memberi judul pada gambar
    plt.xticks([]) # menyembunyikan garis koordinak sumbu x
    plt.yticks([]) # menyembunyikan garis koordinak sumbu y

plt.show() # memnampilkan semua plot
