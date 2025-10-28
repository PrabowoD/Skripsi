import numpy as np
import cv2

def AutoCorrelation_Ixx(Ix_list):
    Ixx_list = []
    for Ix in Ix_list:
        Ixx = Ix ** 2
        Ixx = cv2.GaussianBlur(Ixx, (3, 3), sigmaX=1)
        Ixx_list.append(Ixx)
    return np.stack(Ixx_list, axis=0)

def AutoCorrelation_Ixy(Ix_list, Iy_list):
    Ixy_list = []
    for Ix, Iy in zip(Ix_list, Iy_list):
        Ixy = Ix * Iy
        Ixy = cv2.GaussianBlur(Ixy, (3, 3), sigmaX=1)
        Ixy_list.append(Ixy)
    return np.stack(Ixy_list, axis=0)

def AutoCorrelation_Iyy(Iy_list):
    Iyy_list = []
    for Iy in Iy_list:
        Iyy = Iy ** 2
        Iyy = cv2.GaussianBlur(Iyy, (3, 3), sigmaX=1)
        Iyy_list.append(Iyy)
    return np.stack(Iyy_list, axis=0)
