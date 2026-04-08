import numpy as np
import cv2
import os

def AutoCorrelation(Ix_list, Iy_list):
    Ixx_list = []
    Ixy_list = []
    Iyy_list = []
    
    for Ix, Iy in zip(Ix_list, Iy_list):
        Ixx = Ix ** 2
        Ixy = Ix * Iy
        Iyy = Iy ** 2
        
        Ixx = cv2.GaussianBlur(Ixx, (3, 3), sigmaX=1)
        Ixy = cv2.GaussianBlur(Ixy, (3, 3), sigmaX=1)
        Iyy = cv2.GaussianBlur(Iyy, (3, 3), sigmaX=1)
        
        Ixx_list.append(Ixx)
        Ixy_list.append(Ixy)
        Iyy_list.append(Iyy)
    
    return np.stack(Ixx_list, axis=0), np.stack(Ixy_list, axis=0), np.stack(Iyy_list, axis=0)

def Compute_Gradient_X(images):
    Kx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]], np.float32)
    gradient_images = []
    for img in images:
        Ix = cv2.filter2D(img.astype(np.float32), cv2.CV_32F, Kx)
        gradient_images.append(Ix)
    return np.stack(gradient_images, axis=0)

def Compute_Gradient_Y(images):
    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]], np.float32)
    gradient_images = []
    for img in images:
        Iy = cv2.filter2D(img.astype(np.float32), cv2.CV_32F, Ky)
        gradient_images.append(Iy)
    return np.stack(gradient_images, axis=0)

def thresholding(preprocessed_images, Harris_respon, output_dir="Output"):
    os.makedirs(output_dir, exist_ok=True)
    all_corners = []

    for idx, (img, r) in enumerate(zip(preprocessed_images, Harris_respon)):
        # Normalisasi R untuk visualisasi
        R_norm = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
        R_norm = np.uint8(R_norm)

        # Threshold dan Non-Maximum Suppression
        thresh = 0.01 * r.max()
        dilated = cv2.dilate(r, None)
        nms_mask = (r == dilated) & (r > thresh)
        corners = np.argwhere(nms_mask)
        all_corners.append(corners)
    return all_corners

def Harris(Ixx_list, Ixy_list, Iyy_list, k=0.04):
    R_list = []
    for Ixx, Ixy, Iyy in zip(Ixx_list, Ixy_list, Iyy_list):
        Det_M = Ixx * Iyy - Ixy**2
        Trace_M = Ixx + Iyy
        R = Det_M - k * (Trace_M ** 2)
        R_list.append(R)
    return R_list
