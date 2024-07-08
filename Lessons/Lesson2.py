'''
Lesson 2: Operators in Python

Lesson Objectives:
- Understand the different types of operators in Python
- Learn how to use arithmetic, assignment, comparison, logical, identity, membership, bitwise, and unary operators
- Apply these operators in code examples and solve challenges

'''

'''
1 Arithmetic Operators

Explanation:
Arithmetic operators are used to perform basic mathematical operations 
such as addition, subtraction, multiplication, division, modulus, exponentiation, and floor division.
'''
# Example 1
# Addition
print(13 + 7)  # Output: 20

# Subtraction
print(10 - 7)  # Output: 3

# Multiplication
print(64 * 8)  # Output: 512

# Division
print(225 / 15)  # Output: 15.0

# Modulus (remainder after division)
print(69 % 8)  # Output: 5

# Exponentiation (raising by a power)
print(2 ** 5)  # Output: 32

# Floor division (quotient without remainder)
print(100 // 7)  # Output: 14
'''
In-Depth Explanation:
- Addition (+): Adds two numbers. Here, 13 + 7 results in 20.
- Subtraction (-): Subtracts the second number from the first. Here, 10 - 7 results in 3.
- Multiplication (*): Multiplies two numbers. Here, 64 * 8 results in 512.
- Division (/): Divides the first number by the second. Here, 225 / 15 results in 15.0. The result is a float.
- Modulus (%): Returns the remainder after division. Here, 69 % 8 results in 5 because 69 = 8*8 + 5.
- Exponentiation (**): Raises the first number to the power of the second. Here, 2 ** 5 results in 32 (2 raised to the power of 5).
- Floor Division (//): Divides the first number by the second and returns the largest integer less than or equal to the result. 
  Here, 100 // 7 results in 14 because 100 / 7 is approximately 14.285, and the floor value is 14.
'''

'''
2. Assignment Operators

Explanation:
Assignment operators are used to assign values to variables. 
They combine assignment with other operations such as addition, subtraction, multiplication, etc.

'''
# Assignment
x = 10
print(x)  # Output: 10

# Add and assign (x = x + 5)
x += 5
print(x)  # Output: 15

# Subtract and assign (x = x - 2)
x -= 2
print(x)  # Output: 13

# Multiply and assign (x = x * 4)
x *= 4
print(x)  # Output: 52

# Divide and assign (x = x / 2)
x /= 2
print(x)  # Output: 26.0

# Modulus and assign (x = x % 4)
x %= 4
print(x)  # Output: 2.0

# Exponentiation and assign (x = x ** 8)
x **= 8
print(x)  # Output: 256.0

# Floor division and assign (x = x // 15)
x //= 15
print(x)  # Output: 17.0

# Bitwise AND and assign (x = x & 18)
x = int(x)
x &= 18
print(x)  # Output: 16

# Bitwise OR and assign (x = x | 10)
x |= 10
print(x)  # Output: 26

# Bitwise XOR and assign (x = x ^ 2)
x ^= 2
print(x)  # Output: 24

# Bitwise signed right shift and assign (x = x >> 1)
x >>= 1
print(x)  # Output: 12

# Bitwise zero fill left shift and assign (x = x << 2)
x <<= 2
print(x)  # Output: 48
'''
In-Depth Explanation:
- Assignment (=): Assigns the value on the right to the variable on the left. Here, x = 10 assigns 10 to x.
- Add and Assign (+=): Adds the right operand to the left operand and assigns the result to the left operand. Here, x += 5 is equivalent to x = x + 5, resulting in 15.
- Subtract and Assign (-=): Subtracts the right operand from the left operand and assigns the result to the left operand. Here, x -= 2 is equivalent to x = x - 2, resulting in 13.
- Multiply and Assign (*=): Multiplies the left operand by the right operand and assigns the result to the left operand. Here, x *= 4 is equivalent to x = x * 4, resulting in 52.
- Divide and Assign (/=): Divides the left operand by the right operand and assigns the result to the left operand. Here, x /= 2 is equivalent to x = x / 2, resulting in 26.0.
- Modulus and Assign (%=): Takes the modulus using the left and right operands and assigns the result to the left operand. Here, x %= 4 is equivalent to x = x % 4, resulting in 2.0.
- Exponentiation and Assign (**=): Raises the left operand to the power of the right operand and assigns the result to the left operand. Here, x **= 8 is equivalent to x = x ** 8, resulting in 256.0.
- Floor Division and Assign (//=): Performs floor division using the left and right operands and assigns the result to the left operand. Here, x //= 15 is equivalent to x = x // 15, resulting in 17.0.
- Bitwise AND and Assign (&=): Performs bitwise AND using the left and right operands and assigns the result to the left operand. Here, x &= 18 is equivalent to x = x & 18, resulting in 16.
- Bitwise OR and Assign (|=): Performs bitwise OR using the left and right operands and assigns the result to the left operand. Here, x |= 10 is equivalent to x = x | 10, resulting in 26.
- Bitwise XOR and Assign (^=): Performs bitwise XOR using the left and right operands and assigns the result to the left operand. Here, x ^= 2 is equivalent to x = x ^ 2, resulting in 24.
- Bitwise Right Shift and Assign (>>=): Performs bitwise right shift using the left and right operands and assigns the result to the left operand. Here, x >>= 1 is equivalent to x = x >> 1, resulting in 12.
- Bitwise Left Shift and Assign (<<=): Performs bitwise left shift using the left and right operands and assigns the result to the left operand. Here, x <<= 2 is equivalent to x = x << 2, resulting in 48.
'''

'''
3. Comparison Operators
Explanation:
Comparison operators are used to compare two values. They return a Boolean value (True or False) indicating the result of the comparison.
'''
# Equal
print(10 == 100)  # Output: False

# Not equal
print(2 != 5)  # Output: True

# Greater than
print(13 > 12)  # Output: True

# Less than
print(100 < 1_000_000)  # Output: True

# Greater than or equal to
print(15 >= 15)  # Output: True

# Less than or equal to
print(20 <= 19)  # Output: False

'''
In-Depth Explanation:
- Equal (==): Checks if the values of two operands are equal. Here, 10 == 100 is False because 10 is not equal to 100.
- Not Equal (!=): Checks if the values of two operands are not equal. Here, 2 != 5 is True because 2 is not equal to 5.
- Greater Than (>): Checks if the left operand is greater than the right operand. Here, 13 > 12 is True because 13 is greater than 12.
- Less Than (<): Checks if the left operand is less than the right operand. Here, 100 < 1_000_000 is True because 100 is less than 1,000,000.
- Greater Than or Equal To (>=): Checks if the left operand is greater than or equal to the right operand. Here, 15 >= 15 is True because 15 is equal to 15.
- Less Than or Equal To (<=): Checks if the left operand is less than or equal to the right operand. Here, 20 <= 19 is False because 20 is not less than or equal to 19.
'''

'''
4. Logical Operators
Explanation:
Logical operators are used to combine conditional statements. They include and, or, and not.
'''
# AND
print(1 < 100 and 10 < 100)  # Output: True

# OR
print(13 > 14 or 1 > 0)  # Output: True

# NOT
print(not(1 < 100 and 10 < 100))  # Output: False

'''
In-Depth Explanation:
- AND (and): Returns True if both statements are true. Here, 1 < 100 and 10 < 100 is True because both conditions are true.
- OR (or): Returns True if at least one of the statements is true. Here, 13 > 14 or 1 > 0 is True because the second condition (1 > 0) is true.
- NOT (not): Reverses the result of the condition. Here, not(1 < 100 and 10 < 100) is False because the inner condition is True, and not operator reverses it.
'''

'''
5. Identity Operators

Explanation:
Identity operators are used to compare the memory location of two objects. They include is and is not.
'''
x = 10
y = 100.0

# IS
print(x is y)  # Output: False
print(x is x)  # Output: True

# IS NOT
print(x is not y)  # Output: True

x = y
print(x is y)  # Output: True
print(x is not y)  # Output: False
'''
In-Depth Explanation:
- IS (is): Checks if both operands refer to the same object. Here, x is y is False because x and y are different objects, but x is x is True because x is compared with itself.
- IS NOT (is not): Checks if both operands do not refer to the same object. Here, x is not y is True because x and y are different objects.
- When x = y, both x and y refer to the same object, so x is y is True and x is not y is False.
'''

'''
6. Membership Operators

Explanation:
Membership operators are used to test if a sequence is presented in an object. They include in and not in.
'''
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# IN
print('Thursday' in weekdays)  # Output: True
print('Saturday' in weekdays)  # Output: False

# NOT IN
print('Sunday' not in weekdays)  # Output: True

'''
In-Depth Explanation:
- IN (in): Returns True if the specified element is present in the sequence. 
Here, 'Thursday' in weekdays is True because 'Thursday' is an element of weekdays.
- NOT IN (not in): Returns True if the specified element is not present in the sequence. 
Here, 'Saturday' in weekdays is False because 'Saturday' is not an element of weekdays.
'''

'''
7. Bitwise Operators
Explanation:
- Bitwise operators are used to perform operations on binary numbers. They include & (AND), | (OR), ^ (XOR), ~ (NOT), >> (right shift), and << (left shift).
'''
# Bitwise AND
print(17 & 18)  # Output: 16

# Bitwise OR
print(16 | 10)  # Output: 26

# Bitwise XOR
print(26 ^ 2)  # Output: 24

# Bitwise NOT
print(~4)  # Output: -5

# Bitwise signed right shift
print(24 >> 2)  # Output: 6

# Bitwise zero fill left shift
print(12 << 2)  # Output: 48
'''
In-Depth Explanation:
- Bitwise AND (&): Compares each bit of the first operand with the corresponding bit of the second operand. If both bits are 1, the corresponding result bit is set to 1. Here, 17 & 18 results in 16:
    17 in binary: 00010001  
    18 in binary: 00010010
    Result: 00010000 (which is 16 in decimal)
- Bitwise OR (|): Compares each bit of the first operand with the corresponding bit of the second operand. If at least one of the bits is 1, the corresponding result bit is set to 1. Here, 16 | 10 results in 26:
    16 in binary: 00010000
    10 in binary: 00001010
    Result: 00011010 (which is 26 in decimal)
- Bitwise XOR (^): Compares each bit of the first operand with the corresponding bit of the second operand. If the bits are different, the corresponding result bit is set to 1. Here, 26 ^ 2 results in 24:
    26 in binary: 00011010
    2 in binary: 00000010
    Result: 00011000 (which is 24 in decimal)
- Bitwise NOT (~): Inverts each bit of the operand. Here, ~4 results in -5:
    4 in binary: 00000100
    Inverted: 11111011 (in two's complement, which represents -5)
- Bitwise Right Shift (>>): Shifts the bits of the first operand to the right by the number of positions specified by the second operand. Here, 24 >> 2 results in 6:
    24 in binary: 00011000
    Shifted right by 2: 00000110 (which is 6 in decimal)
- Bitwise Left Shift (<<): Shifts the bits of the first operand to the left by the number of positions specified by the second operand. Here, 12 << 2 results in 48:
    12 in binary: 00001100
    Shifted left by 2: 00110000 (which is 48 in decimal)
'''

'''
8. Unary Operators
Explanation:
Unary operators operate on a single operand and include operations such as negation, logical negation, and bitwise NOT.
'''
x = 5
y = -10
z = False

# Negative
print(-x)  # Output: -5

# Unchanged
print(+y)  # Output: -10

# Not
print(not z)  # Output: True

# Bitwise NOT
print(~x)  # Output: -6
'''
In-Depth Explanation:
- Negative (-): Negates the value of the operand. Here, -x with x = 5 results in -5.
- Positive (+): Returns the value of the operand unchanged. Here, +y with y = -10 results in -10.
- Logical NOT (not): Returns True if the operand is False and False if the operand is True. Here, not z with z = False results in True.
- Bitwise NOT (~): Inverts each bit of the operand. Here, ~x with x = 5 results in -6:
    5 in binary: 00000101
    Inverted: 11111010 (in two's complement, which represents -6)
'''