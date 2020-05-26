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


class ImageProcessing:
    def __init__(self, num_samples, IMG_CLASS_PATH):
        self.num_samples = num_samples
        self.IMG_CLASS_PATH = IMG_CLASS_PATH

    def image_manipulation(self, frame, count):
        roi = frame[100:500, 100:500]  # img[y:y+h, x:x+w]
        # save_path = os.path.join(self.IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        # cv2.imwrite(save_path, roi)  # menyimpan file dataset satu persatu

    def video_capture(self):
        cap = cv2.VideoCapture(0)  # membuka camera
        start = False
        count = 0

        while cap.isOpened():
            ret, frame = cap.read()

            # validasi jika gagal mengambil gambar/frame
            if not ret:
                continue  # semua proses akan melewati(skip) dan kembali ke perulangan selanjutnya

            # validasi jika jumlah dataset sudah memenuhi kriteria yang diinginkan
            if count == self.num_samples:
                break  # keluar dari proses perulangan

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
