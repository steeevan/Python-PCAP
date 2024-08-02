import random
def generate_random_numbers(n, start, end):
    random_numbers = [random.randint(start, end) for _ in range(n)]
    return random_numbers
n = 10
start = 1
end = 100

print(f"List of {n} random numbers between {start} and {end}:")
print(generate_random_numbers(n, start, end))