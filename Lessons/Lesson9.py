'''
10 Tuple in python
- define and create tuples
- understand the immutability of tuples 
- access tuple element using indexing and slicing
- utilie common tuple methods and operations
- iterate over tuple

 Definitions:
 A tuple is a collection of objects which is ordered and immutable. Tuples are silimar to lists
 but unlike lists, they can't be changed after they are created. Tuples are definced by enclising the elements in parentheses '()'
'''
'''
10.1 defining a tuple
 create an empty tuple
'''
empty_tuple=()
print(empty_tuple)
#ex 10.1.2
# create a tuple with one element, a trailing comma required
one_elem='elem1',
print(one_elem)
two_elem=10,15,
print(two_elem)
#example 10.1.3
#Incorrect single element tuple(without comma)
print(type(one_elem))# should be a tuple
error_tuple=('a')
print(type(error_tuple))
#ex 10.1.4
#create a tuple with multiple elements
my_tuple=(1,2,3,4,5)
print(my_tuple)

#ex 10.1.5
# initializing a tuple from a list
my_list=['a','b','c']
my_tup_from_list=tuple(my_list)
print(my_list)
print(my_tup_from_list)
'''
10.2 Heterogeneity
    tuples can contain hetergenous data type 
'''
#ex 10.2
ind_tuple=("Barack Obama","Joe Biden","Donald Trump",50,True,1.1)
print(ind_tuple)
'''
10.3 Index and negative Indexing 
Access elements in a tuple by their index numbers
'''
my_tuple=("Barack","Obama","04/08/1961",59,"Male",1.85,"American")
print(my_tuple[0]) # 1st element
print(my_tuple[3])  # 4th element
print(my_tuple[-1]) # last element
print(my_tuple[-2]) # Second to last element
'''
10.4 slice notation
slice notation to access arange of elements using syntax tuple[start:end]
start is inclusive and end is exclusive
'''
# ex 10.4
print(my_tuple[:]) # all elements
print(my_tuple[2:]) # from the third element to the end 
print(my_tuple[:4])
print(my_tuple[2:5])
print(my_tuple[1::2])
'''
10.5 tuple length
user the len() function to finde the number of elements in a tuple

'''
#ex 10.5
print(len(my_tuple))
'''
10.6 tuple membership
u can use the 'in' keyword tro tesgt if the element is in tuple
'''
#ex 10.6
if 'Obama'  in my_tuple:
    print(f"This tuple corresponds to information about Barack Obama")
else:
    print(f"This tuple does not correspond to information about Barack Obama")
'''
10.7 deleting tuples
u can delete tuple using the 'del' keyword
'''
print(my_tuple)
del my_tuple
try:
    print(my_tuple)
except NameError as e:
    print(e)
'''
10.8 joining tuples
you can join two tuples using the '+' operator this is known concatenation
'''
my_first_tuple=('a',1,'b',2,'c',3)
my_second_tuple=('d',4,'e',5,'f',6)
my_third_tuple=my_first_tuple+my_second_tuple
print(my_third_tuple)
'''
10.9 tuple assignment
tuples can pack and unpack multiple values into a single tuple and unpack the into individual varibles
'''
barack_Obama="Barack","Obama",59
print(barack_Obama)
print(type(barack_Obama))
barack_Obama_first_name, barack_Obama_last_name, barack_Obama_age= barack_Obama
print(barack_Obama_first_name)
print(barack_Obama_age)
a=10
b=99
print(a)
print(b)
(a,b)=(b,a)
print(a)
print(b)
'''
10.10 tuple methods
two methods' count()' and 'Index()'
'''
my_tuple =(0,1,0,1,1,0,0,1,1,1)
#tuple.count(x) returns the number of occurreneces of x in the tuple
print(my_tuple.count(0))
print(my_tuple.count(1))
print(my_tuple.count(2))
# tuple.index(x) returns the index of the first occurrenece of x in the tuple
print(my_tuple.index(0))
print(my_tuple.index(1))
try:
    print(my_tuple. index(2))
except ValueError as e:
    print(e)
'''
10.11 Iterating tuple
    Iterate over a tuple using various loop constructs
'''
'''
10.12 Tuples as return value
function can return multiple values as tuple
'''
#ex 10.12
import math 

'''
10.13 tuple is lists
lists can contain tuples a elements
'''

'''
10.14 lists in tuples 
tuples can contain lists as elements
'''
'''
10.15
multi-dimensional tuples
tuples can be nested to create multi-dimensional data structures
'''
identity_matrix=((1,0,0),(0,1,0),(0,0,1))
for row in identity_matrix:
    for elem in row:
        print(elem, end='')
    print()
'''
11 dictionaries in python
'''
'''
11.1
dictioanaries in python are collecftion of ley-value pairs. They are difined using 
curly brace'{}' or the 'dict()' function
'''
'''
11.2 Accessing dictionary items dictionary Items
can be accessed by referring to their key name, using either'[]' or get ( method)
'''
'''
11.3 Modifying dictionart itams
dictionart itmes can be modifying by assigning a new value to n existing key
'''
#ex 11.3
# modify and existing item
gdp_ranking_dict={
    "china":2,
    "India":8,
    "Japan":3,
    "United Kingdom": 5,
    "United states": 1
}
print(gdp_ranking_dict)
# update india's ranking
gdp_ranking_dict["India"]=7
print(gdp_ranking_dict)
'''
11.4 adding dictionary Items
New items can be added to a dictionary by assigning a value to new key 
'''
#ex 11.4
# add a new key-value pair
country_population_dict["South Korea"]=52
print(country_population_dict)
'''
11.5 removing dictionary items
items can be removed from a dictionary using the 'del' keyword abd 'pop()' method or the 
'popitne()' method
'''
#ex 11.5.1
'''
11.6 iterating dictionaries
dictyionaries can be iterated using loops to access key, values, or key-value pairs

'''
'''
11.7 Checking key existence 
check key exisitance by using the 'in' keyword in python
'''
'''
11.8 dictionary comprehension
dictionary comprehhension allows you to create dictionaries in a concise way using a single line of code
'''
'''
11.9 filtering data
filter data in dictionaries to include certain key-value pairs based on a condition
'''
#ex
'''
11.10 copying Dictionaries
dictionaries can be copies using a shallow copy and deep copy methods
'''
'''
11.11 Nested dictionaries
dictionaries can contain other dictionaries, creating nested structures
'''


'''
11.12 dictionaries from tuple
convert a list of tuples into dictionary
'''