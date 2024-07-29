# Define a list of numbers.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Substitute a subset of the list with new elements.
numbers[1:6] = [1,2,3,4,5]

# Replace every 3rd element with a new value.
numbers[::3] = [10,20,30,40,50,60,70]

# Replace and resize a subset of the list.
numbers[1:9] = [1,2,3,4,5]

# Delete every other element starting from the second element.
del numbers[1::2]
