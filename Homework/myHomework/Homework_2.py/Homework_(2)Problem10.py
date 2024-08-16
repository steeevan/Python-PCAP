# Write a function that prints the first n numbers in the Fibonacci sequence.

def i_dont_like_this_one(n):
    if n <= 0:
        print("Please enter a positive integer")
        return
    elif n == 1:
        print("0")
        return
    elif n == 2:
        print("0")
        print("1")
        return
    a, b = 0, 1
    print(a)
    print(b)
    for huh in range(2, n):
        a, b = b, a + b
        print(b)