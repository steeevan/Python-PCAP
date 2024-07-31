'''
12 Functions, Generateor Functions, and Lambda Functions in Python

Functions: bespoke functions, parameters, arguments, default parameters, name scope, 
and important keywords such as return, None, and global

Generator Functions: bespoke generators, lazy evaluation and lazy iterators, 
generator termination, and generator expressions

Lambda Functions: functional programming, anonymous functions, 
and lambda functions within filter, map, reduce, sorted, and reversed functions
'''

'''
12.1 Defining Functions
Functions are defined using the 'def' keyword followed by the name of the function and parantheses.

'''
# Example 12.1
# A simple example of a user defined function
def product(number1, number):
    return number1 * number

# call the function (invoke)
a = 12
b = 10
c = product(a,b)

'''
12 .2 Arbitraty Arguments
Functions can accept an arbitrary number of arguments using the '*args' keywords (syntax)
'''
# Define a function to expect an arbitrary number of arguments
def product(*nums):
    x = 1
    for num in nums:
        x *= num
    return x

# Call the function with a tuple as argument
print(product(10,5,10,2))

# UNPACK the Arguments lists
# Define a function to test whether a given number is a prime number or not
def is_prime(num):
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def findPrimeBetween(start_num,end_num=10):
    return [num for num in range(start_num,end_num) if is_prime(num)]

args = [1,100]
print(findPrimeBetween(*args))

# USE KEYWORDS ARGUMENTS
print(findPrimeBetween(end_num=400,start_num=200))

'''
12.3 Arbitrary Keyword Arguments

'''
def concanate_words(**words):
    return ' '.join(words.values())

print(concanate_words(word1="Wonderful",word2="World",word3="of",word4= "Python"))

'''
12.4 Pass Statement
The 'pass' statement is used as a placeholder for future code, allowing the creation of empty functions
'''
# Example 12.4
def my_empty_function():
    pass


'''
12.5 None Keyword
'''

# define a function that does not return a value
def my_logging_function(message):
    print(message)
    

log = my_logging_function("Hello I am here to log")
print(type(log))
print(log)

'''
12.6 Function Recursion
Recursion occurs when a function calls itself
'''

# Calculates the Nth element in the fiboncci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    
print(fib(10))

'''
12.7 Local Scope Variables
Variables are defined inside a function and are only accessible within the function
'''


def calculate_weight(height, age):
    total_weight = height * age
    print(total_weight)
 


'''
 12.8 Generator Functions
 Generator functions use the 'yield' keyword to return a value and suspend their execution, 
 allowing them to be resumed
'''



# Example 12.8
def infinite_sequence_generator():
    counter = 0
    while True:
        yield counter
        counter += 1
# Call this generator function and lazily evaluate the next element in the iterable object
infinite_gen = infinite_sequence_generator()
print(next(infinite_gen)) # output: 0
print(next(infinite_gen)) # output: 1
print(next(infinite_gen)) # output: 2


'''
12.9 Generator Termination
Generators raise a 'StopIteration' exception when there are no further elements to generate
'''
# Define a generator to lazily return an ordered sequence of letters
def letter_seq_gen(start,stop, step=1):
    for ord_unicode in range(ord(start.lower()), ord(stop.lower()),step):
        
        yield chr(ord_unicode)
    
alphabet = letter_seq_gen('a','e',2)
print(next(alphabet))
print(next(alphabet))

alphabet = letter_seq_gen('a','z')
for letter in alphabet:
    print(letter, end=' ')

'''
12.10 Generator Expressions
Generator expressions are similar to list comprehensions but use parentheses instead of '[]'
'''
print()
# Example 12.10 
first_million = (num for num in range(1,1_000_000))
print(first_million)
print(next(first_million))
print(next(first_million))
print(next(first_million))

# Example 12.10.2
# Create a lazily evaluated generator object
alphabet = letter_seq_gen("a", "z")

# Convert the generator object into a list
alphabet_list = list(alphabet)
print(alphabet_list)  # Output: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']

'''
12.11 Lamda Functions
Lambda Functions are anonynous functions defined using the 'lambda' keyword. THey can have
any number of parameters but only one expression
'''
# Example 12.11.1
# Create a simple lambda function to square a given number
square = lambda n: n*n

