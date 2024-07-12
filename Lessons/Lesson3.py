'''
Python Fundamentals: Lesson 3
In this module, we will continue to cover the fundamental building blocks of the Python programming language, namely:

Functions and Methods - the difference between methods and functions
Input and Output - input, print, int, float and str functions
Formatting - formatting the output of the print function, and formatted string literals
Conditional Statements - if, if-else, if-elif, if-elif-else statements and the pass instruction

------------------------------------------------------------------------------------------------------------
1. Functions and Methods
Explanation:
Functions and methods are blocks of reusable code. Functions are defined using the def keyword and can be called anywhere in the code. Methods are functions that are associated with objects and are called on them.

Functions are standalone blocks of code designed to perform a specific task and can be used independently.
Methods are functions that belong to an object (like a string or a list) and are called on that object.
Code Examples:
'''
# A simple function to return the product of two given numbers
def product(number_1, number_2):
    return number_1 * number_2

print(product(12, 20))  # Output: 240

# The common len() function given a string
my_string = 'Hello World!'
print(len(my_string))  # Output: 12

# A common string method that will return the string all in uppercase
my_string = 'Hello World!'
print(my_string.upper())  # Output: HELLO WORLD!

'''
Tips:
- Use functions to encapsulate code that performs a specific task to make your code more modular and reusable.
- Methods are particularly useful for operations related to specific data types like strings and lists.
- Naming conventions: Use descriptive names for functions and methods to make your code more readable.
------------------------------------------------------------------------------------------------------------------------

2. Input and Output
Explanation:
Input and output functions are used to receive data from the user and display data to the user, respectively.

2.1. Input Function
Explanation:
The input() function is used to get user input. You can provide a prompt message as an argument to guide the user.

Code Examples:
'''
# Input function without a prompt message argument
full_name = input()
print(f'Your Full Name is: {full_name}')
# Input: Jillur Quddus
# Output: Your Full Name is: Jillur Quddus

# Input function with a prompt message argument
fname = input('Please enter your first name: ')
lname = input('Please enter your last name: ')
print(f'Hello {fname} {lname}!')
# Input: Please enter your first name: Jillur
# Input: Please enter your last name: Quddus
# Output: Hello Jillur Quddus!

'''
Tips:
Always provide a prompt message to make the input request clear to the user.
Remember that input() returns a string, so you might need to convert it to the appropriate data type (e.g., int or float) for further processing.
-------------------------------------------------------------------------------------------------------------------------------------------------------

2.2. Int Function
Explanation:
The int() function converts a string or number to an integer. It can also take a second argument to specify the base of the number being converted.

Code Examples:
'''
# Integer input using the int function (default base 10)
age = int(input('Please enter your age: '))
print(f'You are {age} years old')
# Input: Please enter your age: 28
# Output: You are 28 years old

# Integer input using the int function and base 16
age = int(input('Please enter your age: '), 16)
print(f'You are {age} years old')
# Input: Please enter your age: 1c
# Output: You are 28 years old

'''
Tips:
Use int() to convert user input to an integer, especially when dealing with numerical data.
Be cautious when specifying bases other than 10, and ensure that the input format matches the expected base.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
2.3. Float Function
Explanation:
The float() function converts a string or number to a floating-point number.

Code Examples:
'''
# Floating point input using the float function
height = float(input('Please enter your height in metres: '))
print(f'You are {height}m tall')
# Input: Please enter your height in metres: 2
# Output: You are 2.0m tall

'''
Tips:
Use float() to handle inputs that require decimal points.
Validate user input to ensure it is in the correct format before converting to a float to avoid errors.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
2.4. Str Function
Explanation:
The str() function converts a value to a string, making it possible to concatenate different data types with strings.

Code Examples:
'''
# Without the str function we cannot concatenate a number to a string
pi = 3.141592653589793238462643
print('The value of π is: ' + pi)
# Output: TypeError: can only concatenate str (not "float") to str

# The str function will convert pi into a string
print('The value of π is: ' + str(pi))
# Output: The value of π is: 3.141592653589793

'''
Tips:
Use str() to convert numbers and other data types to strings for concatenation or display purposes.
Combine str() with formatted string literals (f-strings) for more readable and flexible code.
-----------------------------------------------------------------------------------------------------------------------------------------------------------
2.5. Print Function
Explanation:
The print() function outputs text to the console. It can take multiple arguments and has options for customizing the output format.
'''
# Print a given string
print("My name is Jillur Quddus")
# Output: My name is Jillur Quddus

# Print a given collection of strings
print("Software Engineer", "Data Scientist", "Technical Architect")
# Output: Software Engineer Data Scientist Technical Architect

# Print a given collection of strings with a separator
print("Software Engineer", "Data Scientist", "Technical Architect", sep=', ')
# Output: Software Engineer, Data Scientist, Technical Architect

# Print a list of occupations on the same line
print("My Roles", end=": ")
print("Software Engineer", "Data Scientist", "Technical Architect", sep=', ')
# Output: My Roles: Software Engineer, Data Scientist, Technical Architect
'''
Tips:
Use the sep parameter to customize the separator between multiple arguments in print().
Use the end parameter to change the default newline character at the end of the output.
-------------------------------------------------------------------------------------------------------------
3. Formatting
Explanation:
Formatted string literals (also known as f-strings) provide a way to embed expressions inside string literals, using {}.

3.1. Formatted String Literals
Explanation:
Formatted string literals, introduced in Python 3.6, allow embedding expressions inside string literals, using curly braces {}.

Code Examples:
'''
# Print the value of e (Euler's number) using formatted string literals
e = 2.718281828459045235360287
print(f'The value of e is {e}')
# Output: The value of e is 2.718281828459045

