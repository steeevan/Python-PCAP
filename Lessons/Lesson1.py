## Lesson Plan: Fundamental Building Blocks of Python Programming

### Lesson Objectives:
- Understand the basic concepts of Python programming
- Learn about various types of literals in Python
- Explore different operators and their usage in Python

---

### 1. Basic Concepts

#### 1.1. Logical and Physical Lines
- **Logical Line:** A logical line is a statement that the Python interpreter executes. In Python, a logical line can span multiple physical lines using explicit or implicit line joining.
- **Physical Line:** A physical line is what you see as a single line in your text editor.

**Example:**
```python
# Logical line spanning a single physical line
my_string = 'My entire string on a single physical line.'
print(my_string)
# Output: My entire string on a single physical line.
```

#### 1.2. Explicit Line Joining
- You can join two physical lines using a backslash `\`.

**Example:**
```python
# String literal spanning two physical lines
my_string = 'The first part of the string. \
The second part of the string'
print(my_string)
# Output: The first part of the string. The second part of the string

# Control flow spanning multiple physical lines
year = 2019
month = 9
day = 15
if 1900 < year < 2100 and 1 <= month <= 12 \
    and 1 <= day <= 31:    # Valid date
        print("You have entered a valid date")
# Output: You have entered a valid date
```

#### 1.3. Implicit Line Joining
- Parentheses `()`, brackets `[]`, and braces `{}` can be used to span multiple physical lines without using `\`.

**Example:**
```python
# Implicit line joining
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday',    # Weekdays
        'Saturday', 'Sunday')    # Weekend
print(days)
# Output: ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
```

#### 1.5. Multi-Logical Physical Lines
- You can write multiple logical lines in a single physical line by separating them with a semicolon `;`.

**Example:**
```python
# Multiple logical lines spanning a single physical line
from datetime import date; today = date.today(); print(today)
# Output: 2019-09-17
```

#### 1.7. Indentation
- Indentation is used to define the blocks of code. Incorrect indentation will result in an `IndentationError`.

**Example:**
```python
# Correct indentation
x = 101
if x >= 100:
    print("Your number is bigger than or equal to 100")
else:
    print("Your number is less than 100")
# Output: Your number is bigger than or equal to 100

# Incorrect indentation
x = 100
    y = 200    # Incorrect indentation
if x >= y:
print("X is bigger than or equal to Y")    # Incorrect indentation 
else:
    print("Y is bigger than X")
# Output: IndentationError: unexpected indent
```

#### 1.8. Identifiers
- Identifiers are the names given to variables, functions, etc. They must follow certain rules: 
  - They must start with a letter (a-z, A-Z) or an underscore (_).
  - They can be followed by letters, digits (0-9), or underscores.
  - They cannot be a keyword (reserved words in Python).

**Example:**
```python
# Valid identifiers
my_first_number = 100
my_first_string = 'Hello World'

# Invalid identifiers
1number = 10
string-test = 'Invalid Identifier'
# Output: SyntaxError: can't assign to operator
```

---

### 2. Literals

#### 2.1. String Literals
- String literals can be enclosed in single quotes, double quotes, or triple quotes.

**Example:**
```python
my_first_string = 'Hello World'
my_second_string = 'Line 1.\nLine 2.'
my_third_string = r'Line 1.\nLine 2.'  # Raw string literal
my_fourth_string = u'r\u00e9sum\u00e9'  # Unicode string literal

print(my_first_string)
print(my_second_string)
print(my_third_string)
print(my_fourth_string)
# Output: 
# Hello World
# Line 1.
# Line 2.
# Line 1.\nLine 2.
# résumé
```

#### 2.2. Boolean Literals
- Boolean literals are `True` and `False`.

**Example:**
```python
my_first_boolean = True
my_second_boolean = False

