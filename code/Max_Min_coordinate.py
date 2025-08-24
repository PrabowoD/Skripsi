import math
import numpy as np

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def max_y_coordinate(corners_list):
    max_y = -np.inf
    for corners in corners_list:
        for corner in corners:
            if corner[1] > max_y and corner[1] > 0:
                max_y = corner[1]
    return max_y



def check_Y(point1, point2):
    if point1[1] == point2[1]:
        return 0
    
    elif point1[1] > point2[1]:
        point2 = (point2[0], point1[1])
        return 0
    
    elif point1[1] < point2[1]:
        point1 = (point1[0], point2[1])
        return 0

    return 1

def check_X(point1, point2):
    if point1[0] == point2[0]:
        return 0
    
    elif point1[0] > point2[0]:
        point2 = (point1[0], point2[1])
        return 0
    
    elif point1[0] < point2[0]:
        point1 = (point2[0], point1[1])
        return 0
    
    return 1
