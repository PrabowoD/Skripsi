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
    return np.array(images)


def preprocess_image(image):
    # Check if the image is colored or grayscale
    if len(image.shape) == 3:  
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif len(image.shape) == 2: 
        pass
    
    # Apply Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (5, 5), sigmaX=1)
    # Normalize the image to the range [0, 255]
    blurred_image = cv2.normalize(blurred_image, None, 0, 255, cv2.NORM_MINMAX)

    return blurred_image