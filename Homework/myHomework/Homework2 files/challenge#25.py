# Create a two-dimensional array and access its elements using nested loops.
my_2d_array = [['a','b','c'],['d','e','f'],['g','h','i']]
for row in my_2d_array:
    for elem in row:
        print(elem, end = ' ')
    print()

# Create a two-dimensional array with list comprehension.
number_cols = 5
number_rows = 5
my_2d_array = [[0 for i in range(number_cols)] for j in range(number_rows)]

# Update, insert, append, and delete elements in a two-dimensional array.
my_2d_array = [['a','b','c'],['d','e','f'],['g','h','i']]
my_2d_array.append(1)
my_2d_array.insert(-1,[1,2,3])
del my_2d_array[-1]

# Create and manipulate a three-dimensional array.
my_3d_array = [[['a','b','c'],['d','e','f'],['g','h','i']],[['j','k','l'],['m','n','o'],['p','q','r']]]
my_3d_array.append(['s','t','u'])
my_3d_array.insert(-1,['v','w','x'])
del my_3d_array[-1]