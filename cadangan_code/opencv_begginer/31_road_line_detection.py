import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np


def region_of_interest(img, vertices):
    mask = np.zeros_like(img)
    channel_count = img.shape[2]
    match_mask_color = (255,) * channel_count
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


image = cv.imread('road_2.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

region_of_interest_vertices = [
    (0, height),
    (width / 2, height / 2),
    (width, height)
]

cropped_image = region_of_interest(image,
                             np.array([region_of_interest_vertices], np.int32))

plt.imshow(cropped_image)
plt.show()
