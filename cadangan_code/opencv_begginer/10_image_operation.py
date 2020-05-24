import cv2
import numpy as np


# start of function

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        text = str(x) + ', ' + str(y)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(img, text, (x, y), font, 0.5, (0, 0, 0), 1)
        cv2.imshow('image', img)


# end of function

img = cv2.imread('lena.jpg')  # membaca file gambar
img2 = cv2.imread('opencv-logo.png')  # membaca file gambar

print(img.shape)  # mereturn nilai lebar pixel, panjang pixel, dan 3 merupakan channel gambar (RGB)
print(img.size)  # mereturn jumlah seluruh pixel yang ada pada gambar
print(img.dtype)  # mereturn nilai data type pada gambar (uint8)
b, g, r = cv2.split(img)  # memecah nilai BGR pada gambar (treshold)
img = cv2.merge((b, g, r))  # menggabungkan nilai BGR menjadi gambar baru

eye = img[255:281, 316:350]  # [y1:y2 ,x1:x2] -> mengambil nilai pixel pada bagian gambar
img[355:381, 316:350] = eye  # menimpa nilai pixel dengan pixel lain

img = cv2.resize(img, (512, 512))  # mengatur ukuran gambar panjang * tinggi
img2 = cv2.resize(img2, (512, 512))  # mengatur ukuran gambar panjang * tinggi

# img_dst = cv2.add(img,img2) # menambah nilai pixel(array) 2 buah gambar
img_dst = cv2.addWeighted(img, 0.90, img2, 0.10,
                          0)  # menambah nilai pixel(array treshold) 2 buah gambar + di beri seberapa persen dominasi gambar (alpha , beta , gamma)

cv2.imshow('image', img_dst)  # menampilkan gambar pada windows 'image'

cv2.setMouseCallback('image', click_event)  # membuat inisialisasi event action mouse

cv2.waitKey(0)  # delay , mencegah fungsi selanjutmnya di eksekusi (menunggu inputan keyboard / mouse event)
cv2.destroyAllWindows()  # menutup semua windows yang terbuka
