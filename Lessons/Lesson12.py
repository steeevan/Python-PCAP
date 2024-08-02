'''
12 Functions, Generator Functions, and Lambda Functions in Python









'''

'''
12.1 Defining Functions
- Functions are defined using the 'def' keyword followed by the name of the function and parantheses
- Methods are specific to things like the 'import math' and 'import random'
functions are all-use thins like 'print' 
'''
# Example 12.1
def product(number1,  number):
    return number1 * number

# Call the function (invoke)
a = 12
b = 10
c = product(a,b)

'''
12.2 Arbitrary Arguments
- Functions can accept an arbitrary number of arguments using the '*args' keyword (syntax)
'''
# Define a function to expect an arbitrary number of arguments
def product(*nums):  # star in front of variable accepts as many numbers as it can
    x = 1
    for num in nums:
        x *= num
    return x

# Call the function with a tuple as arguments
print(product(2, 5, 10, 3, 3, 3, 3, 3, 3, 900, 900, 900, 10000, 100000, 100000, 100000, 10000, 9999, 99999, 9999, 9999 ,999 ,999, 999 ,999, 99999, 9999999999999, 99999999999999999, 99999999999999999999999999999, 99999999999999999999999999))

# Unpack the Arguments lists
# Define a function to test whether a given number is a prime number or not
def is_prime(num):
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def findPrimeBetween(start_num, end_num):
    return [num for num in range(start_num, end_num) if is_prime(num)]

args = [1,100]
print(findPrimeBetween(*args))

# Use  keywords arguments
print(findPrimeBetween(start_num = 100, end_num = 200))

'''
12.3 Arbitrary Keyword Arguments

'''
def concanate_words(**words):  # Double asterik pulls everything together, used where there are keyword arguments. Single asterik is for pulling everything together without any values
    return ' '.join(words.values())

print(concanate_words(word1 = "Wonderful1", word2 = "World", word3 = "of", word4 = "Python")) # Has to have values or else there will be error

'''
12.4 Pass Statement
- The 'pass' statement is used as a placeholder for future code allowing the creation of empty functions
'''
# Example 12.4
def my_empty_function():
    pass # To come back to code if you are not working on it yet


'''
12.5 None Kyeword
'''

# Define a function that does not return a value
def my_logging_function(message):
    print(message)


log = my_logging_function("Hello I am here to log") # The "Hello i am here to log" is the message
print(type(log))# Log does not get anthing back from the function because there is no 'return'
print(log)

'''
12.6 Function Recursion
- Recursiom occurs when a function calls itself
'''

# Calculates the Nth elementin the fibonacci sequence
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n - 2)
    
print(fib(10)) # Not taking the actual number, we are taling the number in the 10 place in the sequence

'''
12.7 Local Scope Variables
- Variables are defined inside a function and are only accessible within the function
'''
def calculate_weight(height, age):
    total_weight = height * age # 'total_weight cannot be called outside of the function, but if you use 'global total_weight" you are able to access it outside the function






'''
12.8 Generator Functions
- Generator functions use the 'yield'  keyword to return a value and suspend their execution,
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
print(next(infinite_gen)) # output = 0  Next gives out the next iteration
print(next(infinite_gen)) # output = 1
print(next(infinite_gen)) # output = 2

for i in range(1,100):
    print(next(infinite_gen))

'''
12.9 Generator Termination
- Generators raise a 'StopIteration' exception when there are no further elements to generate
'''
# Define a generator to lazily return an ordered dequence ot letters
def letter_seq_gen(start, stop, step = 1):
    for ord_unicode in range(ord(start.lower()), ord(stop.lower()), step):

        yield chr(ord_unicode)

alphabet = letter_seq_gen('a', 'e')
print(next(alphabet))
print(next(alphabet))

alphabet = letter_seq_gen('a', '{')
for letters in alphabet:
    print(letters, end=' ')

'''
12.10 Generator Expressions
- Generator Expressions are similar to list comprehension but uses parantheses instead of '[]'
'''
print()
# Example 12.10
first_million = (num for num in range(1,1_000_000)) # Paranthese is lazy generator that prints everything separately but brackets print everything together
print(first_million)
print(next(first_million))
print(next(first_million))
print(next(first_million))

# Example 12.10.2
# Create a lazily evaluated generator object
alphabet = letter_seq_gen("a", "{")

# Convert the generator object into a list
alphabet_list = list(alphabet)
print(alphabet_list) # output = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z]

'''
12.11 Lambda Functions
- Lambda functions are anonymous functions defined using the 'lambda' keyword. They can have
any number of parameters but only one expression
'''
# Example 12.11.1
# Create a simple lambda function to square a given number
square = lambda n: n * n

# Call this function
print(square(5))

# Example 12.11.2
# Create a simple lambda function with 3 arguments
volume = lambda x, y, z: x * y * z

# Call this lambda function
print(volume(3, 10 ,5))





#Activity 1.1
# Create a tuple containing three different data types.
tuple = (1, "ONE", 1.1)

# Print the tuple to the console.
print(tuple)




# Activity 1.2
# Access and print the second item in the tuple you created.
print(tuple[1])

# Try to modify the second item in the tuple and observe the result.






# Activity 1.3
# Use the count() method to find the number of times a specific item appears in your tuple.
print(tuple.count(1))

# Use the index() method to find the index of a specific item in your tuple.
print(tuple.index("ONE"))





# Activity 1.4
# Create a tuple with three elements and unpack the elements into three variables.\
tup = (1, 2, 3)
a, b, c = tup

# Print the variables to verify the unpacking.
print(a, b, c)





# Activity 2.1
# Create a dictionary with at least three key-value pairs.
d = {1:2, 3:4, 5:6}

# Print the dictionary to the console.
print(d)





# Activity 2.2
# Access and print the value associated with a specific key in your dictionary.
print(d[1])

# Try to access a key that does not exist and handle the exception.
try:
    print(d[58])
except:
    print("It is okie")




# Activity 2.3
# Modify the value of an existing key in your dictionary.
d[1] = 45

# Print the modified dictionary to verify the change.
print(d)




# Activity 2.4
# Add a new key-value pair to your dictionary.
d[123] = 321

# Print the dictionary to verify the addition.
print(d)




# Activity 2.5
# Remove a key-value pair from your dictionary using the del keyword.
del d[1]

# Print the dictionary to verify the removal.
print(d)

# Remove a key-value pair using the pop() method.
d.pop(3)

# Print the dictionary to verify the removal.
print(d)




# Activity 2.6
# Iterate through the keys of your dictionary and print them.
for i in d:
    print(d)

# Iterate through the values of your dictionary and print them.


# Iterate through the key-value pairs of your dictionary and print them.