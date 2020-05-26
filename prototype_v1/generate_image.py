desc = '''
*script untuk mengumpulkan data gambar dengan lebel tertentu.

Cara Running : - python gather_images.py <nama_label> <jumlah_sampel>

*script akan menyimpan gambar didalam folder sesuai <nama_label> dengan <jumlah_sampel> yang sudah ditentukan

*hanya sebagian gambar yang berada didalam kotak yang akan disimpan

*tekan 'a' untuk memulai/berhenti proses mengambilan data gambar
*tekan 'q' untuk keluar dari proses mengambilan data gambar
'''

import cv2  # image processing
import os  # memanipulasi operating system
import sys  # menangkap arguments/parse
import numpy as np


class ImageProcessing:
    def __init__(self, num_samples, IMG_CLASS_PATH):
        self.num_samples = num_samples
        self.IMG_CLASS_PATH = IMG_CLASS_PATH
        self.window_name_tracking = 'Tracking'

    def nothing(self, x):
        pass

    def hsv_boundary_tracker(self):

        cv2.namedWindow(self.window_name_tracking)  # membuat window dengan nama

        cv2.createTrackbar('LH', self.window_name_tracking, 0, 255, self.nothing)  # membuat trackbar
        cv2.createTrackbar('LS', self.window_name_tracking, 0, 255, self.nothing)  # membuat trackbar
        cv2.createTrackbar('LV', self.window_name_tracking, 0, 255, self.nothing)  # membuat trackbar

        cv2.createTrackbar('UH', self.window_name_tracking, 255, 255, self.nothing)  # membuat trackbar
        cv2.createTrackbar('US', self.window_name_tracking, 255, 255, self.nothing)  # membuat trackbar
        cv2.createTrackbar('UV', self.window_name_tracking, 255, 255, self.nothing)  # membuat trackbar

    def image_manipulation(self, frame, count):
        roi = frame[100:500, 100:500]  # img[y:y+h, x:x+w] --> crop image

        hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)  # konversi warna dari BGR -> HSV

        lower_h = cv2.getTrackbarPos('LH', self.window_name_tracking)  # mendapatkan posisi trackbar
        lower_s = cv2.getTrackbarPos('LS', self.window_name_tracking)  # mendapatkan posisi trackbar
        lower_v = cv2.getTrackbarPos('LV', self.window_name_tracking)  # mendapatkan posisi trackbar

        upper_h = cv2.getTrackbarPos('UH', self.window_name_tracking)  # mendapatkan posisi trackbar
        upper_s = cv2.getTrackbarPos('US', self.window_name_tracking)  # mendapatkan posisi trackbar
        upper_v = cv2.getTrackbarPos('UV', self.window_name_tracking)  # mendapatkan posisi trackbar

        # define range of skin color in HSV
        lower_skin = np.array([lower_h, lower_s, lower_v], dtype=np.uint8)
        upper_skin = np.array([upper_h, upper_s, upper_v], dtype=np.uint8)

        # extract skin colur image
        mask = cv2.inRange(hsv, lower_skin, upper_skin)

        # # extrapolate the hand to fill dark spots within
        # kernel = np.ones((3, 3), np.uint8)
        # mask = cv2.dilate(mask, kernel, iterations=4)
        #
        # # blur the image
        # mask = cv2.GaussianBlur(mask, (5, 5), 100)

        res = cv2.bitwise_and(roi, roi, mask=mask)  # hasil akhir operasi gambar dengan mask

        cv2.imshow('mask', mask)
        cv2.imshow('res', res)

        # save_path = os.path.join(self.IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        # cv2.imwrite(save_path, roi)  # menyimpan file dataset satu persatu

    def video_capture(self):
        cap = cv2.VideoCapture(0)  # membuka camera
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1208)  # mengatur sebuah properti video (video_width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)  # mengatur sebuah properti video (video_height)

        start = False
        count = 0

        self.hsv_boundary_tracker()

        while cap.isOpened():
            ret, frame = cap.read()

            # validasi jika gagal mengambil gambar/frame
            if not ret:
                continue  # semua proses akan melewati(skip) dan kembali ke perulangan selanjutnya

            # validasi jika jumlah dataset sudah memenuhi kriteria yang diinginkan
            # if count == self.num_samples:
            #     break  # keluar dari proses perulangan

            cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)  # membuat bangun segi empat pada frame

            # validasi proses pengambilan dataset
            if start:
                self.image_manipulation(frame, count)
                count += 1

            # menambah text pada gambar/frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, 'Mengumpulkan : {} dataset'.format(count), (0, 50), font, 0.7, (0, 255, 255), 2,
                        cv2.LINE_AA)

            cv2.imshow("Frame Utama", frame)  # menampilkan gambar/frame kedalam layar

            # validasi untuk memulai/berhenti/keluar dari pemrosesan dataset
            k = cv2.waitKey(10)
            if k == ord('a'):
                start = not start  # mengubah nilai boolean start menjadi sebaliknya ->True/False
            elif k == ord('q'):
                break  # keluar dari proses perulangan

        print('\n{} image(s) saved to {}'.format(count, self.IMG_CLASS_PATH))
        cap.release()
        cv2.destroyAllWindows()


def main():
    # validasi awal pada saat menerima data arguments
    try:
        # menangkap data argument sesuai dengan urutan index
        label_name = sys.argv[1]
        num_samples = int(sys.argv[2])
    except:
        print("Argument Missing")
        print(desc)
        exit(-1)  # terjadi kesalahan/error/masalah yang membuat program exit/keluar

    IMG_SAVE_PATH = 'image_data'  # lokasi absolute path --> home untuk semua dataset
    IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)  # lokasi tempat data gambar hasil program disimpan

    # proses + validasi ketika membuat folder untuk dataset yang berhasil disimpan
    try:
        os.mkdir(IMG_SAVE_PATH)  # membuat folder kumpulan semua dataset
    except FileExistsError:
        pass
    try:
        os.mkdir(IMG_CLASS_PATH)  # membuat folder kumpulan dataset sesuai label
    except FileExistsError:
        print('{} directory already exists.'.format(IMG_CLASS_PATH))
        print('All images gathered will be saved along with existing items in this folder')

    # memanggil class ImageProcessing
    IP = ImageProcessing(num_samples, IMG_CLASS_PATH)
    IP.video_capture()


# memanggil main method
main()
