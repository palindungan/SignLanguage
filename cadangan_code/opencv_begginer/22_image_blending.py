import cv2 as cv
import numpy as np

apple = cv.imread('apple.jpg')
orange = cv.imread('orange.jpg')

print(apple.shape)
print(orange.shape)

apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))  # horizontal stack dengan 256(apple) > x > 256(orange)

level_gp = 6  # level dari guassian pyramid

# membuat guassian pyramid untuk apple
apple_copy = apple.copy()
gp_apple = [apple_copy]
for i in range(int(level_gp)):
    apple_copy = cv.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# membuat guassian pyramid untuk orange
orange_copy = orange.copy()
gp_orange = [orange_copy]
for i in range(int(level_gp)):
    orange_copy = cv.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

level_lp = int(level_gp) - 1  # level dari laplacian pyramid

# membuat laplacian pyramid untuk apple
apple_copy = gp_apple[level_lp]
lp_apple = [apple_copy]
for i in range(int(level_lp), 0, -1):
    gaussian_expanded = cv.pyrUp(gp_apple[i])
    laplacian = cv.subtract(gp_apple[i - 1], gaussian_expanded)
    lp_apple.append(laplacian)

# membuat laplacian pyramid untuk orange
orange_copy = gp_orange[level_lp]
lp_orange = [orange_copy]
for i in range(int(level_lp), 0, -1):
    gaussian_expanded = cv.pyrUp(gp_orange[i])
    laplacian = cv.subtract(gp_orange[i - 1], gaussian_expanded)
    lp_orange.append(laplacian)

# now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0
for apple_lap, orange_lap in zip(lp_apple, lp_orange):
    n += 1
    cols, rows, ch = apple_lap.shape
    laplacian = np.hstack((apple_lap[:, 0:int(cols / 2)], orange_lap[:, int(cols / 2):]))
    apple_orange_pyramid.append(laplacian)

# reconstruct image
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, int(level_gp)):
    apple_orange_reconstruct = cv.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv.add(apple_orange_pyramid[i], apple_orange_reconstruct)

cv.imshow('apple', apple)
cv.imshow('orange', orange)
cv.imshow('apple_orange', apple_orange)
cv.imshow('apple_orange_reconstruct', apple_orange_reconstruct)

cv.waitKey(0)
cv.destroyAllWindows()
