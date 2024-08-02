def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print() 
n = 10
print(f"The first {n} numbers in the Fibonacci sequence are:")
fibonacci(n)