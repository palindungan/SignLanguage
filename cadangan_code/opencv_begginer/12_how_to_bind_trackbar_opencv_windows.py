import cv2 as cv
import numpy as np


# start of function

def callBackFunction(x):
    print(x)


# end of function

# img = np.zeros((250, 500, 3), np.uint8)  # membuat gambar blank
windowNameImage = 'image'
cv.namedWindow(windowNameImage)  # membuat window dengan nama

# cv.createTrackbar('B', windowNameImage, 0, 255, callBackFunction)  # membuat trackbar
# cv.createTrackbar('G', windowNameImage, 0, 255, callBackFunction)  # membuat trackbar
# cv.createTrackbar('R', windowNameImage, 0, 255, callBackFunction)  # membuat trackbar
cv.createTrackbar('CP', windowNameImage, 10, 400, callBackFunction)  # membuat trackbar

# switch = '0 : OFF\n 1: ON'  # variable nama switch
switch2 = 'color/grayscale'  # variable nama switch
# cv.createTrackbar(switch, windowNameImage, 0, 1, callBackFunction)  # membuat switch dengan trackbar
cv.createTrackbar(switch2, windowNameImage, 0, 1, callBackFunction)  # membuat switch dengan trackbar

while (1):
    img = cv.imread('lena.jpg')

    k = cv.waitKey(1) & 0xff  # menunggu keyboard delay ms
    if k == 27:  # jika inputan keyboard aktif (esc)
        break  # keluar looping

    # b = cv.getTrackbarPos('B', windowNameImage)  # mendapatkan posisi trackbar
    # g = cv.getTrackbarPos('G', windowNameImage)  # mendapatkan posisi trackbar
    # r = cv.getTrackbarPos('R', windowNameImage)  # mendapatkan posisi trackbar

    cp = cv.getTrackbarPos('CP', windowNameImage)  # mendapatkan posisi trackbar
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(cp), (50, 300), font, 5, (255, 255, 255), 10)

    # s = cv.getTrackbarPos(switch, windowNameImage)  # mendapatkan posisi trackbar
    # if s == 0:
    #     img[:] = 0  # mengeset nilai warna image (treshold) BGR
    # else:
    #     img[:] = (b, g, r)  # mengeset nilai warna image (treshold) BGR

    s1 = cv.getTrackbarPos(switch2, windowNameImage)  # mendapatkan posisi trackbar
    if s1 == 0:
        pass
    else:
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow(windowNameImage, img)  # memanggil windows yang berisikan gambar

cv.destroyAllWindows()  # menghapus semua windows
