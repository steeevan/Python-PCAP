'''
10 Tuples in Python
- Define and Create tuples
<<<<<<< HEAD
- understand the immutability of tuples
- Access tuple elements using indexing and slicing
- Utilie common tuple methods and operations
=======
- Understand the immutability of tuples
- Access tuple elements using indexing and slicing
- Utilize common tuple methods and operations
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
- Iterate over tuples


Definition:
<<<<<<< HEAD
A tuple is a collecition of objects which is ordered and immutable. Tuples are similar to lists, 
but unlike lists, they cannot be changed after they are created. Tuples are defined by enclising the
elements in parentheses '()'
=======
A tuple is a collection of objects which is ordered and immutable. Tuples are similar to lists,
but unlike lists, they cannot be changed after they are created. Tuples are defined by enclosing the
elements in parenthesis '()'
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''

'''
10.1 Defining a tuple

<<<<<<< HEAD
Create an empty tuple
=======
Create and empty tuple
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''
empty_tuple = ()
print(empty_tuple)

# Example 10.1.2
<<<<<<< HEAD
# Create a tuple with one element, a trailing comma required
one_elem = 'elem1',
print(one_elem)
two_elem = 10,
=======
# Create a tuple with one element, a trailing common required
one_elem = 'elem1',
print(one_elem)
two_elem = 10,15,
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
print(two_elem)

# Example 10.1.3
# Incorrect single element tuple (without comma)
print(type(one_elem)) # should be a tuple
error_tuple = ('a') 
<<<<<<< HEAD
print(type(error_tuple)) # will be a str

# Exampe 10.1.4
=======
print(type(error_tuple)) # will be a string because PEMDAS (capturing string first)

# Example 10.1.4
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
# Create a tuple with multiple elements
my_tuple = (1,2,3,4,5)
print(my_tuple)

# Example 10.1.5
<<<<<<< HEAD
# Initializing a tuple from a list
=======
# Intializing a tuple from a list
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
my_list = ['a','b','c']
my_tup_from_list = tuple(my_list)
print(my_list)
print(my_tup_from_list)

'''
10.2 Heterogeneity
<<<<<<< HEAD
 Tuples can contain hetergenous data type
=======
Tuples can contain heterogenous data type
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''
# Example 10.2
ind_tuple = ("Barack Obama", "Joe Biden", "Donald Trump", 50, True, 1.1)
print(ind_tuple)


'''
10.3 Index and Negative Indexing
Access elements in a tuple by their index numbers
'''
<<<<<<< HEAD
my_tuple = ("Barack", "Obama", "04/08/1961", 59, "Male", 1.85, "American")
print(my_tuple[0])   # First element
print(my_tuple[3])   # Fourth element
print(my_tuple[-1])  # Last element
print(my_tuple[-2])  # Second to last element
=======
my_tuple = ("Barack","Obama","04/08/1961",59,"Male",1.85,"American")
print(my_tuple[0])  # First element
print(my_tuple[3])  # Fourth element
print(my_tuple[-1]) # Last element
print(my_tuple[-2]) # Second to last element
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4


'''
10.4 Slice Notation
Slice notation to access a range of elements using syntax tuple[start:end]
start is inclusive and end is exclusive
'''
# Example 10.4
<<<<<<< HEAD
print(my_tuple[:])     # All elements
print(my_tuple[2:])    # From the third element to the end
print(my_tuple[:4])    # From the beginning to the fourth element
print(my_tuple[2:5])   # From the third to the fifth element
print(my_tuple[1::2])  # Every second element starting from the second element
=======
print(my_tuple[:])      # All elements
print(my_tuple[2:])     # From the third element to the end
print(my_tuple[:4])     # From the beginning to the fourth element
print(my_tuple[2:5])    # From the third to the fifth element
print(my_tuple[1::2])   # Every second element starting from the second element
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

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
<<<<<<< HEAD
You can delete tules using the 'del' keyword
=======
You can delete tuples using the 'del' keyword
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''
print(my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(e)

'''
10.8 Joining Tuples
<<<<<<< HEAD
You can join two tuples using the '+' operator this is known concatenation
'''
my_first_tuple = ('a', 1, 'b', 2, 'c', 3)
my_second_tuple = ('d', 4, 'e', 5, 'f', 6)
my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

'''10.9 Tuple Assignment
Tuples can pack and unpack multiple values into a single tuple and unpack them into individual variables
=======
You can join two tuples using the '+' operator this is known as concatenation
'''
my_first_tuple = ('a',1,'b',2,'c',3)
my_second_tuple = ('d',4,'e',5,'f',6)
my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

'''
10.9 Tuple Assignment
Tuples can pack and unpack multiple values into a single tuple and unpack them into individual variables 
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
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
<<<<<<< HEAD
(a, b) = (b, a)
=======
(a,b) = (b,a)
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
print(a)
print(b)

'''
10.10 Tuple Methods
<<<<<<< HEAD
two methods 'count()' and 'index()'
'''
my_tuple = (0, 1, 0, 1, 1, 0, 0, 1, 1, 1)

