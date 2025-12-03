import numpy as np
import cv2 as cv2
import math

def Manhattan (nilai1, nilai2):
    D = abs(nilai2 - nilai1)

def interpolasi (DataX, DataY, Npanjang, Nlebar) :
    
    panjangX = df.loc["panjang"]
    lebarX = df.loc["lebar"]
    beratX = df.loc["berat"]
    
    panjangY = df.loc["panjang"]
    lebarY = df.loc["lebar"]
    beratY = df.loc["berat"]
    
    LB = beratX + (beratY - beratX)  * ((Npanjang - panjangX) / (panjangX - panjangY))
    PB = beratX + (beratY - beratY) * ((Nlebar - lebarX) / (lebarX - lebarY))
    
    Nberat = (LB + PB) / 2
    
    return Nberat

def keliling (panjang, lebar)
    K = 2 * (panjang + lebar)
    
    return K