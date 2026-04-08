import numpy as np
import cv2 as cv2
from scipy import ndimage
import os
from rembg import remove
from Rorate import *
from Harris_Respon import *



directory = "Picts"
output_base = "Output"
sk = 0.0267
akn = 3.67
akl = 4.15
akm = 5.93

for root, dirs, files in os.walk(directory):
    for filename in files:
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            image_path = os.path.join(root, filename)
            image_name = filename
            
            folder_name = os.path.basename(root)
            output_folder = os.path.join(output_base, folder_name)
        
        image = remove(cv2.imread(image_path), bgcolor=(255, 255, 255, 255))
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred_image = cv2.GaussianBlur(image, (3, 3), sigmaX=1)
        blurred_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)
        thresholded_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
        
        pca = PCA_rotate(thresholded_image)
        rotated_image = PCa_rotate_image(thresholded_image, pca)
    
        # blurred_image = cv2.GaussianBlur(rotated_image, (3, 3), sigmaX=1)
        # blurred_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)
        
        Gx = Compute_Gradient_X(rotated_image)
        Gy = Compute_Gradient_Y(rotated_image)
        
        Ixx, Ixy, Iyy = AutoCorrelation(Gx, Gy)
        Harris_respon = Harris(Ixx, Ixy, Iyy)
        all_corners = thresholding(rotated_image, Harris_respon)
        
        ymin = int(np.min(all_corners[0][:, 0]))
        ymax = int(np.max(all_corners[0][:, 0]))
        xmin = int(np.min(all_corners[0][:, 1]))
        xmax = int(np.max(all_corners[0][:, 1]))

        Dx = abs(xmax - xmin)
        Dy = abs(ymax - ymin)
        
        P = Dx * sk
        L = Dy * sk
        
        keliling_x = 2 * (P + L)
        

        if folder_name == "Mas":
            berat = akm * keliling_x
        elif folder_name == "Lele":
            berat = akl * keliling_x 
        elif folder_name == "Nila":
            berat = akn * keliling_x
        else:
            berat = 0

        print(f"Gambar: {image_name}, Panjang: {P:.2f} cm, Lebar: {L:.2f} cm, Berat: {berat:.2f} gram")
        


        
        