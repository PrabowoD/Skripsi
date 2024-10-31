from scipy import ndimage

# Fungsi untuk menerapkan konvolusi 2D
def apply_kernel(image, kernel):
    
    # Lakukan konvolusi menggunakan scipy.ndimage.convolve
    return ndimage.convolve(image, kernel, mode="constant")

