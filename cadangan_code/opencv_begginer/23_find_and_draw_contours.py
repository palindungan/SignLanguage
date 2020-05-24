import cv2 as cv

img = cv.imread('opencv-logo.png')
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # perubahan warna dari BGR ke GRAYSCALE

_, tresh = cv.threshold(imgGray, 127, 255, 0) # jika kurang / sama dari 127 maka akan 0 , jika lebih maka akan 255 (per B G R)

contours, hierarchy = cv.findContours(tresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # fungsi mencari contour dalam img

print(str(len(contours)))  # jumlah contours yang ditemukan dalam gambar

cv.drawContours(img, contours, -1, (255, 255, 0), 3)  # contours id = kontur index kebrapa (urutan array). -1 = semua

cv.imshow('img', img)
cv.imshow('imgGray', imgGray)
cv.imshow('tresh', tresh)

cv.waitKey(0)
cv.destroyAllWindows()
