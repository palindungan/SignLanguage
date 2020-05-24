import cv2 as cv
import numpy as np


# ////////////// start of logic /////////////

def nothing(x):
    pass


cap = cv.VideoCapture(0)

winTrackName = 'Track Bar'
cv.namedWindow(winname=winTrackName)

cv.createTrackbar('THRESH', winTrackName, 0, 255, nothing)
cv.createTrackbar('MAXVAL', winTrackName, 0, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)

    threshVal = cv.getTrackbarPos(trackbarname='THRESH', winname=winTrackName)
    maxVal = cv.getTrackbarPos(trackbarname='MAXVAL', winname=winTrackName)

    _, thResult = cv.threshold(src=frame, thresh=threshVal, maxval=maxVal, type=cv.THRESH_BINARY_INV)

    contours, _ = cv.findContours(image=thResult.copy(), mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

    hull = [cv.convexHull(points=c) for c in contours]

    finalResult = cv.drawContours(image=frame, contours=hull, contourIdx=-1, color=(255, 0, 0))

    if ret == True:
        cv.imshow(winname='Original Image', mat=frame)
        cv.imshow(winname='Thresh', mat=thResult)
        cv.imshow(winname='Convex Hull', mat=finalResult)

        key = cv.waitKey(delay=1) & 0xff
        if key == 27:
            break

cap.release()
cv.destroyAllWindows()
