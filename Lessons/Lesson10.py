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