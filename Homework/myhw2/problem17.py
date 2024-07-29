# Create a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate over the list using a while loop
i = 0
while i < len(numbers):
    print(f"While loop iteration {i}: {numbers[i]}")
    i += 1

# Iterate over the list using a for loop with the range function
for i in range(len(numbers)):
    print(f"For loop with range iteration {i}: {numbers[i]}")

# Iterate over the list using a for loop with the in operator
for num in numbers:
    print(f"For loop with in operator: {num}")

# Iterate over the list using a for loop with the in operator and the enumerate function
for i, num in enumerate(numbers):
    print(f"For loop with enumerate iteration {i}: {num}")