# Print the value of e but to 3 decimal points
print(f'The value of e to 3 decimal points is {e:.3f}')
# Output: The value of e to 3 decimal points is 2.718

# Print age as a number of days
age = int(input('Please enter your age: '))
print(f'You are at least {age * 365} days old')
# Input: Please enter your age: 28
# Output: You are at least 10220 days old

# Access common mathematical constants using the Python math module
import math
print(f'The value of π to 3 decimal points is {math.pi:.3f}')
print(f'The value of e to 3 decimal points is {math.e:.3f}')
# Output: 
# The value of π to 3 decimal points is 3.142
# The value of e to 3 decimal points is 2.718
'''
Tips:
Use f-strings for cleaner and more readable code when embedding expressions within strings.
Control the format of numbers using format specifiers within the curly braces (e.g., {e:.3f} for three decimal places).
-------------------------------------------------------------------------------------------------------------------------
4. Conditional Statements
Explanation:
Conditional statements allow for decision-making in code based on certain conditions. They include if, if-else, if-elif, and if-elif-else statements.

4.1. If Statement
Explanation:
The if statement executes a block of code if a specified condition is true.

Code Examples:
'''
# If statement using a comparison operator
age = int(input('Please enter your age: '))
if age >= 18:
    print("You are allowed to vote in UK elections")
# Input: Please enter your age: 19
# Output: You are allowed to vote in UK elections

# If statement using comparison and logical operators
if age >= 16 and age < 21:
    print("You are allowed to work full-time, join the armed forces, drive and vote but you cannot yet adopt a child in the UK")
# Output: You are allowed to work full-time, join the armed forces, drive and vote but you cannot yet adopt a child in the UK

# If statement using an identity operator
a = 10
b = 20
c = a

if a is b:
    print("a and b are the same object at object memory level")
if a is c:
    print("a and c are the same object at object memory level")
if b is c:
    print("b and c are the same object at object memory level")
# Output: a and c are the same object at object memory level

# If statement using a membership operator
first_ten_prime_numbers = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
if 13 in first_ten_prime_numbers:
    print("13 is in the first ten prime numbers")
# Output: 13 is in the first ten prime numbers

'''
Tips:
Use logical operators (and, or, not) to combine multiple conditions in an if statement.
Use identity operators (is, is not) to compare objects at the memory level.
Use membership operators (in, not in) to check if a value is present in a sequence.
------------------------------------------------------------------------------------------------------------------
4.2. If-else Statement
Explanation:
The if-else statement allows execution of a block of code if a condition is true, and another block of code if the condition is false.

Code Examples:
'''
# If-else statement using a comparison operator
age = int(input('Please enter your age: '))
if age >= 18:
    print("You ARE allowed to vote in UK elections")
else:
    print("You are NOT yet allowed to vote in UK elections")
# Input: Please enter your age: 17
# Output: You are not yet allowed to vote in UK elections
'''
Tips:
Use else to handle cases where the condition in the if statement is not met.
Ensure that else is used to cover all other possible conditions that were not handled by the if statement.
----------------------------------------------------------------------------------------------------------
4.3. If-elif Statement
Explanation:
The if-elif (else if) statement allows for multiple conditions to be checked in sequence.

Code Examples:
'''
# If-elif statements using comparison and logical operators
age = int(input('Please enter your age: '))
if age >= 21:
    print("You are entitled to undertake all legally permissible activities in the UK")
elif age >= 14 and age < 16:
    print("You can get a part-time job in the UK")
    print("But you cannot work full-time nor get married in the UK")
elif age >= 16 and age < 18:
    print("You can get a full-time job and get married in the UK")
    print("But you cannot yet vote in the UK")
elif age >= 18 and age < 21:
    print("You can get a full-time job, get married and vote in the UK")
    print("But you cannot adopt a child in the UK")
else:
    print("You can't do much by yourself unfortunately")
    print("Stay in school and listen to your parents!")
    if age >= 10:
        print("But since you are greater than 10 years old, you have full criminal responsibility for your actions and can be convicted of a criminal offence in the UK")
        print("So think before you act!")
# Input: Please enter your age: 11
# Output: 
# You can't do much by yourself unfortunately
# Stay in school and listen to your parents!
# But since you are greater than 10 years old, you have full criminal responsibility for your actions and can be convicted of a criminal offence in the UK
# So think before you act!
'''
Tips:
Use elif to check multiple conditions in sequence.
Ensure that each elif condition is mutually exclusive to avoid conflicts.
---------------------------------------------------------------------------------------------
4.4. Pass Statement
Explanation:
The pass statement is a placeholder for future code. It allows you to write a statement that does nothing, acting as a placeholder for code to be added later.

Code Examples:
'''
# Use the pass statement to only print if x is even
x = int(input('Please enter an integer number: '))
if x % 2 != 0:
    pass
else:
    print(f"{x} is an even number")
# Input: Please enter an integer number: 88
# Output: 88 is an even number

'''
Tips:
Use pass when you need to have a statement syntactically but do not want to execute any code.
pass is often used in loops, functions, and conditional statements as a placeholder during development.
'''