=======
Two methods 'count()' and 'index()'
'''
my_tuple = (0,1,0,1,1,0,0,1,1,1)
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
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
<<<<<<< HEAD
my_diatomic_tuple = (0, 1, 1, 2, 1, 3, 2, 3, 1, 4, 3, 5, 2, 5, 3, 4)
=======
my_diatomic_tuple = (0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4)
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

# Using a while loop
i = 0
while i < len(my_diatomic_tuple):
<<<<<<< HEAD
    print(f'Diatomic Sequence - Element #{i + 1}: {my_diatomic_tuple[i]}')
=======
    print(f"Diatomic Sequence - Element #{i+1}: {my_diatomic_tuple[i]}")
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
    i += 1

# Using a for loop with range()
for x in range(len(my_diatomic_tuple)):
<<<<<<< HEAD
    print(f'Diatomic Sequence - Element #{x + 1}: {my_diatomic_tuple[x]}')
=======
    print(f"Diatomic Sequence - Element #{x+1}: {my_diatomic_tuple}")
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

# Using a for loop with the in operator
for elem in my_diatomic_tuple:
    print(elem)

# Using a for loop with the in operator and enumerate()
for idx, elem in enumerate(my_diatomic_tuple):
<<<<<<< HEAD
    print(f'Diatomic Sequence - Element #{idx + 1}: {elem}')
=======
    print(f"Diatomic Sequence - Element #{idx+1}: {elem}")
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
10.12 Tuples as Return Value
Functions can return multiple values as tuples
'''
# Example 10.12
<<<<<<< HEAD
import math

def circle(radius):
    """Return the (circumference, area) of a circle given its radius."""
    circumference = 2 * math.pi * radius
    area = math.pi * radius * radius
    return (circumference, area)

my_radius = 10
my_circumference, my_area = circle(my_radius)
print(f'The circumference of a circle of radius {my_radius}cm is {my_circumference}cm')
print(f'The area of a circle of radius {my_radius}cm is {my_area}cm\u00b2')

'''
10.13 Tuples in Lists
LIsts can contain tuples as elements
'''
my_list_of_tuples = [(1, 'abc'), (2, 'def'), (3, 'ghi')]
print(my_list_of_tuples)
print(my_list_of_tuples[0])
print(my_list_of_tuples[0][0])
print(my_list_of_tuples[1])
print(my_list_of_tuples[1][1])
print(my_list_of_tuples[2])
print(my_list_of_tuples[2][0])
print(type(my_list_of_tuples))
=======

'''
10.13 Tuples in Lists
Lists can contain tuples as elements
'''
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
10.14 Lists in Tuples
Tuples can contain lists as elements
'''
<<<<<<< HEAD
my_tuple_of_lists = ([1, 2, 3], ['abc', 'def', 'ghi'])
print(my_tuple_of_lists)
print(my_tuple_of_lists[0])
print(my_tuple_of_lists[0][0])
print(my_tuple_of_lists[1])
print(my_tuple_of_lists[1][1])
print(type(my_tuple_of_lists))

'''
10.15
Multi-Dimensional Tuples
Tuples can be nested to create multi-dimensional data structures
'''
identity_matrix = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
for row in identity_matrix:
    for elem in row:
        print(elem, end=' ')
    print()

=======

'''
10.15 Multi-Dimensional Tuples
Tuples can be nested to create multi-dimensional data structures
'''
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11 Dictionaries in Python
'''

'''
11.1 
<<<<<<< HEAD
Dictionaies in Python are collections of key-value pairs. They are defined using 
curly braces '{}' or the 'dict()' function
'''
 
# Example 11.1
# Create an empty dictionary
my_empty_dict = {}
print(my_empty_dict)

# Create a dictionary mapping countries to their population size in millions
country_population_dict = {
    "China": 1394,
    "India": 1326,
    "Japan": 126,
    "United Kingdom": 66,
    "United States": 330
}
print(country_population_dict)

# Create a dictionary using the dict() function and a list of tuples
country_population_dict = dict([
    ("China", 1394), 
    ("India", 1326), 
    ("Japan", 126), 
    ("United Kingdom", 66), 
    ("United States", 330)
])
print(country_population_dict)
=======
Dictionaries in Python are collections of key-value paris. They are defined using
curly braces know as '{}' or the 'dict()' function
'''

# Example 11.1 
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.2 Accessing Dictionary Items
Dictionary Items can be accessed by referring to their key name, using either '[]' or get() method
'''
# Example 11.2
<<<<<<< HEAD
# Access a value using square brackets
japan_population = country_population_dict["Japan"]
print(f'The population of Japan is {japan_population}m')

# Access a value using the get() method
china_population = country_population_dict.get("China")
print(f'The population of China is {china_population}m')

# Handling non-existent keys
# Using square brackets will raise a KeyError
# brazil_population = country_population_dict["Brazil"]  # Uncommenting this line will raise a KeyError

# Using get() method returns None if the key does not exist
brazil_population = country_population_dict.get("Brazil")
print(f'The population of Brazil is {brazil_population}m')

'''
11.3 Modifying Dictionary Items
Dictionary Items can be modified by assinging a new value to an existing key
'''

