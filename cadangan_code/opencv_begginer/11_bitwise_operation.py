import cv2
import numpy as np

img_1 = np.zeros((250, 500, 3), np.uint8)  # membuat gambar blank
img_1 = cv2.rectangle(img_1, (200, 0), (300, 100), (255, 255, 255), -1)  # membuat bentuk geometri persegi panjang

img_2 = cv2.imread('chessboard.png')  # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)
img_2 = cv2.resize(img_2, (500, 250))  # mengatur ukuran gambar panjang * tinggi

bitAnd = cv2.bitwise_and(img_1, img_2)  # operasi AND pada 2 nilai array pixel (image 1 && image 2) (true = nilai besar , false = nilai kecil)
bitOr = cv2.bitwise_or(img_1, img_2)  # operasi OR pada 2 nilai array pixel (image 1 || image 2) (true = nilai besar , false = nilai kecil)
bitXor = cv2.bitwise_xor(img_1,img_2) # operasi XOR pada 2 nilai array pixel (image 1 || image 2) (true = nilai besar , false = nilai kecil)
bitNot1 = cv2.bitwise_not(img_1) # kebalikan dari input
bitNot2 = cv2.bitwise_not(img_2) # kebalikan dari input

cv2.imshow('img_1', img_1)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
cv2.imshow('img_2', img_2)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

cv2.imshow('bitAnd', bitAnd)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
cv2.imshow('bitOr', bitOr)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
cv2.imshow('bitXor', bitXor)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
cv2.imshow('bitNot1', bitNot1)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
cv2.imshow('bitNot2', bitNot2)  # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

cv2.waitKey(0)  # menunggu keyboard delay ms
cv2.destroyAllWindows()  # menutup semua windows yang ada
