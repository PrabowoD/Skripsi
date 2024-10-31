import numpy as np
from scipy import ndimage
from Smoothing_Image import gaussian_kernel
from Convolve import apply_kernel
from Gradient import Compute_Gradient_X, Compute_Gradient_Y
from AutoCorrelation import AutoCorrelation_Ixx, AutoCorrelation_Iyy, AutoCorrelation_Ixy
from Harris_Respon import Harris

# Contoh penggunaan dengan citra buatan
if __name__ == "__main__":
    # Buat citra buatan 5x5
    image = np.array([[10, 20, 30, 40, 50],
                      [60, 70, 80, 90, 100],
                      [110, 120, 130, 140, 150],
                      [160, 170, 180, 190, 200],
                      [210, 220, 230, 240, 250]], dtype=np.float32)

    # Buat kernel Gaussian 
    kernel = gaussian_kernel(size=3, sigma=1)

    # Terapkan Gaussian smoothing
    smoothed_image = apply_kernel(image, kernel)
    
    # Terapkan Gradient
    Gradient_X = Compute_Gradient_X(smoothed_image)
    Gradient_Y = Compute_Gradient_Y(smoothed_image)
    
    # Terapkan Convolusi
    Ixx = AutoCorrelation_Ixx(Gradient_X, kernel)
    Ixy = AutoCorrelation_Ixy(Gradient_X, Gradient_Y, kernel)
    Iyy = AutoCorrelation_Iyy(Gradient_Y,kernel)
    
    # Respon Harris
    Harris_respon = Harris(Ixx, Ixy, Iyy)
    
    #Menentukan Korner
    threshold = 1e-5
    corners = np.zeros_like(Harris_respon)
    corners[Harris_respon > threshold] = 1

    # Tampilkan citra asli dan citra hasil smoothing
    print("Citra Asli:\n", image)
    print("\nKernel Gaussian:\n", kernel)
    print("\nCitra Setelah Gaussian Smoothing:\n", smoothed_image)
    print("\nHarris_respon:\n", Harris_respon)
    print("\nCorner terpilih:\n", corners)
    