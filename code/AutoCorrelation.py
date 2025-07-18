import numpy as np
import cv2

def AutoCorrelation_Ixx(Ix_list):
    Ixx_list = []
    for Ix in Ix_list:
        Ixx = Ix ** 2
        Ixx_list.append(Ixx)
    return Ixx_list

def AutoCorrelation_Ixy(Ix_list, Iy_list):
    Ixy_list = []
    for Ix, Iy in zip(Ix_list, Iy_list):
        Ixy = Ix * Iy
        Ixy_list.append(Ixy)
    return Ixy_list

def AutoCorrelation_Iyy(Iy_list):
    Iyy_list = []
    for Iy in Iy_list:
        Iyy = Iy ** 2
        Iyy_list.append(Iyy)
    return Iyy_list
