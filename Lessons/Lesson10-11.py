'''
10 Tuples  in Python
- Define and Create tuples
- Understand the immutability of tuples
- Access tuple elements using indexing and slicing
- Utilize common tuple methods and operations
- Iterate over tuples


Definition
- A tuple is a collction of objects which is ordered and immutable. Tuples are similar to lists,
but unlike lists, they cannont be changed after they are created. Tuples are defined by enclosing
the elements in parentheses '()'
'''


'''
10.1 Defining a Tuple
- Create an empty tuple
'''

empty_tuple = ()
print(empty_tuple)

# Example 10.1.2
# Create a tuple with one element, a trailing comma required
one_elem = 'elem1',
print(one_elem)
two_elem = 10, 15,
print(two_elem)

# Example 10.1.3
# Incorrect single element tuple (without comma)
print(type(one_elem)) # Should print as a tuple
error_tuple = ('a') 
print(type(error_tuple)) # Will be a read as a string. If you want it to be read as a tuple, put commas behind or no quotations

# Example 10.1.4
# Create a tuple with multiple elements
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Example 10.1.5
# Initializing a tuple from a list
my_list = ['a', 'b', 'c']
my_tup_from_list = tuple(my_list)
print(my_list)
print(my_tup_from_list)

'''
10.2 Heterogenity
Tuple can contain heterogenous data types
'''
# Example 10.2
ind_tuple = ("Barak Obama", "Joe Biden", "Donald Trump", 50, True, 1.1)
print(ind_tuple)


'''
10.3 Index and Negative Indexing
- Access elements in a tuple by their index numbers
'''
my_tuple = ("Barak", "Obama", "04/08/1061", 59, "Male", 1.85, "American")
print(my_tuple[0]) # First element
print(my_tuple[3]) # Fourth element
print(my_tuple[-1]) # Last element
print(my_tuple[-2]) # Second to last element


'''
10.4 Slice Notation
- Slice Notation to access a range of elements using syntax tuple[start:end]
start is inclusive and end is exclusive
'''
# Example 10.4
print(my_tuple[:])
print(my_tuple[2:])
print(my_tuple[:4])
print(my_tuple[2:5])
print(my_tuple[1::2])

'''
10.5 Tuple Length
Use the 'len()' function to find the number of elements in a tuple
'''
# Example 10.5
print(len(my_tuple))

'''
10.6 Tuple Membership
- You can use the 'in' keyword to test if the element is in a tuple
'''
# Example 10.6
if 'Obama' in my_tuple:
    print("OOGA BOOGA")
else:
    print("BOOGA OOGA")


'''
10.7 Deleting Tuples
- You can delete tuples using the 'del' keyword
'''
print(my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(e)

'''
10.8 Joining Tuples
- You can join two tuples using the '+' operator. This is known as concatenation
'''
my_first_tuple = ('a', 1, 'b', 2, 'c', 3)
my_second_tuple = ('d', 4, 'e', 5, 'f', 6)
my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

'''10.9 Tuple Assignment
- Tuples can pack and unpack multiple values into a single tuple and unpack them into individual variables
'''
barak_obama = "Barak", "Obama", 59
print(barak_obama)
print(type(barak_obama))

barak_obama_first_name, barak_obama_last_name, barak_obama_age = barak_obama
print(barak_obama_first_name)
print(barak_obama_last_name)
print(barak_obama_age)

# Example 10.9.2 
# Swap values of two variables using tuple unpacking
a = 10
b = 99
print(a)
print(b)
(a, b) = (b, a)
print(a)
print(b)

'''
10.10 Tuple Methods
- Two methods known as 'count()' and 'index()'
'''
my_tuple = (0, 1, 0, 1, 1, 0, 0, 1, 1, 1)

# tuple.count(x) returns the number of occurrences of x in the tuple
print(my_tuple.count(0))
print(my_tuple.count(2))
print(my_tuple.ocunt(1))

# tuple.index(x) returns the index of the dirst occurrences of x in the tuple
print(my_tuple.index(0))
print(my_tuple.index(1))
try:
    print(my_tuple.index(2))
except ValueError as e:
    print(e)

'''
10.11 Iterating Tuples
- Iterate of a tuple using various loop constructs
'''
# Example 10.11




















'''
10.12 Tuples as Return Value
- Functions can reutrn multiple vlaues as tuples
'''
# Example 10.12
import math












'''
10.13 Tuples in Lists
- Lists can contain tuples  as elements
'''










'''
10.14 Lists in Tuples
- Tuples can contain lists as elements
'''








'''
10.15
Multi-Dimensional Tuples
Tuples can be nested to create multi-dimensional data stctures
'''







'''
11 Dictionaries in Python
'''

'''
11.1
Dictionaries in Python are collections of key-values pairs. They are defined using
curly braces '{}' of the 'dict{}' function
'''


























'''
11.2 Accessin Dictionary Items
- Dictionary items can be accessed by referring to hteir key name  using either '[]' or to  'get()' method
'''

















'''
11.3 Modifying Dictionary Items
- Dictionary items can be modified by assigning to an existing key
'''

# Example 11.3
# Modify an existing item
gpd_rankings_dict = {
    "China": 2,
    "India": 8,
    "Japan": 3,
    "UK": 5,
    "US": 1
}
print(gpd_rankings_dict)

# Update India's ranking
gpd_rankings_dict["Inia"] = 7
print(gpd_rankings_dict)

'''
11.4 Adding Dictionary Items
- New items can be added to a dictionary by assigning a value to a new key
'''
# Example 11.4
# Add a new key-value pair
country_population_dict["South Korea"] = 52
print(country_population_dict)

'''
11.5 Removing Dictionary Items
- Items can be removed from a dictionary using the 'del' keyword and 'pop()' method or the
'popitem()' method
'''




















'''
11.6 Iteratind Dictionaries
- Dictionaries can be iterated using loops to access keys, values, or key-value pairs
'''












'''
11.7 Checking key Existence
- Check key existence by using the 'in' keyword in Python
'''






'''
11.8 Dictionary Comprehension
- Dictionary comprehension allows you to create dictionaries in a concise way using a single line of code.
'''




















'''
11.9 Filtering Data
- Filter data in dictionaries to inlcude certain key-value pairs based on a condition
'''







'''
11.10 Copying Dictionaries 
- Dictionaries can be copied using a shallow copy and deep copy method
'''














'''
11.11 Nested Dictionaries
- Dictionaries can contain other dictionaries, creatinf nested structures
'''













'''
11.12 Dictionaries from Tuples
- Convert a list of tuples into a dictionary
'''









