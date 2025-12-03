import math
import numpy as np


def get_min_max_points_direct(corners):
    min_x_point = corners[np.argmin(corners[:, 1])]
    max_x_point = corners[np.argmax(corners[:, 1])]
    min_y_point = corners[np.argmin(corners[:, 0])]
    max_y_point = corners[np.argmax(corners[:, 0])]
    
    points = {
        "min_x": (int(min_x_point[0]), int(min_x_point[1])),
        "max_x": (int(max_x_point[0]), int(max_x_point[1])),
        "min_y": (int(min_y_point[0]), int(min_y_point[1])),
        "max_y": (int(max_y_point[0]), int(max_y_point[1]))
    }

    return points

def get_center_from_bounds(points):
    min_x, max_x = points["min_x"][0], points["max_x"][0]
    min_y, max_y = points["min_y"][1], points["max_y"][1]
    center_x = (min_x + max_x) / 2
    center_y = (min_y + max_y) / 2
    return (int(center_x), int(center_y))

def get_center_from_corners(corners):
    if len(corners) == 0:
        return None 
    
    mean_x = int(np.mean(corners[:, 1]))
    mean_y = int(np.mean(corners[:, 0]))    
    return (mean_x, mean_y)

