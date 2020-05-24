import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)

kernel_size = 3  # jumlah size kernel
laplacian_gradient = cv.Laplacian(img, cv.CV_64F, ksize=kernel_size)  # laplacian gradient, CV_64F = tipe data slope
laplacian_gradient = np.uint8(np.absolute(laplacian_gradient))  # konversi nilai menjadi unsigned 8 bit interger

sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)  # (gradient) perubahan arah intensitas warna ada di arah x
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)  # (gradient) perubahan arah intensitas warna ada di arah y

sobelX = np.uint8(np.absolute(sobelX))  # konversi nilai menjadi unsigned 8 bit interger
sobelY = np.uint8(np.absolute(sobelY))  # konversi nilai menjadi unsigned 8 bit interger

sobelCombined = cv.bitwise_or(sobelX, sobelY)  # kombinasi sobel x dan y

titles = ['img', 'laplacian_gradient', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, laplacian_gradient, sobelX, sobelY, sobelCombined]

for i in range(len(images)):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
