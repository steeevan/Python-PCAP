'''
Write a function that generates a list of n random numbers between a given range using the random module.
Hint: Use random.randint().
'''

import random

def r(low, high):
    return [random.randint(low, high) for _ in range(10)]

print(r(1, 100))
