import cv2 as cv
import numpy as np

# logic :
# 1. edge detection
# 2. mapping of edges point to the hough space and storage to an accumulator
# 3. interpretation of the accumulator to yield lines of infinite lenght.
#    the interpretation is done by thresholding and possibly other constrains
# 4. convertion of infinite lines to finite lines

img = cv.imread('sudoku.png')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 50, 150, apertureSize=3)
lines = cv.HoughLines(edges, 1, np.pi / 180, 200, )

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))  # x1 stores the rounded off value of (r * cos(theta) - 1000 * sin(theta))
    y1 = int(y0 + 1000 * (a))  # y1 stores the rounded off value of (r * sin(theta) + 1000 * cos(theta))
    x2 = int(x0 - 1000 * (-b))  # x2 stores the rounded off value of (r * cos(theta) + 1000 * sin(theta))
    y2 = int(y0 - 1000 * (a))  # y2 stores the rounded off value of (r * sin(theta) - 1000 * cos(theta))
    cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv.imshow('img', img)
cv.imshow('edges', edges)

cv.waitKey(0)
cv.destroyAllWindows()
