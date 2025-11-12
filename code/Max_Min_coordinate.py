import math
import numpy as np

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def get_min_max_points_direct(corners):
    min_x_point = corners[np.argmin(corners[:, 1])]
    max_x_point = corners[np.argmax(corners[:, 1])]
    min_y_point = corners[np.argmin(corners[:, 0])]
    max_y_point = corners[np.argmax(corners[:, 0])]
    
    points = {
        "min_x": (int(min_x_point[1]), int(min_x_point[0])),
        "max_x": (int(max_x_point[1]), int(max_x_point[0])),
        "min_y": (int(min_y_point[1]), int(min_y_point[0])),
        "max_y": (int(max_y_point[1]), int(max_y_point[0]))
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


def select_near_center_points(corners, center):
    cx, cy = center
    result = {}

    # Konversi ke format (x, y) agar mudah dibaca
    pts = [(int(x), int(y)) for y, x in corners]

    # ----- cari min_x -----
    min_x_val = min(p[0] for p in pts)
    min_x_candidates = [p for p in pts if p[0] == min_x_val]
    min_x = min(min_x_candidates, key=lambda p: abs(p[1] - cy))

    # ----- cari max_x -----
    max_x_val = max(p[0] for p in pts)
    max_x_candidates = [p for p in pts if p[0] == max_x_val]
    max_x = min(max_x_candidates, key=lambda p: abs(p[1] - cy))

    # ----- cari min_y -----
    min_y_val = min(p[1] for p in pts)
    min_y_candidates = [p for p in pts if p[1] == min_y_val]
    min_y = min(min_y_candidates, key=lambda p: abs(p[0] - cx))

    # ----- cari max_y -----
    max_y_val = max(p[1] for p in pts)
    max_y_candidates = [p for p in pts if p[1] == max_y_val]
    max_y = min(max_y_candidates, key=lambda p: abs(p[0] - cx))

    result["min_x"] = min_x
    result["max_x"] = max_x
    result["min_y"] = min_y
    result["max_y"] = max_y

    return result