#2d list
two_d_array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Updating an element
two_d_array[1][1] = 50
print("After updating an element:")
for row in two_d_array:
    print(row)

# Inserting a new row
new_row = [10, 11, 12]
two_d_array.insert(1, new_row)
print("After inserting a new row:")
for row in two_d_array:
    print(row)

# Appending a new row
another_new_row = [13, 14, 15]
two_d_array.append(another_new_row)
print("After appending a new row:")
for row in two_d_array:
    print(row)

# Deleting a row
del two_d_array[2]
print("After deleting a row:")
for row in two_d_array:
    print(row)

# Creating a 3D array
three_d_array = [
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ],
    [
        [13, 14, 15],
        [16, 17, 18]
    ]
]

print("3D array elements:")
for matrix in three_d_array:
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()
    print()