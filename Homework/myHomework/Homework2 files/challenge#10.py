# 10:
def fibo(n):
    x = 0
    y = 1
    temp = 0
    print(x)
    for i in range(n-1):
        print(x + y)
        temp = x
        x = x + y
        y = temp
fibo(9)
# This program works by using 2 integers, and a temp integer. It adds the 2 integers, assigns the value of one of the variables
# to temp, assigns the total to the variable, then assigns the other varable temp. It also prints the total of the two numbers.