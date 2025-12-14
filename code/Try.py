import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
from Thresholding import *
from Gradient import *
from AutoCorrelation import *
from Harris_Respon import *
from Max_Min_coordinate import *
from Rorate import *
import os
import pandas as pd

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    
    # Baca citra dari file
    
    folder = "Picts/Koin"
    image_paths = [os.path.join(folder, f) for f in os.listdir(folder)
                   if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    
    for idx, img in enumerate(image_paths):
        
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        
        filename = os.path.basename(img)
        
    #Preproses citra
        preprocessed_images = [preprocess_image(image)]
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
        pca_angle = PCA_rotate(all_corners[0])
        rotated_pca_image = PCa_rotate_image(preprocessed_images[0], pca_angle)
        
        save_path = os.path.join("Output/Rotated", filename)
        cv2.imwrite(save_path, rotated_pca_image)


    #Max Min Coordinate
    
    Fls = "Output/Rotated"
    imps = [os.path.join(Fls, f) for f in os.listdir(Fls)
                   if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    #df = pd.ExcelFile("Size_ikan.xlsx")
    sk = 0.0138
    
    for idx, img in enumerate(imps):
        
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        filename = os.path.basename(img)
        #image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        
        pre = [preprocess_image(image)]
        pre = np.array(pre)
        
        Gradient_X = Compute_Gradient_X(pre)
        Gradient_Y = Compute_Gradient_Y(pre)
        
        Ixx = AutoCorrelation_Ixx(Gradient_X)
        Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
        Iyy = AutoCorrelation_Iyy(Gradient_Y)
        
        Harris_respon = Harris(Ixx, Ixy, Iyy)
        all_corners = thresholding(pre, Harris_respon)
    
        points = get_min_max_points_direct(all_corners[0])
        print(f"Gambar {idx}: {points}")
    
        center = get_center_from_bounds(points)
        print(f"Center: {center}")
    
        cc = get_center_from_corners(all_corners[0])
        print(f"Center from corners: {cc}")

        ymin = int(np.min(all_corners[0][:, 0]))
        ymax = int(np.max(all_corners[0][:, 0]))
        xmin = int(np.min(all_corners[0][:, 1]))
        xmax = int(np.max(all_corners[0][:, 1]))
        
        print(np.min(all_corners[0], axis=0))
        print(np.max(all_corners[0], axis=0))
        Dx =  abs(xmax - xmin)
        Dy = abs(ymax - ymin)

        save_path = os.path.join("Output/Box", filename)
        box = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 0), 2)
        cv2.imwrite(save_path, box)
        print(Dx, Dy)

        P = Dx * sk
        L = Dy * sk
        
        keliling_x = 2 * (P + L)
        
        print(f"panjang (P) : {P} cm")
        print(f"lebar (L) : {L} cm")
        print(f"Keliling ikan (Kx) : {keliling_x} cm")
        
        # Sd = pd.read_excel(df, sheet_name="Nila")
        # Sd = Sd.sort_values(by="keliling").reset_index(drop=True)
        # Kdbawah = Sd[Sd["keliling"] <= keliling_x]
        # Kdatas = Sd[Sd["keliling"] >= keliling_x]

        # if not Kdbawah.empty:
        #     titik_bawah = Kdbawah.iloc[-1]    # nilai keliling terbesar yang <= keliling_x
        # else:
        #         titik_bawah = None

        # if not Kdatas.empty:
        #     titik_atas = Kdatas.iloc[0]       # nilai keliling terkecil yang >= keliling_x
        # else:
        #     titik_atas = None
        

        # print(f"Keliling Data Bawah (Kdb) : {Kdbawah.values} cm")
        # print(f"Keliling Data Atas (Kda) : {Kdatas.values} cm")

        # if idx == "Nila":
        #     Sd = pd.read_excel("Size_ikan.xlsx", sheet_name="Nila")
        #     Kd = Sd["keliling"]
        # elif idx == "Lele":
        #     Sd = pd.read_excel("Size_ikan.xlsx", sheet_name="Lele")
        #     Kd = Sd["keliling"]
        # elif idx == "Mas":
        #     Sd = pd.read_excel("Size_ikan.xlsx", sheet_name="Mas")
        #     Kd = Sd["keliling"]
        # else:
        #     Sd = None

    
#for i, R in enumerate(Harris_respon):
#    print(f"Gambar {i}")
#    print("  shape :", R.shape)
#    print("  min   :", R.min())
#    print("  max   :", R.max())
#    print("  mean  :", R.mean())
 


