import cv2 as cv

img = cv.imread('lena.jpg')

# /// Start of perubahan resolusi image (pyramid) dengan gaussian1
# lowR1 = cv.pyrDown(img) # menurunkan resolusi image dengan defaut 1/4*resolusi
# lowR2 = cv.pyrDown(lowR1) # menurunkan resolusi image dengan defaut 1/4*resolusi
# highR1 = cv.pyrUp(lowR2) # meningkatkan resolusi image dengan defaut 1/4*resolusi

# cv.imshow('lowR1', lowR1)
# cv.imshow('lowR2', lowR2)
# cv.imshow('highR1', highR1)
# /// End of perubahan resolusi image (pyramid) dengan gaussian1


# /// Start of perubahan resolusi image (pyramid) dengan gaussian2
# layer = img.copy() # mennyalin nilai image
# gaussianP = [layer] # menyimpan nilai value (array) dari setiap perubahan layer (img - pydown)

# for i in range(5):
#     layer = cv.pyrDown(layer) # menurunkan resolusi image dengan defaut 1/4*resolusi
#     gaussianP.append(layer) # menyimpan nilai array dari layer image yang sudah di turunkan resolusinya
#     cv.imshow(str(i), layer)
# /// End of perubahan resolusi image (pyramid) dengan gaussian2


# /// Start of perubahan resoluso image(pyramid) dengan laplacian
layer = img.copy()  # mennyalin nilai image
gaussianP = [layer]  # menyimpan nilai value (array) dari setiap perubahan layer (img - pydown)

for i in range(6):  # 0,1,2,3,4,5
    layer = cv.pyrDown(layer)  # menurunkan resolusi image dengan defaut 1/4*resolusi
    gaussianP.append(layer)  # menyimpan nilai array dari layer image yang sudah di turunkan resolusinya

# layer = gaussianP[5]  # mengambil top of pyramid / last array
# laplacianP = [layer]

for i in range(5, 0, -1):  # start, stop , step(decrease|increase) hasil = 5,4,3,2,1
    gaussianExtended = cv.pyrUp(gaussianP[i]) # menaikkan resolusi image dengan defaut 1/4*resolusi
    laplacianLayer = cv.subtract(gaussianP[i - 1], gaussianExtended)
    cv.imshow(str(i), laplacianLayer)
# /// End of perubahan resoluso image(pyramid) dengan laplacian

# print(gaussianP)
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()
