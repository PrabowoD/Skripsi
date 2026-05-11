import numpy as np
import cv2 as cv2
import math
import pandas as pd

# def Manhattan (nilai1, nilai2):
#     D = abs(nilai2 - nilai1)

# def interpolasi (Kx, K1, K2, B1, B2) :

#     KB = B1 + (B2 - B1)  * ((Kx - K1) / (K2 - K1))
    
#     return KB

# def keliling (panjang, lebar) :
#     K = 2 * (panjang + lebar)
    
#     return K

def calculate_weight(Luas, filename):
    alm = 2.00
    all_induk = 2.00
    all_pembesar = 1.59
    all_pedaging = 1.07
    aln_induk = 1.29
    aln_kdua  = 1.13
    aln_kbawah = 1.08
    
    Berat = 0
    if "mas" in filename:
            Berat = alm * Luas
    elif "lele" in filename and "induk" in filename:
            Berat = all_induk * Luas
    elif "lele" in filename and "pembesaran" in filename:
        Berat = all_pembesar * Luas
    elif "lele" in filename and "pedaging" in filename:
        Berat = all_pedaging * Luas
    elif "nila" in filename and "induk" in filename:
        #if "nila" in filename and "induk" in filename:
            Berat = aln_induk * Luas
    elif "nila" and "kdua" in filename:
        Berat = aln_kdua * Luas
    elif "nila" and "kbawah" in filename:
        Berat = aln_kbawah * Luas
    else:
            return None
    
    return Berat


def calculate_size(corners):
    sk = 0.0138
    
    ymin = int(np.min(corners[:, 0]))
    ymax = int(np.max(corners[:, 0]))
    xmin = int(np.min(corners[:, 1]))
    xmax = int(np.max(corners[:, 1]))
    
    height = abs(ymax - ymin) * sk
    width = abs(xmax - xmin) * sk
    
    return height, width
