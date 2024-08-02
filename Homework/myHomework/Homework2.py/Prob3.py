# Define a list of numbers.
num = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Substitute a subset of the list with new elements.
num[1:3] = [8, 5]
print(num)

# Replace every 3rd element with a new value.
num[::3] = [13, 165, 491, 10033]
print(num)

# Replace and resize a subset of the list.
num[4:] = [22345, 23436, 42349, 62344]
print(num)

# Delete every other element starting from the second element.
del num[1::2]
print(num)