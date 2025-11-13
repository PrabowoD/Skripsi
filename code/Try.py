import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
from Thresholding import *
from Gradient import *
from AutoCorrelation import *
from Harris_Respon import *
from Max_Min_coordinate import *
import os
import pandas as pd

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    
    # Baca citra dari file
    image = Input_image("Picts/Clean")
    
    #Preproses citra
    #preprocessed_images = [preprocess_image(x) for x in image]
    preprocessed_images = [preprocess_image(img) for img in image]
    preprocessed_images = np.array(preprocessed_images)
    
    # Terapkan Gradient
    Gradient_X = Compute_Gradient_X(preprocessed_images)
    Gradient_Y = Compute_Gradient_Y(preprocessed_images)
    
    # Terapkan Convolusi
    Ixx = AutoCorrelation_Ixx(Gradient_X)
    Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
    Iyy = AutoCorrelation_Iyy(Gradient_Y)

    # Respon Harris
    Harris_respon = Harris(Ixx, Ixy, Iyy)
    
    # Thresholding dan Non-Maximum Suppression
    all_corners = thresholding(preprocessed_images, Harris_respon)
    
    #Max Min Coordinate
    for idx, corners in enumerate(all_corners):
        points = get_min_max_points_direct(corners)
        print(f"Gambar {idx}: {points}")
    
    center = get_center_from_bounds(points)
    print(f"Center: {center}")
    
    cc = get_center_from_corners(corners)
    print(f"Center from corners: {cc}")
    
    selected_points = select_near_center_points(corners, center)
    print(f"Selected Points near center: {selected_points}")
    
for idx, (img, R) in enumerate(zip(preprocessed_images, corners)):
    # Normalisasi R agar bisa divisualisasikan
    R_norm = cv2.normalize(R, None, 0, 255, cv2.NORM_MINMAX)
    R_norm = np.uint8(R_norm)
    
    # Konversi gambar ke warna agar bisa diberi titik merah
    if len(img.shape) == 2:  # grayscale
        img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    else:
        img_color = img.copy()
    
    for y, x in corners:
        cv2.circle(img_color, (x, y), 3, (0, 0, 255), -1)
    
    save_path = os.path.join("Output", f"corners_{idx}.png")
    cv2.imwrite(save_path, img_color)

    
for idx, (orig, corners) in enumerate(zip(image, all_corners)):
    img_vis = cv2.cvtColor(orig, cv2.COLOR_GRAY2BGR)

    points = get_min_max_points_direct(corners)
    center = get_center_from_bounds(points)
    cc = get_center_from_corners(corners)
#    selected_points = select_near_center_points(corners, center)

    # Titik ekstrem (hijau)
    for name, pt in points.items():
        cv2.circle(img_vis, pt, 6, (0, 255, 0), -1)
        cv2.putText(img_vis, name, (pt[0]+5, pt[1]-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    #Titik corners 
    for y, x in corners:
        cv2.circle(img_vis, (x, y), 2, (255, 255, 0), -1)

    # Titik tengah bounding box (biru)
    cv2.circle(img_vis, center, 6, (255, 0, 0), -1)
    cv2.putText(img_vis, "center_bounds", (center[0]+5, center[1]-5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    # Titik tengah corners (merah)
    cv2.circle(img_vis, cc, 6, (0, 0, 255), -1)
    cv2.putText(img_vis, "center_corners", (cc[0]+5, cc[1]-5),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
    
    # Titik terpilih dekat tengah (kuning)
 #   for name, pt in selected_points.items():
#        cv2.circle(img_vis, pt, 6, (0, 255, 255), -1)
#        cv2.putText(img_vis, f"sel_{name}", (pt[0]+5, pt[1]-5),
 #                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    # Simpan hasil ke folder Results
    save_path = os.path.join("Output", f"CenterMaxMix_{idx}.png")
    cv2.imwrite(save_path, img_vis)
    print(f"Gambar hasil disimpan di: {save_path}")
    
    
#for i, R in enumerate(Harris_respon):
#    print(f"Gambar {i}")
#    print("  shape :", R.shape)
#    print("  min   :", R.min())
#    print("  max   :", R.max())
#    print("  mean  :", R.mean())
 


