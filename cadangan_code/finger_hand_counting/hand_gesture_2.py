import cv2 as cv  # library open computer vision untuk pengolahan citra
import math  # mengakses fungsi dan proses matematik
import numpy as np  # pengolahan array -> data


# def click_event(event, x, y, flags, param):
#     if cv.EVENT_LBUTTONDOWN:
#         text = str(x) + ', ' + str(y)
#         font = cv.FONT_ITALIC
#         cv.putText(frame, text, (x, y), font, 2, (255, 0, 255), 3)
#         cv.imshow('Original', frame)

def nothing(x):
    pass


kernel_size = 5
cap = cv.VideoCapture(0)

window_name_tracking = 'Tracking'
cv.namedWindow(window_name_tracking)  # membuat window dengan nama

# inisialisasi trackbar
cv.createTrackbar('LH', window_name_tracking, 0, 255, nothing)
cv.createTrackbar('LS', window_name_tracking, 76, 255, nothing)
cv.createTrackbar('LV', window_name_tracking, 30, 255, nothing)

cv.createTrackbar('UH', window_name_tracking, 53, 255, nothing)
cv.createTrackbar('US', window_name_tracking, 255, 255, nothing)
cv.createTrackbar('UV', window_name_tracking, 255, 255, nothing)

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        # membuat bangun segi empat -> cv.rectangle(img, (x1,y1), (x2,y2), (B,G,R), thickness)
        # (x1,y1) = pojok kiri atas , (x2,y2) = pojok kanan bawah (dari bangun segi empat)
        cv.rectangle(frame, (100, 100), (300, 300), (0, 255, 0), 0)
        crop_image = frame[100:300, 100:300]  # img[y:y+h, x:x+w]

        # penerapan Gaussian Blur
        # cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )
        blur = cv.GaussianBlur(crop_image, (kernel_size, kernel_size), 0)

        # merubah warna dari BGR ke HSV
        # cv.cvtColor(src, code[, dst[, dstCn]])
        hsv = cv.cvtColor(blur, cv.COLOR_BGR2HSV)

        # mendapatkan nilai dari trackbar
        lower_h = cv.getTrackbarPos('LH', window_name_tracking)
        lower_s = cv.getTrackbarPos('LS', window_name_tracking)
        lower_v = cv.getTrackbarPos('LV', window_name_tracking)

        upper_h = cv.getTrackbarPos('UH', window_name_tracking)
        upper_s = cv.getTrackbarPos('US', window_name_tracking)
        upper_v = cv.getTrackbarPos('UV', window_name_tracking)

        # membuat array dengan nilai yang berasal dari trackbar berfungsi sebagai penentu batas
        lower_b = np.array([lower_h, lower_s, lower_v])
        upper_b = np.array([upper_h, upper_s, upper_v])

        # membuat mask gambar biner dari proses thresholding dengan menggunakan HSV
        # cv.inRange(src, lowerb, upperb[, dst])
        image_mask = cv.inRange(hsv, lower_b, upper_b)

        # Kernel untuk morphological transformations
        kernel = np.ones((5, 5))

        # menerapkan morphological transformations untuk menghilangkan noise
        dilation = cv.dilate(image_mask, kernel, iterations=1)  # melebaran
        erosion = cv.erode(dilation, kernel, iterations=1)  # menipisan / pengikisan

        # penerapan Gaussian Blur
        # cv.GaussianBlur(src, ksize, sigmaX[, dst[, sigmaY[, borderType=BORDER_DEFAULT]]] )
        filtered = cv.GaussianBlur(erosion, (3, 3), 0)
        # penerapan simple image thresholding
        # ret, thresh1 = cv2.threshold(img, thresh, maxval, tipe)
        ret, thresh = cv.threshold(filtered, 127, 255, 0)

        # mencari contours
        # image, contours = cv.findContours(image, mode, method[, contours[, hierarchy[, offset]]])
        contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        try:
            # mencari key(ID) dari value luas(cv.contourArea(x)) kontur yang paling besar -> key= key-n : value-n
            # max(iterable, *iterables, key, default)
            contour = max(contours, key=lambda x: cv.contourArea(x))

            # Membuat bounding rectangle disekitar kontur
            x, y, w, h = cv.boundingRect(contour)
            cv.rectangle(crop_image, (x, y), (x + w, y + h), (0, 0, 255), 0)

            # Find convex hull
            hull = cv.convexHull(contour)

            # Draw contour
            drawing = np.zeros(crop_image.shape, np.uint8)
            cv.drawContours(drawing, [contour], -1, (0, 255, 0), 0)
            cv.drawContours(drawing, [hull], -1, (0, 0, 255), 0)

            # Find convexity defects
            hull = cv.convexHull(contour, returnPoints=False)
            defects = cv.convexityDefects(contour, hull)

            # Use cosine rule to find angle of the far point from the start and end point i.e. the convex points (the finger
            # tips) for all defects
            count_defects = 0

            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(contour[s][0])
                end = tuple(contour[e][0])
                far = tuple(contour[f][0])

                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = (math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 180) / 3.14

                # if angle > 90 draw a circle at the far point
                if angle <= 90:
                    count_defects += 1
                    cv.circle(crop_image, far, 1, [0, 0, 255], -1)

                cv.line(crop_image, start, end, [0, 255, 0], 2)

            # Print number of fingers
            if count_defects == 0:
                cv.putText(frame, "SATU", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            elif count_defects == 1:
                cv.putText(frame, "DUA", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            elif count_defects == 2:
                cv.putText(frame, "TIGA", (5, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            elif count_defects == 3:
                cv.putText(frame, "EMPAT", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            elif count_defects == 4:
                cv.putText(frame, "LIMA", (50, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
            else:
                pass
        except:
            pass

        # memunculkan gambar
        cv.imshow('Original', frame)
        cv.imshow('crop_image', crop_image)
        cv.imshow('blur', blur)
        cv.imshow('image_mask', image_mask)
        cv.imshow('dilation', dilation)
        cv.imshow('erosion', erosion)
        cv.imshow("Thresholded", thresh)
        # all_image = np.hstack((drawing, crop_image))
        cv.imshow('Contours', drawing)

        key = cv.waitKey(1) & 0xff
        if key == 27:
            break

cap.release()
cv.destroyAllWindows()
