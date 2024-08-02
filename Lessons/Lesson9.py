'''
9 Advanced Lists in Python
- Access and manipulating list elements using indexinf and slicing
- Understand and apply advances list slicing techniques
- Differentiate between shallow and deep copies of lists
- Multi-Dimensional arrays
'''


'''
9.1 Index and Negative Indexing
- Lists in Python can be accessed by index numbers. Negative indexing allows access to elements from
    the end of the list
'''
# Example 9.1
# Create a list containing the first ten squares
squares =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
9.2 Advanced List Slicing
- List slicing allows you to use syntax 'list[start:end]'
'''
# Example 9.2.1
# Extract elements from a list that have been indexes using the stride size argument
print(squares[::2])  # ::2 is an example of stride step
# Example 9.2.2
# Use negative indexing stride sized arguments
print(squares[::-2])
# Example 9.2.3
# Extract elements at a defineed set or known as a subset
print(squares[4:8:2])

# Example 9.2.4
# Extract elements with even indexes from the 5th element
print(squares[4::2])

'''
9.3 Advances List Assignment
- List can be modified by assigning values to slices of the list
'''
# Example 9.3.1
my_numbers = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
print(f'My list of numbers (First 10 triandle numbers): {my_numbers}')

# Substituting a subset of the list with new elements
my_numbers[1:3] = [4, 9]
print(f'My list of numbers (Substitution): {my_numbers}')

# Example 9.3.2
# Replace every nth element with a new alue where N = 3
my_numbers[::3] = [1, 16, 49, 100]
print(f'My list of numbers (n-th replacements): {my_numbers}')

# Example 9.3.3
# Replace and resize a subset of the list
my_numbers[4:] = [25, 36, 49, 64]
print(f'My list of number (First 8 square numbers): {my_numbers}')

# Exmaple 9.3.4
# Delete every nth number starting from the 2nd element
del my_numbers[1::2]
print(f'My list of numbers (Every other square number): {my_numbers}')

'''
9.4 Shallow and Deep List Copies
- Shallow copies duplicate the structure of a list but not the elements of the list
- Deep copies duplicate both the stucture and list elements
'''
# Example 9.4.1 Create a shallow copy of the original list using slicing notation
my_phrases = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
print(f'Original list of phrases: {my_phrases}')

my_shallow_phrases = my_phrases[:2] + [['j', 'k', 'l']]
print(f'Shallow copy of my phrases: {my_shallow_phrases}')

# Example 9.4.2 Create a shallow copy using the list() function
my_other_shallow_phrases = list(my_phrases) + [['j', 'k', 'l']]
print(f'Another shallow copy of my phrases: {my_other_shallow_phrases}')

# Example 9.4.3 Make a change to the original list of phrases
my_phrases[0][0] = "ALPHA"
my_phrases[0][1] = "BETA"
my_phrases[0][2] = "GAMMA"
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Challow copy of my phrases: {my_shallow_phrases}')
print(f'Another challow copy of my phrase: {my_other_shallow_phrases}')

# Example 9.4.4 Create a deep copy of the original list
import copy

my_phrases = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
my_deep_phrases = copy.deepcopy(my_phrases)
print(f'Original list of phrases: {my_phrases}')
print(f'Deep copy of my phrases: {my_deep_phrases}')

my_phrases[0][0] = "ALPHA"
my_phrases[0][1] = "BETA"
my_phrases[0][2] = "GAMMA"
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Deep copy of my phrases: {my_deep_phrases}')

'''
9.5 Iterating List
- Lists can be iterated through using while loops, for loops, and the enumerate function
'''
# Example 9.5.1
my_diatomic_list = [0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4]
i = 0
while i < len(my_diatomic_list):
    print(f'Diatomic Sequence - Element #{i + 1}: {my_diatomic_list[i]}')
    i += 1

# Exmaple 9.5.2 Iterate the list using a for loop
for x in range(len(my_diatomic_list)):
    print(f'Diatomic Sequence - Element #{x + 1}: {my_diatomic_list[x]}')

# Example 9.5.3 Iterate the list using a for loop with the 'in' operator\
for elem in my_diatomic_list:
    print(elem)
# Exmaple 9.5.4 Iterate the list ising the enumerate function
for idx, elem, in enumerate(my_diatomic_list):
    print(f'Diatomic Sequence -Element #{idx + 1}: {elem}')


'''
9.6 List Membership
- List membership can be tested using the 'in' and 'not in' operators
'''
# Example 9.6.1 Test whether an element exists in a list
squares = [1, 4, 9, 16, 25]
x = 16
if x in squares:
    print(f"{x} exists in out list of square numbers")
else:
    print(f"{x} does not exist in out list of square numbers")

# Example 9.6.2 Teset whether an element in not in the list
y = 169
if y not in squares:
    print(f"{y} Does not exist in out list of square numbers")
else:
    print(f"{y} exists in our list of square numbers")

'''
9.7 List Comprehension
- List comprehension provides a concise way of creating lists
'''
# Example 9.7.1
squares = [num * num for num in range(1,9)]
print(squares)

# Example 9.7.2 Create a list formed of characters from a string
letters_in_abibliophobia = [character for character in 'abibliophobia']
print(letters_in_abibliophobia)

# Example 9.7.3
def isPrime(num):
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

prime_numbers = [i for i in range(1, 101) if isPrime(i)]
print(prime_numbers)

# Example 9.7.4
even_numbers_zeroed_odd = [1 if 1 % 2 == 0 else 0 for i in range(1, 101)]
print(even_numbers_zeroed_odd)

'''
9.8 Multi-Dimensional Arrays
- List that contains other lists
'''
# Example 9.8.1 Create a 2D array
my_2d_array = [[1, 2, 3,], [4, 5, 6], [7, 8, 9]]
for row in my_2d_array:
    for elem in row:
        print(elem, end=' ')
    print()
# Example 9.8 2 Create a 2D array with list comprehension
number_cols = 3
number_rows = 3
my_2d_array[[0 for i in range(number_cols) for j in range(number_rows)]]
for row in my_2d_array:
    for elem in row:
        print(elem, end=' ')
    print()
    
# Example 9.8.3 Access elements using square brackets and indices
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_2d_array[0][0])
print(my_2d_array[1][1])
print(my_2d_array[2][2])

# Example 9.8.4 Manipulate a 2D array
my_2d_array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

my_2d_array[1][1] = 0
my_2d_array.insert(2, [9, 9, 9])
my_2d_array.append([7, 4, 7])
my_2d_array[0].extend([0, 0])
my_2d_array[2].reverse()
del my_2d_array[3]

for row in my_2d_array:
    for elem in row:
        print(elem, end=' ')
    print()
