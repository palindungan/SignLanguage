import cv2 as cv

img = cv.imread('sudoku.png',0)  # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan 255 (per B G R)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2) # adaptive threshold = region threshold
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) # adaptive threshold = region threshold

cv.imshow('img', img) # memanggil windows yang berisikan gambar
cv.imshow('th1', th1) # memanggil windows yang berisikan gambar
cv.imshow('th2', th2) # memanggil windows yang berisikan gambar
cv.imshow('th3', th3) # memanggil windows yang berisikan gambar

cv.waitKey(0) # menunggu inputan keyboard
cv.destroyAllWindows() # menutup semua windows yang ada
