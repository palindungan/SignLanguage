import cv2 as cv
import numpy as np

# fungsi untuk memncari lokasi dari template image didalam gambar besar

img = cv.imread('lena.jpg') # membaca file
grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # konversi warna ke gray
template = cv.imread('lena_face.jpg', 0) # membaca file template
w, h = template.shape[::-1] # mendapatkan weidth dan height

res = cv.matchTemplate(grey_img, template, cv.TM_CCOEFF_NORMED) # Membandingkan template dengan wilayah gambar yang bertumpuk.
print(res)

threshold = 0.99 # batas
loc = np.where(res >= threshold)# jika hasil lebih dari dan sama dengan 0.99 maka akan disimpan dalam variable
print(loc)

for pt in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2) # membuat bangun ruang segi empat

cv.imshow('img', img) # menampilkan gambar dengan window
cv.imshow('grey_img', grey_img) # menampilkan gambar dengan window

cv.waitKey(0) # delay
cv.destroyAllWindows() # menutup semua windows
