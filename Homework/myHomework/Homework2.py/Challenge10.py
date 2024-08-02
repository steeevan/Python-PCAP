# Write a function that prints the first n numbers in the Fibonacci sequence.

def fib():
    a, b = 0, 1

    for _ in range(10):
        print(a)
        a, b = b, a + b

fib()

