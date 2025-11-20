import numpy as np
import cv2
import os

def thresholding(preprocessed_images, Harris_respon, output_dir="Output"):
    os.makedirs(output_dir, exist_ok=True)
    all_corners = []

    for idx, (img, r) in enumerate(zip(preprocessed_images, Harris_respon)):
        # Normalisasi R untuk visualisasi
        R_norm = cv2.normalize(r, None, 0, 255, cv2.NORM_MINMAX)
        R_norm = np.uint8(R_norm)

        # Threshold dan Non-Maximum Suppression
        thresh = 0.01 * r.max()
        dilated = cv2.dilate(r, None)
        nms_mask = (r == dilated) & (r > thresh)
        corners = np.argwhere(nms_mask)
        all_corners.append(corners)

        # (Opsional) visualisasi titik sudut
        # img_color = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # for y, x in corners:
        #     cv2.circle(img_color, (x, y), 3, (0, 0, 255), -1)
        # cv2.imwrite(os.path.join(output_dir, f"corners_{idx}.png"), img_color)

    return all_corners