import cv2
import numpy as np


# start of Fungsi

def click_event(event, x, y, flags, param):  # fungsi untuk menghandle click event
    if event == cv2.EVENT_LBUTTONDOWN:  # jika ada event klik kiri
        cv2.circle(img, (x, y), 5, (255, 255, 0), -1)  # mengambar circle
        points.append((x, y))  # menambah data list array
        if len(points) >= 2:  # jika array ada 2 atau lebih
            cv2.line(img, points[-1], points[-2], (255, 255, 255),
                     1)  # mengambar line dengan koordinat 2 array terakhir -> points[-1], points[-2]
            print(points)  # penampilkan tulisan pada terminal
        cv2.imshow('image', img)  # menampilkan window gambar
    elif event == cv2.EVENT_RBUTTONDOWN:  # jika ada event klik kanan
        blue = img[x, y, 0]  # mengambil warna pixel pada koordinat x,y, dengan index
        green = img[x, y, 1]  # mengambil warna pixel pada koordinat x,y, dengan index
        red = img[x, y, 2]  # mengambil warna pixel pada koordinat x,y, dengan index
        img_color[:] = [blue, green, red]  # menimpa warna pada gambar dengan warna tertentu
        cv2.imshow('color', img_color)  # menampilkan window gambar


# end of Fungsi

# start of deklarasi dan inisialisasi awal
img = cv2.imread('lena.jpg')  # membaca gambar dengan file name
img_color = np.zeros([512, 512, 3], np.uint8)  # blank image
points = []  # array
# end of deklarasi dan inisialisasi awal

cv2.imshow('image', img)  # menampilkan window gambar
cv2.setMouseCallback('image', click_event)  # membuat mouse event call back

cv2.waitKey(0)  # mendelai event wait key untuk mengeksekusi script dibawahnya
cv2.destroyAllWindows()  # menutup semua windows
