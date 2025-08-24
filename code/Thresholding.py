import numpy as np

def thresholding(R_list):
    corner_list = []
    threshold = 0.01 * np.max(R_list[0])
    for R in R_list:
        if R > threshold:
            corner_list.append(R)
    return corner_list