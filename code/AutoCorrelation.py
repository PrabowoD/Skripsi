import numpy as np
from scipy import ndimage

def AutoCorrelation_Ixx(Ix, kernel):

    #Menghitung Convolusi
    Ixx = Ix**2

    #Pengaplikasian Gaussian
    Ixx = ndimage.convolve(Ixx, kernel)

    return Ixx

def AutoCorrelation_Ixy(Ix, Iy, kernel):

    #Menghitung Convolusi
    Ixy = Ix * Iy
    
    #Pengaplikasian Gaussian
    Ixy = ndimage.convolve(Ixy, kernel)

    return Ixy

def AutoCorrelation_Iyy(Iy, kernel):

    #Menghitung Convolusi
    Iyy = Iy**2
    
    #Pengaplikasian Gaussian
    Iyy = ndimage.convolve(Iyy, kernel)

    return Iyy