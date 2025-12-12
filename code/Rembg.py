from rembg import remove
import cv2 as cv2
import os



path = "Picts/Koin"

for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        full_path = os.path.join(path, filename)
        image = cv2.imread(full_path)
    # Menghapus latar belakang menggunakan rembg
        output = remove(image, bgcolor=(255, 255, 255, 255))
    # Menyimpan gambar hasil dengan latar belakang putih
        save_path = os.path.join("Output/Rembg", filename)
        cv2.imwrite(save_path, output)

