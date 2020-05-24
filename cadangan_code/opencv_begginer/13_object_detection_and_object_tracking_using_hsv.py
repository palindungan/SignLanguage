import cv2
import numpy as np


# start of function

def nothing(x):
    pass


# end of function

cap = cv2.VideoCapture(0)  # menangkap dari video device ke 0 (kamera default)

windowNameTracking = 'Tracking'
cv2.namedWindow(windowNameTracking)  # membuat window dengan nama

cv2.createTrackbar('LH', windowNameTracking, 0, 255, nothing)  # membuat trackbar
cv2.createTrackbar('LS', windowNameTracking, 0, 255, nothing)  # membuat trackbar
cv2.createTrackbar('LV', windowNameTracking, 0, 255, nothing)  # membuat trackbar

cv2.createTrackbar('UH', windowNameTracking, 255, 255, nothing)  # membuat trackbar
cv2.createTrackbar('US', windowNameTracking, 255, 255, nothing)  # membuat trackbar
cv2.createTrackbar('UV', windowNameTracking, 255, 255, nothing)  # membuat trackbar

while True:

    # frame = cv2.imread('smarties.png')
    _, frame = cap.read()  # membaca setiap gambar yang ditangkap pada kamera dan disimpan pada variable ret (true/false) , frame (frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # konversi warna dari BGR ke HSV

    l_h = cv2.getTrackbarPos('LH', windowNameTracking)  # mendapatkan posisi trackbar
    l_s = cv2.getTrackbarPos('LS', windowNameTracking)  # mendapatkan posisi trackbar
    l_v = cv2.getTrackbarPos('LV', windowNameTracking)  # mendapatkan posisi trackbar

    u_h = cv2.getTrackbarPos('UH', windowNameTracking)  # mendapatkan posisi trackbar
    u_s = cv2.getTrackbarPos('US', windowNameTracking)  # mendapatkan posisi trackbar
    u_v = cv2.getTrackbarPos('UV', windowNameTracking)  # mendapatkan posisi trackbar

    l_b = np.array([l_h, l_s, l_v])  # menentukan batas bawah nilai HSV
    u_b = np.array([u_h, u_s, u_v])  # menentukan atas atas nilai HSV

    v_mask = cv2.inRange(hsv, l_b, u_b)  # membuat mask dari gambar HSV sesuai batas bawah dan atas
    res = cv2.bitwise_and(frame, frame, mask=v_mask)  # hasil akhir operasi gambar dengan mask

    cv2.imshow('image', frame)  # memanggil windows yang berisikan gambar
    cv2.imshow('mask', v_mask)  # memanggil windows yang berisikan gambar
    cv2.imshow('res', res)  # memanggil windows yang berisikan gambar

    key = cv2.waitKey(1) & 0xff  # menunggu inputan keyboard
    if key == 27:  # jika esc ditekan
        break

cap.release()  # menutup kamera
cv2.destroyAllWindows()  # menutup semua windows yang ada
