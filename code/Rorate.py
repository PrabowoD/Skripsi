import os
import numpy as np
import cv2 as cv2

def PCA_rotate(corners):
     if corners is not None and len(corners) > 0:
        # Harris corners → (y, x), ubah jadi (x, y)
        pts = corners[:, [1, 0]].astype(np.float32)

        # PCA
        mean, eigenvectors, eigenvalues = cv2.PCACompute2(pts, mean=None)
        vx, vy = eigenvectors[0]

        # Sudut tubuh ikan (dalam derajat)
        pca_angle = np.degrees(np.arctan2(vy, vx))

        print(f"Sudut PCA: {pca_angle:.2f} derajat")
        return pca_angle
    
def PCa_rotate_image(image, angle):
        h, w = image.shape
        center_img = (w // 2, h // 2)

        rotation_matrix_pca = cv2.getRotationMatrix2D(center_img, angle, 1.0)
        rotated_img_pca = cv2.warpAffine(image, rotation_matrix_pca, (w, h), borderValue=(255, 255, 255))
        
        return rotated_img_pca

def Hough_rotate(image):
    gray = image.astype(np.uint8)
    edges = cv2.Canny(gray, 50, 150)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, 100)

    if lines is not None:
        rho, theta = lines[0][0]

        # Hough: theta relatif ke vertikal → ubah jadi horizontal
        hough_angle = np.degrees(theta) - 90

        print(f"Sudut Hough: {hough_angle:.2f} derajat")
        return hough_angle

def Hough_rotate_image(image, angle):
    h, w = image.shape
    center_img = (w // 2, h // 2)

    rotation_matrix_hough = cv2.getRotationMatrix2D(center_img, angle, 1.0)
    rotated_img_hough = cv2.warpAffine(image, rotation_matrix_hough, (w, h), borderValue=(255, 255, 255))
    
    return rotated_img_hough

def rotate_point(point, angle, center):
    angle_rad = np.radians(angle)
    x, y = point
    cx, cy = center

    # Translasi titik ke origin
    x_translated = x - cx
    y_translated = y - cy
    # Rotasi titik
    x_rotated = x_translated * np.cos(angle_rad) - y_translated * np.sin(angle_rad)
    y_rotated = x_translated * np.sin(angle_rad) + y_translated * np.cos(angle_rad)
    # Translasi kembali ke posisi semula    
    x_final = x_rotated + cx
    y_final = y_rotated + cy
    return (int(x_final), int(y_final))