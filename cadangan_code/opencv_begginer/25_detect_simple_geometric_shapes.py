import cv2 as cv

img = cv.imread('shapes.jpg') # membaca file gambar
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY) # kovversi warna dalam greyscale
_, thresh = cv.threshold(imgGrey, 240, 255, cv.THRESH_BINARY) # jika kurang / sama dari 240 maka akan 0 , jika lebih maka akan 255 (per B G R)
contours, _ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE) # fungsi mencari contour dalam img

for contour in contours: # perulangan sebanyak isi array
    approx = cv.approxPolyDP(contour, 0.01 * cv.arcLength(contour, True), True) # memperkirakan kurva poligon dengan presisi yang ditentukan
    cv.drawContours(img, [approx], 0, (0, 0, 0), 5) # menggambar kontur yang merupakan perkiraan dari poligon approxPolyDP
    x = approx.ravel()[0] # mengubah array n-d menjadi array 1D
    y = approx.ravel()[1] - 5 # mengubah array n-d menjadi array 1D
    if len(approx) == 3: # jika perkiraan kurva poligon ada 3
        cv.putText(img, 'Triangel', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4: # jika perkiraan kurva poligon ada 4
        x1, y1, w, h = cv.boundingRect(approx) # Hitung persegi panjang pembatas kanan dari set point.
        aspectRatio = float(w) / h # perbandingan lebar dengan panjang
        # print(aspectRatio)
        if aspectRatio >= 0.95 and aspectRatio <= 1.05: # jika perbandingan mendekati 1
            cv.putText(img, 'Square', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv.putText(img, 'Rectangle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5: # jika perkiraan kurva poligon ada 5
        cv.putText(img, 'Pentagon', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10: # jika perkiraan kurva poligon ada 10
        cv.putText(img, 'Star', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else: # jika perkiraan kurva poligon tidak ada kecocokan
        cv.putText(img, 'Circle', (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

cv.imshow('img', img)
cv.imshow('imgGrey', imgGrey)

cv.waitKey(0)
cv.destroyAllWindows()
