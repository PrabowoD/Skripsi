import numpy as np
import cv2

# 1. Sobel Kernel
def Compute_Gradient_X(images):
    Kx = np.array([[-1, 0, 1],
                   [-2, 0, 2],
                   [-1, 0, 1]])
    gradient_images = []
    for img in images:
        Ix = cv2.filter2D(img, -1, Kx)
        gradient_images.append(Ix)
    return gradient_images

def Compute_Gradient_Y(images):
    Ky = np.array([[1, 2, 1],
                   [0, 0, 0],
                   [-1, -2, -1]])
    gradient_images = []
    for img in images:
        Iy = cv2.filter2D(img, -1, Ky)
        gradient_images.append(Iy)
    return gradient_images