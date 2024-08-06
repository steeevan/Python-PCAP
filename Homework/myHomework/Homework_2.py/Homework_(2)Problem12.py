# Write a function that calculates the area of a circle given its radius using the math module.

import math

def area(radius):
    area = math.pi * (radius ** 2)
    return area
print(area(10))