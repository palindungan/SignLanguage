import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
# img = np.zeros((200, 200), np.uint8)  # membuat gambar dengan semua (200*200) value bernilai 0
# cv.rectangle(img, (0, 100), (200, 200), (255), -1)
# cv.rectangle(img, (0, 50), (100, 100), (127), -1)

# b, g, r = cv.split(img) # memisahkan nilai value img menjadi b, g, r
#
# cv.imshow('img', img)
# cv.imshow('b', b)
# cv.imshow('g', g)
# cv.imshow('r', r)
#
# plt.hist(b.ravel(), 256, [0, 256])  # membuat histogram dengan nilai value max 256 dan range 0-256
# plt.hist(g.ravel(), 256, [0, 256])  # membuat histogram dengan nilai value max 256 dan range 0-256
# plt.hist(r.ravel(), 256, [0, 256])  # membuat histogram dengan nilai value max 256 dan range 0-256

hist = cv.calcHist([img], [0], None, [256], [0, 256])  # Menghitung histogram dari satu set array.
plt.plot(hist) # Plot y , x sebagai garis atau spidol.

plt.show()  # menampilkan matplotlib

cv.waitKey(0)
cv.destroyAllWindows()
