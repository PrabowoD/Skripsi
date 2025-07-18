from scipy import ndimage
import cv2

# Fungsi untuk menerapkan konvolusi 2D
def apply_kernel(image, kernel):

    # Lakukan konvolusi menggunakan OpenCV
    return cv2.filter2D(image, -1, kernel)

