import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
# from Smoothing_Image import *
# from Convolve import *
from Gradient import *
from AutoCorrelation import *
from Harris_Respon import *
import os

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    
    # Baca citra dari file
    image = Input_image("Picts/Clean")
    
    #Preproses citra
    preprocessed_images = [preprocess_image(image) for image in image]
    
    # Terapkan Gradient
    Gradient_X = Compute_Gradient_X(preprocessed_images)
    Gradient_Y = Compute_Gradient_Y(preprocessed_images)
    
    # Terapkan Convolusi
    Ixx = AutoCorrelation_Ixx(Gradient_X)
    Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
    Iyy = AutoCorrelation_Iyy(Gradient_Y)

    # Respon Harris
    Harris_respon = Harris(Ixx, Ixy, Iyy)
    
for idx, (img, R) in enumerate(zip(preprocessed_images, Harris_respon)):
    # Normalisasi R agar bisa divisualisasikan
    R_norm = cv2.normalize(R, None, 0, 255, cv2.NORM_MINMAX)
    R_norm = np.uint8(R_norm)

    # Thresholding untuk menandai titik sudut
    thresh = 0.01 * R.max()
    mask = (R > thresh).astype(np.uint8)
    dilated = cv2.dilate(R, None)
    nms_mask = (R == dilated) & (R > thresh)
    corners = np.argwhere(nms_mask)

    # Konversi gambar ke warna agar bisa diberi titik merah
    if len(img.shape) == 2:  # grayscale
        img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        img_color = img.copy()

    # Tandai sudut dengan warna merah
    for y, x in corners:
        cv2.circle(img_color, (x, y), 3, (0, 0, 255), -1)

    # Simpan hasil ke file
    save_path = os.path.join("Output", f"corners_{idx}.png")
    cv2.imwrite(save_path, img_color)
    
    print(f"Hasil gambar {idx} disimpan ke {save_path}")

    print(f"Gambar {idx}: {len(corners)} sudut terdeteksi")
    
for i, R in enumerate(Harris_respon):
    print(f"Gambar {i}")
    print("  shape :", R.shape)
    print("  min   :", R.min())
    print("  max   :", R.max())
    print("  mean  :", R.mean())


