import cv2
import time
import numpy as np

# Start of Load Model and Image -> load the image and the model into memory.
protoFile = "hand/pose_deploy.prototxt"  # alamat file
weightsFile = "hand/pose_iter_102000.caffemodel"  # alamat file
nPoints = 22  # jumlah keyPoint
POSE_PAIRS = [[0, 1], [1, 2], [2, 3], [3, 4], [0, 5], [5, 6], [6, 7], [7, 8], [0, 9], [9, 10], [10, 11], [11, 12],
              [0, 13], [13, 14], [14, 15], [15, 16], [0, 17], [17, 18], [18, 19], [19, 20]]
frame = cv2.imread("media/images/hand.jpg")  # membaca file
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)
# End of Load Model and Image

# Start of inisialisasi variable untuk setting dimension dari gambar sebelum masuk ke neural network
frameCopy = np.copy(frame)
frameWidth = frame.shape[1]
frameHeight = frame.shape[0]
aspect_ratio = frameWidth / frameHeight

threshold = 0.1

t = time.time()
# input image dimensions for the network
inHeight = 368
inWidth = int(((aspect_ratio * inHeight) * 8) // 8)
# End of inisialisasi variable untuk setting dimension dari gambar sebelum masuk ke neural network

# Start of Get Prediction -> convert the BGR image to blob so that it can be fed to the network.
# Then we do a forward pass to get the predictions.
inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight),
                                (0, 0, 0), swapRB=False, crop=False)

net.setInput(inpBlob)

output = net.forward()
# End of Get Prediction

# Start of  Show Detections
points = []

for i in range(nPoints):
    # confidence map of corresponding body's part.
    probMap = output[0, i, :, :]
    probMap = cv2.resize(probMap, (frameWidth, frameHeight))

    # Find global maxima of the probMap.
    minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

    if prob > threshold:
        cv2.circle(frameCopy, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
        cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255),
                    2, lineType=cv2.LINE_AA)

        # Add the point to the list if the probability is greater than the threshold
        points.append((int(point[0]), int(point[1])))
    else:
        points.append(None)
        cv2.imshow('Output-Keypoints', frameCopy)
# End of  Show Detections

# Draw Skeleton
for pair in POSE_PAIRS:
    partA = pair[0]
    partB = pair[1]

    if points[partA] and points[partB]:
        cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
        cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

cv2.imshow('Skeleton', frame)

cv2.waitKey(0)