print(my_first_boolean)
print(my_second_boolean)
print(1 == True)   # True is equivalent to 1
print(1 == False)  # False is equivalent to 0
print(0 == True)
print(0 == False)
# Output: 
# True
# False
# True
# False
# False
# True
```

#### 2.3. Numeric Literals
- Python supports integer, floating-point, and imaginary literals.

**Examples:**

**2.3.1. Integer Literals**
```python
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
# Output: 
# 100
# 100
# 100
# 100
# 100000000
```

**2.3.2. Floating Point Literals**
```python
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
# Output:
# 3.14
# 1000.0
# 0.001
# 10.0
# 0.12345
# 3.141593
```

**2.3.3. Imaginary Literals**
```python
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
# Output:
# 10j
# 0.1j 0.0 0.1
# (2+3j) 2.0 3.0
```

#### 2.4. Special Literals
- Python has a special literal, `None`, which represents the absence of a value.

**Example:**
```python
x = None
print(x)
if x:
    print('x is True')
else:
    print('x is not True')
print(bool(None))
# Output:
# None
# x is not True
# False
```

---

### 3. Operators

#### 3.1. Arithmetic Operators
- Used to perform basic arithmetic operations.

**Example:**
```python
# Addition
print(13 + 7)

# Subtraction
print(10 - 7)

# Multiplication
print(64 * 8)

# Division
print(225 / 15)

# Modulus (remainder after division)
print(69 % 8)

# Exponentiation (raising by a power)
print(2 ** 5)

# Floor division (quotient)
print(100 // 7)
# Output:
# 20
# 3
# 512
# 15.0
# 5
# 32
# 14
```

#### 3.2. Assignment Operators
- Used to assign values to variables.

**Example:**
```python
# Assignment
x = 10
print(x)

# Add and assign (x = x + 5)
x += 5
print(x)

# Subtract and assign (x = x - 2)
x -= 2
print(x)

# Multiply and assign (x = x * 4)
x *= 4
print(x)

# Divide and assign (x = x / 2)
x /= 2
print(x)

# Modulus and assign (x = x % 4)
x %= 4
print(x)

# Exponentiation and assign (x = x ** 8)
x **= 8
print(x)

# Floor division and assign (x = x // 15)
x //= 15
print(x)

# Bitwise AND and assign (x = x & 18)
x = int(x)
x &= 18
print(x)

# Bitwise OR and assign (x = x | 10)
x |= 10
print(x)

# Bitwise XOR and assign (x = x ^ 2)
x ^= 2
print(x)

# Bitwise signed right shift and assign (x = x >> 1)
x >>= 1
print(x)

# Bitwise zero fill left shift and assign (

x = x << 2)
x <<= 2
print(x)
# Output:
# 10
# 15
# 13
# 52
# 26.0
# 2.0
# 256.0
# 17.0
# 16
# 26
# 24
# 12
# 48
```

#### 3.3. Comparison Operators
- Used to compare two values.

**Example:**
```python
# Equal
print(10 == 100)

# Not equal
print(2 != 5)

# Greater than
print(13 > 12)

# Less than
print(100 < 1_000_000)

# Greater than or equal to
print(15 >= 15)

# Less than or equal to
print(20 <= 19)
# Output:
# False
# True
# True
# True
# True
# False
```

#### 3.4. Logical Operators
- Used to combine conditional statements.

**Example:**
```python
# AND
print(1 < 100 and 10 < 100)

# OR
print(13 > 14 or 1 > 0)

# NOT
print(not(1 < 100 and 10 < 100))
# Output:
# True
# True
# False
```

#### 3.5. Identity Operators
- Used to compare the memory location of two objects.

**Example:**
```python
x = 10
y = 100.0

# IS
print(x is y)
print(x is x)

# IS NOT
print(x is not y)

x = y
print(x is y)
print(x is not y)
# Output:
# False
# True
# True
# True
# False
```

#### 3.6. Membership Operators
- Used to test if a sequence is presented in an object.

**Example:**
```python
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')

# IN
print('Thursday' in weekdays)
print('Saturday' in weekdays)

