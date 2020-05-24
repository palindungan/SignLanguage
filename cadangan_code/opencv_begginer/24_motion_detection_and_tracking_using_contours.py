import cv2 as cv

cap = cv.VideoCapture('vtest.avi') # mengcapture video yang berasal dari file video

ret, frame1 = cap.read() # inisialisasi membaca frame 1 dari video capture
ret, frame2 = cap.read() # inisialisasi membaca frame 2 dari video capture

while cap.isOpened():

    diff = cv.absdiff(frame1, frame2) # Perbedaan absolut antara dua array , punya ukuran dan jenis yang sama
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY) # konversi warna ke grayscale
    blurr = cv.GaussianBlur(gray, (5, 5), 0) # fungsi blurring dengan algoritma GaussianBlur
    _, thresh = cv.threshold(blurr, 20, 255, cv.THRESH_BINARY)  # jika kurang / sama dari 20 maka akan 0 , jika lebih maka akan 255 (per B G R)
    dilated = cv.dilate(thresh, None, iterations=3) # untuk menambah / pelebaran batas dari foreground
    contours, _ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # fungsi mencari contour dalam img

    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour) # Hitung persegi panjang pembatas kanan dari set point.

        if cv.contourArea(contour) < 700: # Menghitung area kontur.
            continue

        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2) # membuat bentuk geometri persegi panjang
        cv.putText(frame1, "Status : {}".format('Movement'), (10, 20), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # cv.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    cv.imshow('feed', frame1) # untuk memunculkan gambar dengan parameter : nama windows , variable gambar
    frame1 = frame2 #
    ret, frame2 = cap.read() # membaca frame dari video capture

    key = cv.waitKey(40) & 0xFF # mengunggu delay
    if key == 27: # detect si inputan keyboard dengan code 27
        break

cap.release()
cv.destroyAllWindows()
