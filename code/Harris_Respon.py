import numpy as np

def Harris(Ixx, Ixy, Iyy, k=0.04):
    #Menghitung Harris Respon
    Det_M = Ixx * Iyy - Ixy**2
    Tr_M = Ixx + Iyy
    
    Harrisrespon = Det_M - k * (Tr_M**2)

    
    return Harrisrespon