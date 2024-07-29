# Define a list of numbers.
# Substitute a subset of the list with new elements.
# Replace every 3rd element with a new value.
# Replace and resize a subset of the list.
# Delete every other element starting from the second element.

num_num = [1,2,3,4,5,6,7,8,9,10]
num_num[0:3] = [11,12,13,14]
print(num_num)

num_num[::3] = [100,101,102,103]
print(num_num)

num_num[4:7] = [50,51,52]
print(num_num)

num_num = [1,2,3,4,5,6,7,8,9,10]
del num_num[2::2]
print(num_num)