# Write a function that calculates the hypotenuse of a right triangle given the lengths of the other two sides using the math module.

import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

print(calculate_hypotenuse(56, 89)) 
