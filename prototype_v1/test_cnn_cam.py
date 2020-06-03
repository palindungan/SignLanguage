import cv2  # image processing
import numpy as np  # array operation
from keras.models import load_model

window_name_tracking = 'Tracking Warna Kulit'

REV_CLASS_MAP = {  # reverse dari variable CLASS_MAP
    0: 'none',
    1: 'one-hand-A',
    2: 'one-hand-B',
    3: 'one-hand-C',
    4: 'one-hand-D',
}

model = load_model('modelSignLanguageV1.h5')


def mapper(key):  # fungsi untuk mengambil nilai
    return REV_CLASS_MAP[key]


def nothing(x):
    pass


def image_manipulation(frame):
    roi = frame[100:500, 100:500]  # img[y:y+h, x:x+w] --> crop image

    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # konversi warna dari BGR -> HSV

    lower_h = cv2.getTrackbarPos('LH', window_name_tracking)  # mendapatkan posisi trackbar
    lower_s = cv2.getTrackbarPos('LS', window_name_tracking)  # mendapatkan posisi trackbar
    lower_v = cv2.getTrackbarPos('LV', window_name_tracking)  # mendapatkan posisi trackbar

    upper_h = cv2.getTrackbarPos('UH', window_name_tracking)  # mendapatkan posisi trackbar
    upper_s = cv2.getTrackbarPos('US', window_name_tracking)  # mendapatkan posisi trackbar
    upper_v = cv2.getTrackbarPos('UV', window_name_tracking)  # mendapatkan posisi trackbar

    # mendefinisikan range dari warna kulit dalam hsv
    lower_skin = np.array([lower_h, lower_s, lower_v], dtype=np.uint8)
    upper_skin = np.array([upper_h, upper_s, upper_v], dtype=np.uint8)

    # ekstraksi warna kulit pada gambar
    mask = cv2.inRange(hsv, lower_skin, upper_skin)

    # # extrapolate the hand to fill dark spots within
    # kernel = np.ones((3, 3), np.uint8)
    # mask = cv2.dilate(mask, kernel, iterations=4)
    #
    # # blur the image
    # mask = cv2.GaussianBlur(mask, (5, 5), 100)

    res = cv2.bitwise_and(roi, roi, mask=mask)  # hasil akhir operasi gambar dengan mask

    # mencocokkan image dengan cnn
    img_cnn = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    img_cnn = cv2.resize(img_cnn, (227, 227))

    # predict the move made
    pred = model.predict(np.array([img_cnn]))
    move_code = np.argmax(pred[0])
    move_name = mapper(move_code)

    print('prediksi : {}'.format(move_name))

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)


def video_capture():
    cap = cv2.VideoCapture(0)  # membuka camera
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)  # mengatur sebuah properti video (video_width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # mengatur sebuah properti video (video_height)

    start = False

    cv2.namedWindow(window_name_tracking)  # membuat window dengan nama

    cv2.createTrackbar('LH', window_name_tracking, 0, 255, nothing)  # membuat trackbar
    cv2.createTrackbar('LS', window_name_tracking, 61, 255, nothing)  # membuat trackbar
    cv2.createTrackbar('LV', window_name_tracking, 0, 255, nothing)  # membuat trackbar

    cv2.createTrackbar('UH', window_name_tracking, 73, 255, nothing)  # membuat trackbar
    cv2.createTrackbar('US', window_name_tracking, 255, 255, nothing)  # membuat trackbar
    cv2.createTrackbar('UV', window_name_tracking, 255, 255, nothing)  # membuat trackbar

    while cap.isOpened():
        ret, frame = cap.read()

        # validasi jika gagal mengambil gambar/frame
        if not ret:
            continue  # semua proses dibawahnya akan dilewati(skip) dan kembali ke perulangan selanjutnya

        cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)  # membuat bangun segi empat pada frame

        # validasi proses pengambilan dataset
        if start:
            image_manipulation(frame)  # proses memanipulasi gambar

        # menambah text pada gambar/frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, 'prediksi : {} dataset'.format('hasil'), (0, 50), font, 0.7, (0, 255, 255), 2,
                    cv2.LINE_AA)

        cv2.imshow("Frame Utama", frame)  # menampilkan gambar/frame kedalam layar

        # validasi untuk memulai/berhenti/keluar dari pemrosesan dataset
        k = cv2.waitKey(10)
        if k == ord('a'):
            start = not start  # mengubah nilai boolean start menjadi sebaliknya ->True/False
        elif k == ord('q'):
            break  # keluar dari proses perulangan

    cap.release()
    cv2.destroyAllWindows()


video_capture()
