import numpy as np
import cv2 as cv2
from scipy import ndimage
import os



directory = ""

for filename in os.listdir(directory):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        image_path = os.path.join(directory, filename)
        image_name = filename
        
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        