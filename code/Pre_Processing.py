import numpy as np
import cv2
import os
from scipy import ndimage

def Input_image(image_path):
    images = []
    for filename in os.listdir(image_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            full_path = os.path.join(image_path, filename)
            image = cv2.imread(full_path, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                images.append(image)
                
                save_filename = os.path.join("Output", filename)
                cv2.imwrite(save_filename, image)
    return images

def PCA_rotate(corners):
     if corners is not None and len(corners) > 0:
        # Harris corners → (y, x), ubah jadi (x, y)
        pts = corners[:, [1, 0]].astype(np.float32)

        # PCA
        mean, eigenvectors, eigenvalues = cv2.PCACompute2(pts, mean=None)
        vx, vy = eigenvectors[0]

        # Sudut tubuh ikan (dalam derajat)
        pca_angle = np.degrees(np.arctan2(vy, vx))

        # print(f"Sudut PCA: {pca_angle:.2f} derajat")
        return pca_angle
    
def PCa_rotate_image(image, angle):
        h, w = image.shape
        center_img = (w // 2, h // 2)

        rotation_matrix_pca = cv2.getRotationMatrix2D(center_img, angle, 1.0)
        rotated_img_pca = cv2.warpAffine(image, rotation_matrix_pca, (w, h), borderValue=(255, 255, 255))
        
        return rotated_img_pca

def GaussianSmooth(image):
    # Check if the image is colored or grayscale
    if len(image.shape) == 3:  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif len(image.shape) == 2: 
        pass
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (3, 3), sigmaX=1)
    # Normalize the image to the range [0, 255]
    blurred_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)

    return blurred_image