import cv2 # library opencv

cap = cv2.VideoCapture(0); # menangkap dari video device ke 0 (kamera default)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # mendapatkan propertis dari frame (width) dan konversi dalam int
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # mendapatkan propertis dari frame (height) dan konversi dalam int

fourcc = cv2.VideoWriter_fourcc(*'XVID') # kode video fourcc https://www.fourcc.org/codecs.php

out = cv2.VideoWriter('output.avi',fourcc,20.0,(frame_width,frame_height)) # inisialisasi membuat video

while(cap.isOpened()): # jika file bisa terbaca / benar
    ret,frame = cap.read() # membaca setiap gambar yang ditangkap pada kamera dan disimpan pada variable ret (true/false) , frame (frame)

    if ret == True:
        print(frame_width) # mendapatkan propertis dari frame (width)
        print(frame_height) # mendapatkan propertis dari frame (height)

        out.write(frame) # menyimpan frame dalam video writer

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # mengkonversi warna ke dalam grayscale dari frame berwarna

        cv2.imshow('video capture',gray) # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

        if cv2.waitKey(1) == ord('q'): # jika mendeteksi input keyboard tertentu
            break # keluar dari fungsi loop
    else:
        break

cap.release() # melepaskan semua resource capture
out.release() # melepaskan semua resource video writer
cv2.destroyAllWindows() # menutup semua windows yang ada
