import numpy as np
from scipy import ndimage
from Smoothing_Image import gaussian_kernel

def preprocess_image(image):
    # Convert to grayscale
    gray_image = np.mean(image, axis=2).astype(np.uint8)

    # Apply Gaussian blur
    blurred_image = gaussian_kernel(gray_image, sigma=1)

    # Binarize image
    binary_image = blurred_image > 128

    return binary_image