# Example 11.3
# Modify an existing item
gdp_rankings_dict = {
    "China": 2,
    "India": 8,
    "Japan": 3,
    "United Kingdom": 5,
    "United States": 1
}
print(gdp_rankings_dict)

# Update India's ranking
gdp_rankings_dict["India"] = 7
print(gdp_rankings_dict)
=======

'''
11.3 Modifying Dictionary Items
Dictionary Items can be modified by assigning a key value to an existing key
'''

# Example 11.3
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.4 Adding Dictionary Items
New items can be added to a dictionary by assigning a value to a new key
'''
# Example 11.4
<<<<<<< HEAD
# Add a new key-value pair
country_population_dict["South Korea"] = 52
print(country_population_dict)
=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.5 Removing Dictionary Items
Items can be removed from a dictionary using the 'del' keyword and 'pop()' method or the
'popitem()' method
'''

# Example 11.5.1
<<<<<<< HEAD
# Remove an item using the del keyword
del country_population_dict["Japan"]
print(country_population_dict)

# Example 11.5.2
# Remove an item using pop()
country_population_dict.pop("United Kingdom")
print(country_population_dict)

# Example 11.5.3
# Remove the last inserted item using popitem()
country_population_dict.popitem()
print(country_population_dict)

# Example 11.5.4
# Delete the entire dictionary
del gdp_rankings_dict

'''
11.6 Iterating Dictionaries
Dictionaries can be iterated using loops to access keys, values, or key-value pairs
'''
# Iterate through keys
for key in country_population_dict:
    print(key)

# Iterate through values
for value in country_population_dict.values():
    print(value)

# Iterate through key-value pairs
for key, value in country_population_dict.items():
    print(f'The population of {key} is {value}m')

'''
11.7 Checking Key Existence
Check key exisitince by using the 'in' keyword in python
'''
# Check for key existence
if "South Korea" in country_population_dict:
    print(f'The population of South Korea is {country_population_dict["South Korea"]}m')
else:
    print('South Korea does not exist in our dictionary of populations.')
=======
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
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.8 Dictionary Comprehension
Dictionary Comprehension allows you to create dictionaries in a concise way using a single line of code
'''

# Example 11.8
# Create a dictionary of squares
<<<<<<< HEAD
squares_dict = {num: num*num for num in range(1, 11)}
print(squares_dict)

# Convert distances from km to AU
km_to_au = 149_600_000
earth_planets_distance_km_dict = {
    "Mercury": 91_691_000, 
    "Venus": 41_400_000, 
    "Mars": 78_340_000, 
    "Jupiter": 628_730_000, 
    "Saturn": 1_275_000_000, 
    "Uranus": 2_723_950_000, 
    "Neptune": 4_351_400_000
}
earth_planets_distance_au_dict = {planet: round((km / km_to_au), 2) for planet, km in earth_planets_distance_km_dict.items()}
print(earth_planets_distance_au_dict)
=======
squares_dict = {num: num*num for num in range(1,11)}
print(squares_dict)

# Convert distance from km to AU
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.9 Filtering Data
Filter data in dictionaries to include certain key-value pairs based on a condition
'''

# Example 11.9
<<<<<<< HEAD
# Filter inner planets
inner_planets = ["Mercury", "Venus", "Earth", "Mars"]
earth_inner_planets_distance_km_dict = {key: earth_planets_distance_km_dict[key] for key in inner_planets if key in earth_planets_distance_km_dict}
print(earth_inner_planets_distance_km_dict)
=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.10 Copying Dictionaries
Dictionaries can be copied using a shallow copy and deep copy methods
'''
# Example 11.10
<<<<<<< HEAD
import copy

# Shallow copy
shallow_copy_dict = earth_planets_distance_km_dict.copy()
shallow_copy_dict["Earth"] = 0
print(shallow_copy_dict)

# Deep copy
deep_copy_dict = copy.deepcopy(earth_planets_distance_km_dict)
deep_copy_dict["Earth"] = 0
print(deep_copy_dict)

=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

'''
11.11 Nested Dictionaries
Dictionaries can contain other dictionaries, creating nested structures
'''
# Example 11.11
<<<<<<< HEAD
import pprint

# Nested dictionary
nested_multiplication_table_2d_dict = {
    1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}, 
    2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10}, 
    3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}, 
    4: {1: 4, 2: 8, 3: 12, 4: 16, 5: 20}, 
    5: {1: 5, 2: 10, 3: 15, 4: 20, 5: 25}
}
pprint.pprint(nested_multiplication_table_2d_dict)

'''
11.12 Dictionaries from tuple
Conver a list of tuples into a dictionary
'''
# Example 11.12
# List of tuples
country_area_tuples = [("Russia", 17_098_242), ("Canada", 9_984_670), ("United States", 9_857_348), ("China", 9_596_961)]
print(country_area_tuples)

# Convert to dictionary
country_area_dict = {key: value for key, value in country_area_tuples}
print(country_area_dict)

=======

'''
11.12 Dictionaries from tuples
Convert a list of tuples into a dictionary
'''
# Example 11.12
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
