import math
def calculate_area_of_circle(radius):
    area = math.pi * math.pow(radius, 2)
    return area
radius = 5
print(f"The area of a circle with radius {radius} is:", calculate_area_of_circle(radius))