# Call this function
print(square(5))

# Example 12.11.2
# Create a simple lambda function with three arguments
volume = lambda x, y, z: x * y * z

# Call this lambda function
print(volume(3,10,5))

'''
12.12 Using Lambda Functions
THese are often used in higer-order functions
'''
# Create a list of numbers
my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use a lambda function within filter() to filter even numbers
even_numbers = list(filter(lambda num: num % 2 == 0, my_numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

# Use a lambda function within map() to square odd numbers
squared_numbers = list(map(lambda num: num if num % 2 == 0 else num * num, my_numbers))
print(squared_numbers)  # Output: [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]

# Use a lambda function within reduce() to calculate the product of all numbers
from functools import reduce
product_of_numbers = reduce(lambda a, b: a * b, my_numbers)
print(product_of_numbers)  # Output: 3628800

# Use a lambda function within sorted() to sort a list of tuples
completed_football_league = [
    ('Manchester United', 75, 64, 35), 
    ('Aston Villa', 56, 48, 44), 
    ('Arsenal', 90, 73, 26), 
    ('Newcastle United', 56, 52, 40), 
    ('Liverpool', 60, 55, 37), 
    ('Chelsea', 79, 67, 30)
]
sorted_league = sorted(completed_football_league, key=lambda item: (item[1], item[2] - item[3]), reverse=True)
print(sorted_league)  # Output: [('Arsenal', 90, 73, 26), ('Chelsea', 79, 67, 30), ('Manchester United', 75, 64, 35), ('Liverpool', 60, 55, 37), ('Newcastle United', 56, 52, 40), ('Aston Villa', 56, 48, 44)]

'''
12.13 User-Defined
Lambda functions can be defined within other functions and returned as results.

Example 12.13
'''
# Create a Python function containing a lambda anonymous function
def multiply(multiplier):
    return lambda x: x * multiplier

# Instantiate a function that always doubles a given number
doubler = multiply(2)

# Call this function with the value 10
print(doubler(10))  # Output: 20

# Instantiate a function that always quadruples a given number
quadrupler = multiply(4)

# Call this function with the value 100
print(quadrupler(100))  # Output: 400

'''
12.14 Filter Function
The filter() function is used to construct an iterator 
from elements of an iterable for which a function returns True.
'''
# Create a function that will test whether a given number is even or not
def test_even(num):
    if num % 2 == 0:
        return True
    return False

# Apply this function to the list of numbers using the filter() function
my_even_numbers = list(filter(test_even, my_numbers))
print(my_even_numbers)  # Output: [2, 4, 6, 8, 10]

# Use a lambda function within filter() to perform the same task
my_even_numbers = list(filter(lambda num: num % 2 == 0, my_numbers))
print(my_even_numbers)  # Output: [2, 4, 6, 8, 10]


'''
12.15 Map Function
The map() function is used to apply a function to all items in an
 input list.
'''
# Create a function that will square a given number but only if that number is odd
def square_odd_number(num):
    if num % 2 == 0:
        return num
    return num * num

# Apply this function to the list of numbers using the map() function
my_squared_odd_numbers = list(map(square_odd_number, my_numbers))
print(my_squared_odd_numbers)  # Output: [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]

# Use a lambda function within map() to perform the same task
my_squared_odd_numbers = list(map(lambda num: num if num % 2 == 0 else num * num, my_numbers))
print(my_squared_odd_numbers)  # Output: [1, 2, 9, 4, 25, 6, 49, 8, 81, 10]


'''
12.16 Reduce Function
The reduce() function is used to apply a particular 
function passed in its argument to all of the list elements.

'''
from functools import reduce

# Create a function that will calculate the product of two given numbers
def product(a, b):
    return a * b

# Apply this function to the list of numbers using the reduce() function
my_product_of_numbers = reduce(product, my_numbers)
print(my_product_of_numbers)  # Output: 3628800

# Use a lambda function within reduce() to perform the same task
my_product_of_numbers = reduce(lambda a, b: a * b, my_numbers)
print(my_product_of_numbers)  # Output: 3628800





'''
12.17 Sorted Function 
The sorted() function returns a sorted list from the elements of any 
iterable.
'''
# Create a list of unordered numbers
my_unordered_numbers = [2, 100, 99, 3, 7, 8, 13, 48, 88, 38]

# Sort the list of numbers
sorted_numbers = sorted(my_unordered_numbers)
print(sorted_numbers)  # Output: [2, 3, 7, 8, 13, 38, 48, 88, 99, 100]

# Sort the list of numbers in descending order
sorted_numbers_desc = sorted(my_unordered_numbers, reverse=True)
print(sorted_numbers_desc)  # Output: [100, 99, 88, 48, 38, 13, 8, 7, 3, 2]

# Create a function to create a compound sorting key
def sorting_key(item):
    total_points = item[1]
    goal_difference = item[2] - item[3]
    return (total_points, goal_difference)

# Use this sorting function with the sorted() function to sort the football league by multiple keys
completed_football_league = [
    ('Manchester United', 75, 64, 35), 
    ('Aston Villa', 56, 48, 44), 
    ('Arsenal', 90, 73, 26), 
    ('Newcastle United', 56, 52, 40), 
    ('Liverpool', 60, 55, 37), 
    ('Chelsea', 79, 67, 30)
]
sorted_football_league = sorted(completed_football_league, key=sorting_key, reverse=True)
print(sorted_football_league)  # Output: [('Arsenal', 90, 73, 26), ('Chelsea', 79, 67, 30), ('Manchester United', 75, 64, 35), ('Liverpool', 60, 55, 37), ('Newcastle United', 56, 52, 40), ('Aston Villa', 56, 48, 44)]

# Use a lambda function within sorted() as the key function to perform the same task
sorted_football_league = sorted(completed_football_league, key=lambda item: (item[1], item[2] - item[3]), reverse=True)
print(sorted_football_league)  # Output: [('Arsenal', 90, 73, 26), ('Chelsea', 79, 67, 30), ('Manchester United', 75, 64, 35), ('Liverpool', 60, 55, 37), ('Newcastle United', 56, 52, 40), ('Aston Villa', 56, 48, 44)]




'''
12.18 Reversed Function
The reversed() function returns a reversed iterator.
'''
# Use the reversed() function to return a reversed iterable object
my_reversed_numbers = list(reversed(my_numbers))
print(my_reversed_numbers)  # Output: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Reverse a range of numbers
my_range = range(11, 21)
my_reversed_range = list(reversed(my_range))
print(my_reversed_range)  # Output: [20, 19, 18, 17, 16, 15, 14, 13, 12, 11]

# Reverse the characters in a string
my_string = 'abracadabra'
my_reversed_string = list(reversed(my_string))
print(my_reversed_string)  # Output: ['a', 'r', 'b', 'a', 'd', 'a', 'c', 'a', 'r', 'b', 'a']

'''
12.19 Sort Method 
The sort() method sorts the elements of a list in place.
'''
import copy

# Create a deepcopy of the previous list of tuples representing a football league
completed_football_league_deep_copy_1 = copy.deepcopy(completed_football_league)

# Sort the previous list of tuples representing a football league using the list sort() method
completed_football_league_deep_copy_1.sort(reverse=True, key=sorting_key)
print(completed_football_league_deep_copy_1)  # Output: [('Arsenal', 90, 73, 26), ('Chelsea', 79, 67, 30), ('Manchester United', 75, 64, 35), ('Liverpool', 60, 55, 37), ('Newcastle United', 56, 52, 40), ('Aston Villa', 56, 48, 44)]

# Use a lambda function within the list sort() method as the key function to perform the same task
completed_football_league_deep_copy_2 = copy.deepcopy(completed_football_league)
completed_football_league_deep_copy_2.sort(reverse=True, key=lambda item: (item[1], item[2] - item[3]))
print(completed_football_league_deep_copy_2)  # Output: [('Arsenal', 90, 73, 26), ('Chelsea', 79, 67, 30), ('Manchester United', 75, 64, 35), ('Liverpool', 60, 55, 37), ('Newcastle United', 56, 52, 40), ('Aston Villa', 56, 48, 44)]
