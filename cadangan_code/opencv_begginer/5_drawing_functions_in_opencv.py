import cv2 # library opencv
import numpy as np # perhitungan matematis

# start of deklarasi awal
nama_file_gambar_1 = 'lena.jpg' # nama file
text_1 = 'OpenCV' # text
font_1 = cv2.FONT_HERSHEY_COMPLEX # tipe font
# end of deklarasi awal

# img = cv2.imread(nama_file_gambar_1,1) # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)
img = np.zeros([512,512,3],np.uint8) # membuat gambar blank

# start of fungsi untuk override gambar dan membuat bentuk geometri pada gambar
img = cv2.line(img,(0,0),(255,255),(255,0,0),10) # membuat garis pada sebuah gambar
img = cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),5) # membuat garis berarah pada sebuah gambar
img = cv2.rectangle(img,(384,0),(510,128),(0,0,255),10) # membuat bentuk geometri persegi panjang
img = cv2.circle(img,(447,63),63,(0,255,0),-1) # membuat bentuk geometri bundar
img = cv2.putText(img,text_1,(10,500),font_1,4,(255,0,0),10,cv2.LINE_AA)
# end of fungsi untuk override gambar dan membuat bentuk geometri pada gambar

cv2.imshow('gambar 1',img) # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

cv2.waitKey(0) # menunggu keyboard delay ms
cv2.destroyAllWindows() # menutup semua windows yang ada
