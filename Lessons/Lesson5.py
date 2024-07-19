'''
Lesson 5 
Basic Lists in Python


5.1 Defining a List
A list in Python is an ordered collection of items (elements) that can be of any type: integers,
strings, or even other lists. Lists are defined by placing elements inside a square bracket ('[]')
seperated by commas.

Empty List: An empty list contains no elements and is defined with empty square brackets
Populated List: List can be populated with elements at the time of definition
'''
# Example 5.1
empty_list = []         # Empty list
squares = [1,2,4,9,16]  # Populated List

'''
5.2 Index and Negative Indexing
List are zero-indexed, meaning the first element has an index of  0, the second an index of 1, and so on
Negative indexing starts from the end, where -1 is the last element, -2 is the second to last, and so on

Positive indexing: Access elements by their position from the start
Negative indexing: Access elements by the position from the end

'''
#Example 5.2

# Access elements in a list by their index numbers
print(squares[0])   # First element
print(squares[3])   # Fourth element
print(squares[-1])  # Last element
print(squares[-4])  # Fourth element from the end

'''
5.3 List Slicing
Slicing allows you to access a subset of a list. The syntax for slicing is 'list[start:end]', 
where 'start' is the index to start from (inclusive), and 
'end' is the index to stop at (exclusive)

Full Slice: list[:] returns all elements
Sublist: list[start:end] return elements from start to end - 1
Ommited Indices: if 'start' is ommitted, slicing starts from the beginning, 
if the 'end' if ommitted slicing goes to the end of the list
'''
# Example 5.3

# Slicing a list
print(squares[0:2])  # First two elements
print(squares[2:])   # From the third element to the end
print(squares[:3])   # First three elements
print(squares[:])    # All elements
print(squares[-3:-1]) # Third to last element to the second to last
print(squares[-1:])  # Last element
print(squares[:-2])  # All elements except the last two

# Define an end index that is purposefully too large
print(squares[0:100]) # Python will handle out-of-range slicing gracefully

'''
5.4 List length
the 'len()' function returns the number of elements in a list. This is useful for determining
the size of the list.
'''
# Example 5.4
print(f'The length of the squares list is: {len(squares)} elements')

'''
5.5 List Membership
You can check if an element exists in a list using the 'in' keyword. This returns 'True'
if the element is found and 'False' otherwise
'''
# Example 5.5
x = 169
if x in squares:
    print(f"{x} exists in our list of square numbers")
else:
    print(f"{x} does not exist in our list of square numbers")

'''
5.6 Modifying Elements in a list
You can modify elements in a list by access them via their index and assigning a new value
'''
# Modify a specific element in a list
squares[0] = 0
print(squares)

# Revert to the original value
squares[0] = 1
print(squares)

'''
5.7 Deleting Elements and Lists
Elements can be removed from a list or the entire list can be deleted using the 'del' keyword

Remove Element: 'del list[index]
Delete List:    'del list'
'''
# Remove a specific element from a list
del squares[-1]
print(squares)

# Delete a list collection entirely
del empty_list
# print(empty_list)  # Uncommenting this will raise a NameError

'''
5.8 Joining Lists
You can concatenate two lists using '+' operator. This operation returns a new list that is the
result of a joining two lists.

'''
# Append all elements from more_squares to squares
more_squares = [25, 36, 49, 64, 81, 100]
updated_squares = squares + more_squares
print(updated_squares)

'''
5.9 List Methods
Python provides a variety of built-in methods to manipulate lists. Some of the most commonly used 
methods are:

- append(element): Adds an element to the end of the list.
- extend(iterable): Adds all elements from an iterable to the end of the list.
- insert(index, element): Inserts an element at the specified index.
- remove(element): Removes the first occurrence of the element from the list.
- pop([index]): Removes and returns the element at the specified index 
    (or the last element if the index is not specified).
- clear(): Removes all elements from the list.
- index(element[, start[, end]]): Returns the index of the first occurrence of the element.
- count(element): Returns the number of occurrences of the element.
- sort(): Sorts the list in ascending order.
- reverse(): Reverses the order of the list.
- copy(): Returns a shallow copy of the list.
'''
# Examples 5.9
# list.append(element)
squares.append(25)
print(squares)

# list.extend(newlist)
del more_squares[0]
squares.extend(more_squares)
print(squares)

# list.insert(index, element)
squares.insert(0, 0)
print(squares)

# list.remove(element)
squares.remove(0)
print(squares)

# list.pop([index])
squares.pop()
print(squares)

# list.clear()
squares.clear()
print(squares)

# Populate the list of square numbers again
squares.extend([1, 4, 9, 16, 25, 36, 49, 64, 81, 100])

# list.index(element[, start[, end]])
print(squares.index(64))

# list.count(element)
print(squares.count(169))

# list.sort()
squares.sort()
print(squares)

# list.reverse()
squares.reverse()
print(squares)

# list.copy()
squares_copy = squares.copy()
print(squares_copy)
