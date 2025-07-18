import numpy as np
import cv2 as cv2
from scipy import ndimage
from Pre_Processing import *
from Smoothing_Image import *
from Convolve import *
from Gradient import *
from AutoCorrelation import *
from Harris_Respon import *

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    
    # Baca citra dari file
    image = Input_image("Picts")
    
    #Preproses citra
    preprocessed_images = [preprocess_image(img) for img in image]
    
    # Terapkan Gradient
    Gradient_X = Compute_Gradient_X(preprocessed_images)
    Gradient_Y = Compute_Gradient_Y(preprocessed_images)
    
    # Terapkan Convolusi
    Ixx = AutoCorrelation_Ixx(Gradient_X)
    Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y)
    Iyy = AutoCorrelation_Iyy(Gradient_Y)

    # Respon Harris
    Harris_respon = Harris(Ixx, Ixy, Iyy)
    
    #Menentukan Korner
    threshold = 0.01 * np.max(Harris_respon[0])
    corners_list = []
for response in Harris_respon:
    corners = np.zeros_like(response)
    corners[response > threshold] = [0, 0, 255]
    corners_list.append(corners)

