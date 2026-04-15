import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
from Harris_Respon import *
from Max_Min_coordinate import *
from rembg import remove
import os
import pandas as pd

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    
    # Baca citra dari file
    
    folder = "Picts"
    image_paths = [os.path.join(folder, f) for f in os.listdir(folder)
                   if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    
    for idx, img in enumerate(image_paths):
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        
        filename = os.path.basename(img)
        
        image = remove(image, bgcolor=(255, 255, 255, 255))
        
    #Preproses citra
        GaussianSmooths = [GaussianSmooth(image)]
        GaussianSmooths = np.array(GaussianSmooths)
    
    # Terapkan Gradient
        Gradient_X = Compute_Gradient_X(GaussianSmooths)
        Gradient_Y = Compute_Gradient_Y(GaussianSmooths)
    
    # Terapkan Convolusi
        # Ixx = AutoCorrelation_Ixx(Gradient_X)
        # Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
        # Iyy = AutoCorrelation_Iyy(Gradient_Y)
        Ixx, Ixy, Iyy = AutoCorrelation(Gradient_X, Gradient_Y)

    # Respon Harris
        Harris_respon = Harris(Ixx, Ixy, Iyy)
    
    # Thresholding dan Non-Maximum Suppression
        all_corners = thresholding(GaussianSmooths, Harris_respon)
        # pca_angle = PCA_rotate(all_corners[0])
        rotated_pca_image = PCa_rotate_image(GaussianSmooths[0], all_corners[0])
        
        # os.makedirs(output_folder, exist_ok=True)
        save_path = os.path.join("Output/Rotated/UjiCoba", filename)
        cv2.imwrite(save_path, rotated_pca_image)


    #Max Min Coordinate
    
    Fls = "Output/Rotated/UjiCoba"
    imps = [os.path.join(Fls, f) for f in os.listdir(Fls)
                   if f.lower().endswith((".jpg", ".png", ".jpeg"))]
    #df = pd.ExcelFile("Size_ikan.xlsx")
    sk = 0.0138
    # berat_dict = {"Mas": 5.93, "Lele": 4.15, "Nila": 3.67}
    akm = 5.93
    akl_induk = 7.20
    akl_pembesar = 4.41
    akl_pedaging = 2.46
    akn_induk = 5.70
    akn_kdua  = 3.38
    akn_kbawah = 2.73
    
    for idx, img in enumerate(imps):
        
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        filename = os.path.basename(img)
        filename = filename.lower()
        # folder_name = os.path.basename(os.path.dirname(img))
        # folder_name = folder_name.lower()
        # image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # blurred_image = cv2.GaussianBlur(image, (3, 3), sigmaX=1)
        # blurred_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)
        # image = np.array(blurred_image)
        # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        
        GaussianSmooths = [GaussianSmooth(image)]
        GaussianSmooths = np.array(GaussianSmooths)
        
        Grad_X = Compute_Gradient_X(GaussianSmooths)
        Grad_Y = Compute_Gradient_Y(GaussianSmooths)
        
        # Ixx = AutoCorrelation_Ixx(Gradient_X)
        # Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
        # Iyy = AutoCorrelation_Iyy(Gradient_Y)
        
        xx, xy, yy = AutoCorrelation(Grad_X, Grad_Y)
        
        Harespon = Harris(xx, xy, yy)
        all_corners = thresholding(GaussianSmooths, Harespon)
    
        # points = get_min_max_points_direct(all_corners[0])
        # print(f"Gambar {idx}: {points}")
    
        # center = get_center_from_bounds(points)
        # print(f"Center: {center}")
    
        # cc = get_center_from_corners(all_corners[0])
        # print(f"Center from corners: {cc}")

        ymin = int(np.min(all_corners[0][:, 0]))
        ymax = int(np.max(all_corners[0][:, 0]))
        xmin = int(np.min(all_corners[0][:, 1]))
        xmax = int(np.max(all_corners[0][:, 1]))
        
        print(np.min(all_corners[0], axis=0))
        print(np.max(all_corners[0], axis=0))
        Dx = abs(xmax - xmin)
        Dy = abs(ymax - ymin)

        save_path = os.path.join("Output/Box", filename)
        box = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 0), 5)
        cv2.imwrite(save_path, box)
        print(Dx, Dy)

        P = Dx * sk
        L = Dy * sk
        
        luas = P * L
        keliling_x = 2 * (P + L)
        # Berat = akn * keliling_x
        # for Berat in filename:
        print(f"Gambar {idx} : {filename}")
        print(f"panjang (P) : {P} cm")
        print(f"lebar (L) : {L} cm")
        print(f"Keliling ikan (Kx) : {keliling_x} cm")
        print(f"Luas ikan : {luas} cm^2")
        
        
        Berat = 0
        if "mas" in filename:
                Berat = akm * keliling_x
        elif "lele" in filename and "induk" in filename:
                Berat = akl_induk * keliling_x
        elif "lele" in filename and "pembesaran" in filename:
            Berat = akl_pembesar * keliling_x
        elif "lele" in filename and "pedaging" in filename:
            Berat = akl_pedaging * keliling_x
        elif "nila" in filename and "induk" in filename:
                Berat = akn_induk * keliling_x
        elif "nila" and "kdua" in filename:
            Berat = akn_kdua * keliling_x
        elif "nila" and "kbawah" in filename:
            Berat = akn_kbawah * keliling_x
        else:
                break
        # if "mas" in filename:
        #         Berat = akm * luas
        # elif "lele" in filename:
        #         Berat = akl * luas
        # elif "nila" in filename:
        #         Berat = akn * luas
        # else:
        #         break

            


        print(f"Berat ikan : {Berat} gram")
        
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
 


