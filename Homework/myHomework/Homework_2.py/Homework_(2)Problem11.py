# Write a function that calculates the hypotenuse of a right triangle given the lengths of the other two sides using the math module.

import math

def hypotenuse(a, b):
    erm = a**2 + b**2
    c = math.sqrt(erm)
    return c
print(hypotenuse(5,6))