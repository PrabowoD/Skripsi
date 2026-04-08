import numpy as np
import cv2
import os

def thresholding(preprocessed_images, Harris_respon, output_dir="Output"):
    os.makedirs(output_dir, exist_ok=True)
    all_corners = []

    for idx, (img, r) in enumerate(zip(preprocessed_images, Harris_respon)):
        R_norm = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
        R_norm = np.uint8(R_norm)


        thresh = 0.01 * r.max()
        dilated = cv2.dilate(r, None)
        nms_mask = (r == dilated) & (r > thresh)
        corners = np.argwhere(nms_mask)
        all_corners.append(corners)
    return all_corners