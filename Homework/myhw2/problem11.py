import math
def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    return hypotenuse
side1 = 3
side2 = 4
print(f"The hypotenuse of {side1} and {side2} is:", calculate_hypotenuse(side1, side2))