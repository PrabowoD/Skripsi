import numpy as np
from scipy.ndimage import gaussian_filter
from scipy.signal import convolve2d

def harris_corner_detection(I, measure='Harris', κ=0.04, σd=1, σi=1, τ=0.1, strategy='grid', cells=(3, 3), N=500, subpixel=False):
    def gaussian_kernel(size, sigma):
        kernel = np.fromfunction(lambda x, y: (1/(2*np.pi*sigma**2)) * np.exp(-((x - (size-1)/2)**2 + (y - (size-1)/2)**2)/(2*sigma**2)), (size, size))
        return kernel / np.sum(kernel)

    def gradient(I):
        kernel_x = np.array([[-1, 0, 1]])
        kernel_y = np.array([[-1], [0], [1]])
        Ix = convolve2d(I, kernel_x, mode='same')
        Iy = convolve2d(I, kernel_y, mode='same')
        return Ix, Iy

    def compute_autocorrelation_matrix(Ix, Iy, σ):
        size = int(2*np.ceil(3*σ)+1)
        G = gaussian_kernel(size, σ)
        A = convolve2d(Ix**2, G, mode='same')
        B = convolve2d(Ix*Iy, G, mode='same')
        C = convolve2d(Iy**2, G, mode='same')
        return A, B, C

    def compute_corner_response(A, B, C, measure, κ):
        if measure == 'Harris':
            R = (A * C - B**2) - κ * (A + C)**2
        elif measure == 'Shi-Tomasi':
            R = np.minimum(A, C) - κ * (A + C)
        else:
            raise ValueError("Unknown measure type. Choose 'Harris' or 'Shi-Tomasi'.")
        return R

    def non_maximum_suppression(R, τ, radius):
        max_filtered = np.zeros_like(R)
        for r in range(R.shape[0]):
            for c in range(R.shape[1]):
                patch = R[max(0, r-radius):min(R.shape[0], r+radius+1), max(0, c-radius):min(R.shape[1], c+radius+1)]
                if R[r, c] == np.max(patch) and R[r, c] > τ:
                    max_filtered[r, c] = R[r, c]
        return max_filtered

    def select_output_corners(corners, strategy, cells, N):
        if strategy == 'grid':
            step_x = I.shape[1] // (cells[0] + 1)
            step_y = I.shape[0] // (cells[1] + 1)
            selected_corners = []
            for i in range(1, cells[0] + 1):
                for j in range(1, cells[1] + 1):
                    cell_corners = corners[j*step_y-1:(j+1)*step_y-1, i*step_x-1:(i+1)*step_x-1]
                    cell_corners = [(x, y) for x, y in zip(*np.where(cell_corners > 0))]
                    cell_corners = sorted(cell_corners, key=lambda x: -corners[x[0], x[1]])
                    selected_corners += cell_corners[:min(N, len(cell_corners))]
            return selected_corners
        else:
            raise ValueError("Unknown strategy type. Choose 'grid'.")
