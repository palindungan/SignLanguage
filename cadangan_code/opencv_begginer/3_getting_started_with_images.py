import cv2 # library opencv

img = cv2.imread('lena.jpg',0) # untuk membaca gambar dan disimpan dalam variable , parameter : 0 (greyscale) , 1(rgb), -1(unchange)
cv2.imshow('foto',img) # untuk memunculkan gambar dengan parameter : nama windows , variable gambar

key = cv2.waitKey(0) # menunggu keyboard delay ms

if key == ord('k'): # membaca inputan keyboard
    cv2.destroyAllWindows() # menutup semua windows yang ada
elif key == ord('s'):  # membaca inputan keyboard
    cv2.imwrite('lena_grayscale.png',img) # membuat gambar baru
    cv2.destroyAllWindows() # menutup semua windows yang ada




