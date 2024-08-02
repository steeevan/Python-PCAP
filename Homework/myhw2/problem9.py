def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
test_numbers = [5, 7, 10]
for number in test_numbers:
    print(f"The factorial of {number} is: {factorial(number)}")