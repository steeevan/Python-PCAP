'''
10 Tuples in Python
- Define and Create tuples
- Understand the immutability of tuples
- Access tuple elements using indexing and slicing
- Utilize common tuple methods and operations
- Iterate over tuples


Definition:
A tuple is a collection of objects which is ordered and immutable. Tuples are similar to lists,
but unlike lists, they cannot be changed after they are created. Tuples are defined by enclosing the
elements in parenthesis '()'

'''

'''
10.1 Defining a tuple

Create and empty tuple
'''
empty_tuple = ()
print(empty_tuple)

# Example 10.1.2
# Create a tuple with one element, a trailing common required
one_elem = 'elem1',
print(one_elem)
two_elem = 10,15,
print(two_elem)

# Example 10.1.3
# Incorrect single element tuple (without comma)
print(type(one_elem)) # should be a tuple
error_tuple = ('a') 
print(type(error_tuple)) # will be a string because PEMDAS (capturing string first)

# Example 10.1.4
# Create a tuple with multiple elements
my_tuple = (1,2,3,4,5)
print(my_tuple)

# Example 10.1.5
# Intializing a tuple from a list
my_list = ['a','b','c']
my_tup_from_list = tuple(my_list)
print(my_list)
print(my_tup_from_list)

'''
10.2 Heterogeneity
Tuples can contain heterogenous data type
'''
# Example 10.2
ind_tuple = ("Barack Obama", "Joe Biden", "Donald Trump", 50, True, 1.1)
print(ind_tuple)


'''
10.3 Index and Negative Indexing
Access elements in a tuple by their index numbers
'''
my_tuple = ("Barack","Obama","04/08/1961",59,"Male",1.85,"American")
print(my_tuple[0])  # First element
print(my_tuple[3])  # Fourth element
print(my_tuple[-1]) # Last element
print(my_tuple[-2]) # Second to last element


'''
10.4 Slice Notation
Slice notation to access a range of elements using syntax tuple[start:end]
start is inclusive and end is exclusive
'''
# Example 10.4
print(my_tuple[:])      # All elements
print(my_tuple[2:])     # From the third element to the end
print(my_tuple[:4])     # From the beginning to the fourth element
print(my_tuple[2:5])    # From the third to the fifth element
print(my_tuple[1::2])   # Every second element starting from the second element

'''
10.5 Tuple Length
Use the 'len()' function to find the number of elements in a tuple
'''
# Example 10.5
print(len(my_tuple))

'''
10.6 Tuple Membership
You can use the 'in' keyword to test if the element is in tuple
'''
# Example 10.6
if 'Obama' in my_tuple:
    print(f"This tuple corresponds to information about Barack Obama")
else:
    print(f"This tuple does not correspond to information about Barack Obama")


'''
10.7 Deleting Tuples
You can delete tuples using the 'del' keyword
'''
print(my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(e)

'''
10.8 Joining Tuples
You can join two tuples using the '+' operator this is known as concatenation
'''
my_first_tuple = ('a',1,'b',2,'c',3)
my_second_tuple = ('d',4,'e',5,'f',6)
my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

'''
10.9 Tuple Assignment
Tuples can pack and unpack multiple values into a single tuple and unpack them into individual variables 
'''
barack_obama = "Barack", "Obama", 59
print(barack_obama)
print(type(barack_obama))

barack_obama_first_name, barack_obama_last_name, barack_obama_age = barack_obama
print(barack_obama_first_name)
print(barack_obama_last_name)
print(barack_obama_age)

# Example 10.9.2
# Swap values of two variables using tuple unpacking
a = 10
b = 99
print(a)
print(b)
(a,b) = (b,a)
print(a)
print(b)

'''
10.10 Tuple Methods
Two methods 'count()' and 'index()'
'''
my_tuple = (0,1,0,1,1,0,0,1,1,1)
# tuple.count(x) returns the number of occurrences of x in the tuple
print(my_tuple.count(0))
print(my_tuple.count(1))
print(my_tuple.count(2))

# tuple.index(x) returns the index of the first occurrence of x in the tuple
print(my_tuple.index(0))
print(my_tuple.index(1))
try:
    print(my_tuple.index(2))
except ValueError as e:
    print(e)

'''
10.11 Iterating Tuples
Iterate over a tuple using various loop constructs
'''
# Example 10.11
my_diatomic_tuple = (0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4)

# Using a while loop
i = 0
while i < len(my_diatomic_tuple):
    print(f"Diatomic Sequence - Element #{i+1}: {my_diatomic_tuple[i]}")
    i += 1

# Using a for loop with range()
for x in range(len(my_diatomic_tuple)):
    print(f"Diatomic Sequence - Element #{x+1}: {my_diatomic_tuple}")

# Using a for loop with the in operator
for elem in my_diatomic_tuple:
    print(elem)

# Using a for loop with the in operator and enumerate()
for idx, elem in enumerate(my_diatomic_tuple):
    print(f"Diatomic Sequence - Element #{idx+1}: {elem}")

'''
10.12 Tuples as Return Value
Functions can return multiple values as tuples
'''
# Example 10.12

'''
10.13 Tuples in Lists
Lists can contain tuples as elements
'''

'''
10.14 Lists in Tuples
Tuples can contain lists as elements
'''

'''
10.15 Multi-Dimensional Tuples
Tuples can be nested to create multi-dimensional data structures
'''

'''
11 Dictionaries in Python
'''

'''
11.1 
Dictionaries in Python are collections of key-value paris. They are defined using
curly braces know as '{}' or the 'dict()' function
'''

# Example 11.1 

'''
11.2 Accessing Dictionary Items
Dictionary Items can be accessed by referring to their key name, using either '[]' or get() method
'''
# Example 11.2

'''
11.3 Modifying Dictionary Items
Dictionary Items can be modified by assigning a key value to an existing key
'''

# Example 11.3

'''
11.4 Adding Dictionary Items
New items can be added to a dictionary by assigning a value to a new key
'''
# Example 11.4

'''
11.5 Removing Dictionary Items
Items can be removed from a dictionary using the 'del' keyword and 'pop()' method or the
'popitem()' method
'''

# Example 11.5.1
# Remove and item using the del keyword

# Example 11.5.2
# Remove an item using pop()

# Example 11.5.3
# Remove the last inserted item using popitem()

# Example 11.5.4
# Delete the entire dictionary

'''
11.6 Iterating Dictionaries 
Dictionaries can be iterated using loops to access keys, values, or key-value pairs
'''
# Example 11.6

'''
11.7 Checking Key Existence
Check key existence by using the 'in' keyword in Python
'''
# Example 11.7

'''
11.8 Dictionary Comprehension
Dictionary Comprehension allows you to create dictionaries in a concise way using a single line of code
'''

# Example 11.8
# Create a dictionary of squares
squares_dict = {num: num*num for num in range(1,11)}
print(squares_dict)

# Convert distance from km to AU

'''
11.9 Filtering Data
Filter data in dictionaries to include certain key-value pairs based on a condition
'''

# Example 11.9

'''
11.10 Copying Dictionaries
Dictionaries can be copied using a shallow copy and deep copy methods
'''
# Example 11.10

'''
11.11 Nested Dictionaries
Dictionaries can contain other dictionaries, creating nested structures
'''
# Example 11.11

'''
11.12 Dictionaries from tuples
Convert a list of tuples into a dictionary
'''
# Example 11.12