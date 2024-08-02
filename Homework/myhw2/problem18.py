numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Substitute a subset of the list with new elements
numbers[3:6] = [20, 21, 22]

# Replace every 3rd element with a new value
numbers[2::3] = [99] * len(numbers[2::3])

# Replace and resize a subset of the list
numbers[4:8] = [30, 31]

# Delete every other element starting from the second element
del numbers[1::2]

print(numbers)
# Output: [1, 99, 30, 99]