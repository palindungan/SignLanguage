import cv2 as cv

# read the input image
cap = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

while (cap.isOpened()):
    ret, img = cap.read()

    if ret == True:
        gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray_img, 1.1, 4)
        for (x, y, w, h) in faces:
            cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

        cv.imshow('img', img)

        key = cv.waitKey(40) & 0xFF
        if key == ord('q'):
            break

    else:
        break

cap.release()
cv.destroyAllWindows()
