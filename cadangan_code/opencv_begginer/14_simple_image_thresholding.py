import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('smarties.png',0)  # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan 255 (per B G R)
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) # jika kurang / sama dari 127 maka akan 255 , jika lebih maka akan 0 (per B G R)
_, th3 = cv.threshold(img, 50, 255, cv.THRESH_TRUNC) # jika kurang / sama dari 50 maka akan tetap , jika lebih maka akan menjadi 50 (per B G R)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan tetap (per B G R)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # jika kurang / sama dari 127 maka akan tetap , jika lebih maka akan 0 (per B G R)

_, th6 = cv.threshold(img, 127, 255, 0) # sama seperti THRESH_BINARY

cv.imshow('image', img)  # memanggil windows yang berisikan gambar
cv.imshow('th1', th1)  # memanggil windows yang berisikan gambar
cv.imshow('th2', th2)  # memanggil windows yang berisikan gambar
cv.imshow('th3', th3)  # memanggil windows yang berisikan gambar
cv.imshow('th4', th4)  # memanggil windows yang berisikan gambar
cv.imshow('th5', th5)  # memanggil windows yang berisikan gambar

cv.imshow('th6', th6)  # memanggil windows yang berisikan gambar

cv.waitKey(0) # menunggu inputan keyboard
cv.destroyAllWindows() # menutup semua windows yang ada
