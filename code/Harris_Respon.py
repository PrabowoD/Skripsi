import numpy as np

def Harris(Ixx_list, Ixy_list, Iyy_list, k=0.04):
    R_list = []
    for Ixx, Ixy, Iyy in zip(Ixx_list, Ixy_list, Iyy_list):
        Det_M = Ixx * Iyy - Ixy**2
        Trace_M = Ixx + Iyy
        R = Det_M - k * (Trace_M ** 2)
        R_list.append(R)
    return R_list
