import cv2 as cv
import numpy as np

img = cv.imread('shapes.jpg')
img = cv.resize(img, (512, 512))  # mengatur ukuran gambar panjang * tinggi

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

corners = cv.goodFeaturesToTrack(gray, 25, 0.01, 10)

corners = np.int0(corners)

for i in corners:
    x, y = i.ravel()
    cv.circle(img, (x, y), 3, 255, -1)

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
