import numpy as np
from scipy import ndimage

# 1. Sobel Kernel
def Compute_Gradient_X(Image):
    # Sobel kernel untuk menghitung gradien
    Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    
    
    Ix = ndimage.convolve(Image, Kx)

    return Ix

def Compute_Gradient_Y(Image):
    Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    
    Iy = ndimage.convolve(Image,Ky)
    
    return Iy