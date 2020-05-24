import cv2 # import library openCV

cap = cv2.VideoCapture(0) # Mengambil video dengan default camera
video_width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) # inisialisasi ukuran video
video_height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # inisialisasi ukuran video

print(video_width) # tampil pada terminal
print(video_height) # tampil pada terminal

cap.set(3,1208) # mengatur sebuah properti video dengan ID unik
cap.set(4,720) # mengatur sebuah properti video dengan ID unik

video_width = cap.get(3) # mengambil propertis video dengan menggunakan ID unik (lebar video)
video_height = cap.get(4) # mengambil propertis video dengan menggunakan ID unik (tinggi video)

print(video_width) # tampil pada terminal
print(video_height) # tampil pada terminal

## start of perulangan video
while(cap.isOpened()): # looping jika camera aktif / terbaca true

    ret,frame = cap.read() # mendapatkan gambar / frame dan status dari camera

    if ret == True: # jika berhasil membaca frame

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # mengkonversi frame ke dalam gray
        cv2.imshow('video capture',gray) # membuat windows baru dan menunjukkan video capture (per frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): # jika keyboard mendeteksi input q
            break # keluar loop

    else:
        break # keluar loop
## end of perulangan video

cap.release() # membuang memory
cv2.destroyAllWindows() # menghapus semua windows yang ada



