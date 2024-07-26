# 11:
def hypo(len1,len2):
    import math
    total = math.pow(len1,2) + math.pow(len2,2)
    return math.sqrt(total)
print(hypo(3,4))

# This program works by using the math module. It takes the two lengths of the legs of the triangle, squares them, adds them, 
# then square roots the total. It then returns this value.