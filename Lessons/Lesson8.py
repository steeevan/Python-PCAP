'''
9 Advanced lists in Python
- Access and manipulating list elements using indexing and slicing
- Understand and apply advanced list slicing techniques
- Differeniate between shallow and deep copies of list
- Multi-dimensional arrays
'''


'''
9.1 Index and Negative indexing
- Lists in ptyhon can be accessed using index numbers. Negative indexing allows access to elements from the end 
    of the list
'''
# Example 9.1
# Create a list containing the first 10 squares
squares = [1,4,9,16,25,36,49,64,81,100]

'''
9.2 AdvancedList Slicing
- List slicing allows you to use syntax 'list[start:end]'
'''
# Example 9.2
# Extract elements from a list that have been indexes using the stride size argument
print(squares[::2])
# Example 9.2.2
# use negative indexing stride size argument
print(squares[::-2])
# Example 9.2.3
# Extract elements at a defined set or known as the subset
print(squares[4:8:2])

# Example 9.2.4
# Extract elements with even indexes from the 5th element
print(squares[4::2])

'''
9.3 Advanced List Assignment
- List can be modified by assigning values to the slice of the list
'''
# Example 9.3.1
my_numbers = [1,3,6,10,15,21,28,36,45,55]
print(f'My list of numbers (first 10 triangle numbers): {my_numbers}')

# Substituting a subset of the list with new elements
my_numbers[1:3] = [4,9]
print(f'My list of numbers (substitution): {my_numbers}')

# Example 9.3.2
# Replace every nth element with a new value where N = 3
my_numbers[::3] = [1,16,49,100]
print(f'My list of numbers (n-th replacements): {my_numbers}')

# Example 9.3.3
# Replcea and resize a subset of the list
my_numbers[4:] = [25,36,49,64]
print(f'My list of numbers (first 8 square numbers): {my_numbers}')

# Example 9.3.4
# delete every th number starting from the 2nd elemebt
del my_numbers[1::2]
print(f'My list of numbers (every other square number): {my_numbers}')

'''
9.4 Shallow and Deep List Copies
- Shallow copies duplicate the structure of a list but not the elements of the list
- Deep copies duplicate both the structure and list elements
'''
# Example 9.4.1 Create a shallow copy of the original list using slicing notation
my_phrases = [['a','b','c'],['d','e','f'],['g','h','i']]
print(f'Original list of phrases: {my_phrases}')

my_shallow_phrases = my_phrases[:2] + [['j','k','l']]
print(f'Shallow copy of my phrases: {my_phrases}')

# Example 9.4.2 Create a shallow copy using the list() function
my_other_shallow_phrases = list(my_phrases) + [['j','k','l']]
print(f'Another shallow copy of my phrases: {my_other_shallow_phrases}')

# Example 9.4.3 Make a change to the original list of phrases
my_phrases[0][0]
my_phrases[0][1]
my_phrases[0][2]
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Shallow copy of my phrases: {my_shallow_phrases}')
print(f'Another shallow copt of my phrases: {my_other_shallow_phrases}')

# Example 9.4.4
import copy

my_phrases = [['a','b','c'],['d','e','f'],['g','h','i']]
my_deep_phrases = copy.deepcopy(my_phrases)
print(f'Original list of phrases: {my_phrases}')
print(f'Deep copy of my phrases: {my_deep_phrases}')

my_phrases[0][0] = 'ALPHA'
my_phrases[0][1] = 'BETA'
my_phrases[0][2] = 'GAMMA'
print(f'\nUpdated original list of phrases: {my_phrases}')

print(f'Deep copy of my phrases: {my_deep_phrases}')

'''
9.5 Iterating List
- Lists can be iterated through using while loops, for loops and the enumerate function
'''
# Example 9.5.1
my_diatomic_list = [0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4]
i = 0
while i < len(my_diatomic_list):
    print(f'Diatomic Sequence - Element #{i+1}: {my_diatomic_list[i]}')
    i+=1

# Example 9.5.2 Iterate the list using a for loop
for x in range(len(my_diatomic_list)):
    print(f"Diatomic Sequence - Element #{x+1}: {my_diatomic_list}")

# Example 9.5.3 Iterate the list using a for loop with the 'in' operator
for elem in my_diatomic_list:
    print(elem)
# Example 9.5.4 Iterate teh list using the enumerate function
for idx, elem in enumerate(my_diatomic_list):
    print(f'Diatomic Sequence - Element #{idx + 1}: {elem}')


'''
9.6 List membership
- List membership can be tested using the 'in' and 'not in' operators.
'''
# 9.6.1 Test whether an element exists in a list
squares = [1,4,9,16,25]
x = 16
if x in squares:
    print(f'{x} exists in our list of square numbers')
else:
    print(f'{x} does not exists in our list of square numbers')

# Example 9.6.2 Test whether an element is not in the list
y = 169
if y not in squares:
    print(f'{y} does not exists in our list of square numbers')
else:
    print(f'{y} exists in our list of square numbers')