import cv2
import datetime

vid_cap = cv2.VideoCapture(0)

frame_width = 1208
frame_height = 720

vid_cap.set(cv2.CAP_PROP_FRAME_WIDTH, frame_width)
vid_cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frame_height)

font = cv2.FONT_HERSHEY_COMPLEX

while vid_cap.isOpened():
    ret, frame = vid_cap.read()

    if ret == True:

        # text = 'Width : ' + str(frame_width) + ' Height: ' + str(frame_height)
        text = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10, 50), font, 2, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow('web cam 1', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break

    else:
        break

cv2.destroyAllWindows()
vid_cap.release()
