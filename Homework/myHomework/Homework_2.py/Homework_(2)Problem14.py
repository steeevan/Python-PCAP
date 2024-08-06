# Write a function that generates a list of n random numbers between a given range using the random module.

import random

def list(n):
    list = []
    for i in range(n):
        list.append(random.randint(1,100))
    return list

print(list(10))