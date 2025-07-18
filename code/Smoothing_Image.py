import numpy as np

# Fungsi untuk membuat Gaussian kernel 2D
def gaussian_kernel(size, sigma=1):
        
    # Tentukan titik pusat kernel
    kernel_range = range(-size//2 + 1, size//2 + 1)
    x, y = np.meshgrid(kernel_range, kernel_range)
    
    # Hitung kernel Gaussian
    normalizer = 1 / (2.0 * np.pi * sigma**2)
    gaussian_kernel = normalizer * np.exp(-(x**2 + y**2) / (2 * sigma**2))

    # Normalisasi
    return gaussian_kernel

