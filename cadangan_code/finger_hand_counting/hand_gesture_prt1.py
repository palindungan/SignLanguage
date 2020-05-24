# import cv2 -> Open Source Computer Vision atau yang dikenal dengan OpenCV merupakan salah satu library yang -
# digunakan pada ilmu tentang Computer Vision.
import cv2 as cv

# import numpy -> library Python yang fokus pada scientific computing. NumPy memiliki kemampuan untuk membentuk -
# objek N-dimensional array, yang mirip dengan list pada Python.
import numpy as np

# ////////////// start of logic /////////////

# fungsi membaca file dan langsung mengkonversi menjadi grey scale
hand = cv.imread(filename='Capture.png', flags=0)

# Metode thresholding dengan inputan image GREY SCALE dengan tipe THRESH_BINARY.
# -- THRESH_BINARY -> jika kurang / sama dari nilai thresh= maka akan 0 , jika lebih maka akan maxval=
_, the = cv.threshold(src=hand, thresh=70, maxval=255, type=cv.THRESH_BINARY)

# mencari kontur dengan inputan image binary yang sudah di tresholding, mode= RETR_TREE, method= CHAIN_APPROX_SIMPLE
# -- RETR_TREE -> It retrieves all the contours and creates a full family hierarchy list. It even tells,
# who is the grandpa, father, son, grandson and even beyond... :).
# -- cv.CHAIN_APPROX_SIMPLE -> removes all redundant points and compresses the contour, thereby saving memory.
# If you pass cv.CHAIN_APPROX_NONE, all the boundary points are stored.
contours, _ = cv.findContours(image=the.copy(), mode=cv.RETR_TREE, method=cv.CHAIN_APPROX_SIMPLE)

# create hull array for convex hull points -> calculate points for each contour
# -> creating convex hull object for each contour
hull = [cv.convexHull(points=c) for c in contours]

# The final step is to visualize the convex hulls we have just found. Of course a convex hull itself is -
# just a contour and therefore we can use OpenCV’s drawContours.
final = cv.drawContours(image=hand, contours=hull, contourIdx=-1, color=(255, 0, 0))

cv.imshow(winname='Original Image', mat=hand)
cv.imshow(winname='Thresh', mat=the)
cv.imshow(winname='Convex Hull', mat=final)

cv.waitKey(delay=0)
cv.destroyAllWindows()
