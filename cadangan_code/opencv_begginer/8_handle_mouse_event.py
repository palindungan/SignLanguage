import cv2
import numpy as np


# events = [i for i in dir(cv2) if 'EVENT' in i]
# print(events)

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:

        text = str(x) + ' , ' + str(y)
        font = cv2.FONT_ITALIC
        cv2.putText(img, text, (x, y), font, 2, (255, 0, 255), 3)
        cv2.imshow('image', img)

    elif event == cv2.EVENT_RBUTTONDOWN:

        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        text = str(blue) + ' , ' + str(green) + ' , ' + str(red)
        font = cv2.FONT_HERSHEY_PLAIN
        cv2.putText(img, text, (x, y), font, 0.5, (255, 255, 0), 1)
        cv2.imshow('image',img)

# img = np.zeros((512, 512, 3), np.uint8)
img  = cv2.imread('lena.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event) # meng inisialisasi mouse callback pada windows yang ditunjuk (harus sudah ada windowsnya)

cv2.waitKey(0)
cv2.destroyAllWindows()