# NOT IN
print('Sunday' not in weekdays)
# Output:
# True
# False
# True
```

#### 3.7. Bitwise Operators
- Used to perform operations on binary numbers.

**Example:**
```python
# Bitwise AND
print(17 & 18)

# Bitwise OR
print(16 | 10)

# Bitwise XOR
print(26 ^ 2)

# Bitwise NOT
print(~4)

# Bitwise signed right shift
print(24 >> 2)

# Bitwise zero fill left shift
print(12 << 2)
# Output:
# 16
# 26
# 24
# -5
# 6
# 48
```

#### 3.8. Unary Operators
- Unary operators operate on a single operand.

**Example:**
```python
x = 5
y = -10
z = False

# Negative
print(-x)

# Unchanged
print(+y)

# Not
print(not z)

# Bitwise NOT
print(~x)
# Output:
# -5
# -10
# True
# -6
```

---

### Homework Explanation

Use the learned concepts to solve the following problems on pen and paper. Let's break down each problem to understand how to compute the result.

**Question 1:** `print(47 & 55)`
- **Explanation:** The `&` operator performs a bitwise AND operation. Convert 47 and 55 to binary and perform AND operation.
  - 47 in binary: `00101111`
  - 55 in binary: `00110111`
  - Result: `00100111` (which is 39 in decimal)
  
**Question 2:** `print(59 | 44)`
- **Explanation:** The `|` operator performs a bitwise OR operation. Convert 59 and 44 to binary and perform OR operation.
  - 59 in binary: `00111011`
  - 44 in binary: `00101100`
  - Result: `00111111` (which is 63 in decimal)

**Question 3:** `print(16 ^ 12)`
- **Explanation:** The `^` operator performs a bitwise XOR operation. Convert 16 and 12 to binary and perform XOR operation.
  - 16 in binary: `00010000`
  - 12 in binary: `00001100`
  - Result: `00011100` (which is 28 in decimal)

**Question 4:** `print(131 // 8)`
- **Explanation:** The `//` operator performs floor division. Divide 131 by 8 and take the floor of the result.
  - 131 divided by 8 is 16.375
  - Floor value: 16

**Question 5:** `print(0b1110101)`
- **Explanation:** The prefix `0b` denotes a binary literal. Convert the binary number `1110101` to decimal.
  - Binary `1110101` is 117 in decimal

**Question 6:** `print((2 + 2) ** (2 + 2))`
- **Explanation:** Compute the sum inside the parentheses first, then perform exponentiation.
  - `(2 + 2)` is 4
  - `4 ** 4` is 256

**Question 7:** `print(10 * 10 + 2 * (100 / 10))`
- **Explanation:** Compute the multiplication and division first, then addition.
  - `10 * 10` is 100
  - `100 / 10` is 10
  - `2 * 10` is 20
  - `100 + 20` is 120

**Question 8:** `print(11 & 13 * 2 ** 3)`
- **Explanation:** Compute exponentiation, multiplication, and then bitwise AND.
  - `2 ** 3` is 8
  - `13 * 8` is 104
  - `11 & 104` is 8 (bitwise AND of `00001011` and `01101000`)

**Question 9:** `print((1000 % 30 ^ 17 % 3 ** (1 + 1)) ** 8)`
- **Explanation:** Compute the modulus, exponentiation, then bitwise XOR, and finally exponentiation.
  - `1000 % 30` is 10
  - `3 ** (1 + 1)` is 9
  - `17 % 9` is 8
  - `10 ^ 8` is 2 (bitwise XOR of `00001010` and `00001000`)
  - `2 ** 8` is 256

**Question 10:** `print((~bool(None)) ** 2 << 4)`
- **Explanation:** Compute `bool(None)`, bitwise NOT, exponentiation, and bitwise left shift.
  - `bool(None)` is `False` (which is 0)
  - `~False` is `-1`
  - `(-1) ** 2` is 1
  - `1 << 4` is 16 (left shift by 4 places)

---

