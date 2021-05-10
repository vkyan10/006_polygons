import math
from display import *


#vector functions
#normalize vector, should modify the parameter
def normalize(vector):
    return [0,0,1]

#Return the dot porduct of a . b
def dot_product(a, b):
    return (a[0]*b[0] + a[1]*b[1] + a[2]*b[2])

#Calculate the surface normal for the triangle whose first
#point is located at index i in polygons
def calculate_normal(polygons, i):
    a = []
    b = []
    for j in range(3):
        a.append(polygons[i+1][j] - polygons[i][j])    # p1-p0
        b.append(polygons[i+2][j] - polygons[i][j])    # p2-p0
    return [a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0]]