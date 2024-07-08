'''
Lesson Plan: Funamental Building Blocks of Python

Objectives:
 - Understand the basic concepts of python programming
 - learn about variout types of literals in Python
 - Explore different operators and their usage in Python
'''

# Basic Conepts
'''
1.1 Logical and Physical Lines
- Logical Line: A logical line is a statement that the Python interpreter executes. In Python
a logical line can span multiple physical lines using explicit or implicit line joining.
- Physical Line: A  physical line is what you see as a single line your text editor.
'''

# Example 1.1
# logical line spanning a single physical line
my_string = "My entire string on a single physical line."
print(my_string)

'''
1.2 Explicit Line Joining
- You can join two physical lines using a backslash '\'
'''
# Example 1.2 
# string literal spanning two physical lines.
my_string = "The first part of the string. \
The second part of the string. "
print(my_string)

# Control flow spannning multiple physical lines
year = 2024
month = 7
day = 32
if 1900 < year < 2100 and 1 <= month<= 12 \
and 1 <= day <= 31:
    print("You have entered a valid date")     # Valid date

'''
1.3 Implicit Line Joining
- Parantheses '()' , brackets '[]', and braces '{}' can be used to span multiple
lines without using '\'.
'''
# Example 1.3
# Implicit Line joining 
days = ("Monday", "Tuesday", "Wednesday", "Thursday","Friday", # Weekdays
        "Saturday", "Sunday") # Weekened
print(days)

'''
1.4 Multi-Logical Physical lines
- You can write multiple logical lines in a single physical line by seperating
them with a semicolon ';'
'''
# Example 1.4
# Multiple logical lines spanning a single physical line
from datetime import date; today = date.today(); print(today)

'''
1.5 Indentation
- Indentation is used to define the blocks of code. Incorrect indentation will result in an 
'IndentationError'
'''
# Correct indentation
x = 101
if x >= 100:
    print("Your number is bigger than or equal to 100")
else:
    print("Your number is less than 100")
# Output: Your number is bigger than or equal to 100
'''
# Incorrect indentation
x = 100
    y = 200    # Incorrect indentation
if x >= y:
print("X is bigger than or equal to Y")    # Incorrect indentation 
else:
    print("Y is bigger than X")
# Output: IndentationError: unexpected indent
'''
#**********************************************************************************************
'''
2 Literals

2.1 String Literals
- String literals can enclosed in single quotes, double quotes, or triple quotes.
'''
# Example 2
my_first_string = 'Hello World'
my_second_string = "Hello World Part 2"
my_third_string = '''Hello World Part 3'''
print(my_first_string)
print(my_second_string)
print(my_third_string)
my_fourth_string = "line1.\n Line 2."
print(my_fourth_string)
my_fifth_string = r"Line1. \n Line 2"
print(my_fifth_string)

'''
2.2 Boolean Literals
- Boolean literals are 'True' and 'False'
'''
# Example 2.2 
my_first_boolean = True
my_second_boolean = False

print(my_first_boolean)
print(my_second_boolean)
print(1== True)
print(1 == False)
print( 0 == True)
print(0 == False)

'''
2.3 Numerical Literals
- Python supports integers, floating-points, and imaginary literals
'''
# 2.3.1 Integer Literals
decimal_integer = 100
binary_integer = 0b1100100
octal_integer = 0o144
hexadecimal_integer = 0x64
decimal_groupings_integer = 100_000_000

print(decimal_integer)
print(binary_integer)
print(octal_integer)
print(hexadecimal_integer)
print(decimal_groupings_integer)

# 2.3.2 Floating Point Literals
my_first_number = 3.14
my_second_number = 10e2
my_third_number = 100e-5
my_fourth_number = 10.
my_fifth_number = .12345
my_sixth_number = 3.14_15_93

print(my_first_number)
print(my_second_number)
print(my_third_number)
print(my_fourth_number)
print(my_fifth_number)
print(my_sixth_number)

# 2.4 Special Literals
# Python has special literlas 'None' which represents the absence of value
x = None
print(x)
if x:
    print('x is True')
else:
    print('x is not True')
print(bool(None))

# 2.5 Imaginary Literals
# Imaginary literals
my_first_complex_number = 10j
my_second_complex_number = .10j
my_third_complex_number = 2+3j

print(my_first_complex_number)
print(my_second_complex_number, 
      my_second_complex_number.real, 
      my_second_complex_number.imag)
print(my_third_complex_number, 
      my_third_complex_number.real, 
      my_third_complex_number.imag)