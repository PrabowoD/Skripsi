import numpy as np
import cv2 as cv2
from scipy import ndimage
import os
from rembg import remove
from Rorate import *
from Harris_Respon import *



directory = "UjiCoba/Input"
output_base = "UjiCoba/Output"
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

        gray = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2GRAY)
        blurred_images = cv2.GaussianBlur(gray, (3, 3), sigmaX=1)
        blurred_images = cv2.normalize(blurred_images, None, 0, 255, cv2.NORM_MINMAX)
        
        
        Gx = Compute_Gradient_X(blurred_images)
        Gy = Compute_Gradient_Y(blurred_images)
        
        # if Gx.ndim == 3:
        #     Gx = Gx[:,:, 0]
        # if Gy.ndim == 3:
        #     Gy = Gy[:,:, 0]
        
        Ixx, Ixy, Iyy = AutoCorrelation(Gx, Gy)
        
        # if Ixx.ndim == 3:
        #     Ixx = Ixx[:,:, 0]
        # if Ixy.ndim == 3:
        #     Ixy = Ixy[:,:, 0]
        # if Iyy.ndim == 3:
        #     Iyy = Iyy[:,:, 0]
        
        Harris_respon = Harris(Ixx, Ixy, Iyy)
        all_corners = thresholding(blurred_images, Harris_respon)
        
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
        


        
        