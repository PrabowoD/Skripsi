import numpy as np
import cv2 as cv2
import math
import pandas as pd

def Manhattan (nilai1, nilai2):
    D = abs(nilai2 - nilai1)

def interpolasi (Kx, K1, K2, B1, B2) :

    KB = B1 + (B2 - B1)  * ((Kx - K1) / (K2 - K1))
    
    return KB

def keliling (panjang, lebar) :
    K = 2 * (panjang + lebar)
    
    return K