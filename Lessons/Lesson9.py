'''
11 Dictionaries in Python
'''

'''
11.1
Dictionaries in Python are collections of key-value pairs. They are defined using
curly braces '{}' or the 'dict()' function
'''

# 11.1
# Create an empty dictionary
# copy from repo




'''
11.2 Accesssing Dictionary itemrs
Dictionary Items can be accessed by referring to their key name, using either '[]' or get() method
'''
# Example 11.2
# copy from repo



'''
11.3 Modifying Dictionary Items
Dictionary items can be modified by assigning a new value to an existing key
'''

# Example 11.3
# Modify an existing list
gdp_ranking_dict = {
    "China":2,
    "India":8,
    "Japan":3,
    "United Kingdom":5,
    "United States":1
}
print(gdp_ranking_dict)

# Update India's ranking
gdp_ranking_dict["India"] = 7
print(gdp_ranking_dict)

'''
11.4 Adding Dictionary Items
New items can be added to a dictionary by assigning a value to a new key
'''
# Example 11.4
# Add a new key-value pair
# copy later


'''
11.5 Removing Dictionary Items
Items can be removed from a dictionary using the 'del' keyword and 'pop()' method or the
'popitem()' method
'''

# Example 11.5.1
# Remove an item using the del keyword
# copy later

# Example 11.5.2
# Remove an item using pop()
# copy later cause don't have dictionary


# Example 11.5.3
# Remove the last inserted item by using popitem()
# copy later cause don't have dictionary



# Example 11.5.4
# Delete the entire dictionary
del gdp_ranking_dict

'''
11.6 Iterating Dictionaries
Dictionaries can be iterated using loops to access keys, values, or key-value pairs.
'''

# copy later cause don't have dictionary


'''
11.7 Checking Key Existence
CHeck key exisitince by using the 'in' keyword in python
'''
# Check for key existence
# copy later cause don't have dictionary

'''
11.8 Dictionary Comprehension
Dictionary Comprehension allows you to create dictionaries in a concise way using a single line of code
'''
# Create a dictionary of squares
squares_dict = {num: num*num for num in range(1,11)}
print(squares_dict)

# Convert distances from km to AU
km_to_au = 149_600_000
# later

'''
11.9 Filtering Data
Filter Data in dictionaries to include certain key-value pairs based on a condition
'''

# 11.9
# copy later cause don't have dictionary


'''
11.10 Copying Dictionaries
Dictionaries can be copied using a shallow copy and deep copy methods
'''
# Example 11.10
import copy

# copy later 


'''
11.11 Nested Dictionaries
Dictionaries can contain other dictionaries, created nested structures
'''
# Example 11.11
import pprint

# Nested Dictionary
# copy later

'''
11.12 Dictionaries from tuples
Convert a list of tuples into a dictionary
'''
# Example 11.12
# List of tuples
# Copy later