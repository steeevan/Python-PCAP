# 9:
def factorial(num):
    counter = 1
    for i in range(1,num+1):
        counter *= i
    return counter
print(factorial(10))
# This program works by using a for loop to iterate from 1 to the number and multiplies a counter variable by the iteration. It then
# returns the counter variable.