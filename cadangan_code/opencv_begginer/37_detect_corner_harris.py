import cv2 as cv
import numpy as np

img = cv.imread('chessboard.png')
img = cv.resize(img, (512, 512))  # mengatur ukuran gambar panjang * tinggi

cv.imshow('img', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 2, 3, 0.04)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

if cv.waitKey(0) & 0xFF == 27:
    cv.destroyAllWindows()
