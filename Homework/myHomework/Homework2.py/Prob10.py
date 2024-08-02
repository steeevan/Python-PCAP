# Create a two-dimensional array and access its elements using nested loops.
d = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
for row in d:
    for elem in row:
        print(elem, end=' ')
    print()

# Create a two-dimensional array with list comprehension.
'''
num = 3
numb = 3
d[[0 for i in range(num) for j in range(numb)]]
for row in d:
    for elem in row:
        print(elem, end=' ')
    print()
    '''

# Update, insert, append, and delete elements in a two-dimensional array.
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m.append([4, 6, 3])
m.pop(2)
print(m)

# Create and manipulate a three-dimensional array.

g = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]]]

print(g[2][0][1])

