import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
from Harris_Respon import *
from Max_Min_coordinate import *
from rembg import remove
from pands import transform_size
import os
import pandas as pd
from Calculated import calculate_size, calculate_weight

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
    alm = 2.00
    all_induk = 2.00
    all_pembesar = 1.59
    all_pedaging = 1.07
    aln_induk = 1.29
    aln_kdua  = 1.13
    aln_kbawah = 1.08
    
    for idx, img in enumerate(imps):
        
        image = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        filename = os.path.basename(img)
        # filename = os.path.splitext(filename)[0]
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
        
        print(f"Gambar {idx} : {filename}")
        # print(np.min(all_corners[0], axis=0))
        # print(np.max(all_corners[0], axis=0))
        Dx = abs(xmax - xmin)
        Dy = abs(ymax - ymin)

        save_path = os.path.join("Output/Box", filename)
        box = cv2.rectangle(image, (xmin, ymin), (xmax, ymax), (0, 0, 0), 5)
        cv2.imwrite(save_path, box)
        # print(Dx, Dy)

        P = Dx * sk        
        L = Dy * sk
        
        transformed_values = transform_size("Size_ikan.xlsx", P, L, Fls)
        # Pt, Lt = transform_size("Size_ikan.xlsx", P, L, Fls)
        
        # if "nila" in filename:
        #     Pt, Lt = transform_size("Size_ikan.xlsx", "Nila", Fls, P, L)
        # elif "lele" in filename:
        #     Pt, Lt = transform_size("Size_ikan.xlsx", "Lele", Fls, P, L)
        # elif "mas" in filename:
        #     Pt, Lt = transform_size("Size_ikan.xlsx", "Mas", Fls, P, L)
        
        # else:
        #     break
        # luas = 0
        # keliling_x = 0
        filename = os.path.splitext(filename)[0]
        # +".jpg"
        for img in transformed_values:
            if img[0] == filename:       
                luas = img[1] * img[2]
                keliling_x = 2 * (img[1] + img[2])
                Cw = calculate_weight(luas, img[0])
                
                print(f"panjang (P) : {img[1]} cm")
                print(f"lebar (L) : {img[2]} cm")
                print(f"Keliling ikan (Kx) : {keliling_x} cm")
                print(f"Luas ikan : {luas} cm^2")
                print(f"Berat ikan : {Cw} gram")
                
        # Berat = akn * keliling_x
        # for Berat in filename:
        # print(f"Gambar {idx} : {filename}")
        print(f"panjang deteksi (Pd) : {P} cm")
        print(f"lebar deteksi (Ld) : {L} cm")

        
        
        # Berat = 0
        # if "mas" in filename:
        #         Berat = alm * luas
        # elif "lele" in filename and "induk" in filename:
        #         Berat = all_induk * luas
        # elif "lele" in filename and "pembesaran" in filename:
        #     Berat = all_pembesar * luas
        # elif "lele" in filename and "pedaging" in filename:
        #     Berat = all_pedaging * luas
        # elif "nila" in filename and "induk" in filename:
        # #if "nila" in filename and "induk" in filename:
        #         Berat = aln_induk * luas
        # elif "nila" and "kdua" in filename:
        #     Berat = aln_kdua * luas
        # elif "nila" and "kbawah" in filename:
        #     Berat = aln_kbawah * luas
        # else:
        #         break
        # if "mas" in filename:
        #         Berat = akm * luas
        # elif "lele" in filename:
        #         Berat = akl * luas
        # elif "nila" in filename:
        #         Berat = akn * luas
        # else:
        #         break

            



        
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
 


