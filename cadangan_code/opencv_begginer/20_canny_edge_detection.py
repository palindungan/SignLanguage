import cv2 as cv
from matplotlib import pyplot as plt


def nothing(x):
    pass


windowNameTrackbar = 'Trackbar'
cv.namedWindow(windowNameTrackbar) # membuat windows
cv.createTrackbar('TH1', windowNameTrackbar, 0, 255, nothing) # membuat sebuah trackbar
cv.createTrackbar('TH2', windowNameTrackbar, 0, 255, nothing) # membuat sebuah trackbar

while True:

    frame = cv.imread('butterfly.jpg', cv.IMREAD_GRAYSCALE) # membaca file dan mengkonversi dalam bentuk grayscale

    th1 = cv.getTrackbarPos('TH1', windowNameTrackbar) # memdapatkan nilai pada trackbar yang sedang dituju
    th2 = cv.getTrackbarPos('TH2', windowNameTrackbar) # memdapatkan nilai pada trackbar yang sedang dituju

    canny = cv.Canny(frame, th1, th2) # edge detection dengan algoritma canny

    cv.imshow('frame', frame)
    cv.imshow('canny', canny)

    key = cv.waitKey(1) & 0xff  # menunggu inputan keyboard
    if key == 27:  # jika esc ditekan
        break

cv.destroyAllWindows()
