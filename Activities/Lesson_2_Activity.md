# Python Operators Challenge

A series of challenges and activities designed to help you understand and practice various Python operators.

## Table of Contents

- [Challenges/Activities](#challengesactivities)
  - [Basic Arithmetic Challenge](#basic-arithmetic-challenge)
  - [Assignment Operator Challenge](#assignment-operator-challenge)
  - [Comparison Operator Activity](#comparison-operator-activity)
  - [Logical Operator Puzzle](#logical-operator-puzzle)
  - [Identity and Membership Challenge](#identity-and-membership-challenge)
  - [Bitwise Operator Exercise](#bitwise-operator-exercise)
  - [Unary Operator Task](#unary-operator-task)
- [Homework](#homework)

## Challenges/Activities

### Basic Arithmetic Challenge

1. Write a program to calculate the area of a rectangle given its width and height.
2. Calculate the circumference of a circle given its radius.

### Assignment Operator Challenge

Create a program that updates a variable using different assignment operators and prints the result after each operation.

### Comparison Operator Activity

Write a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.

### Logical Operator Puzzle

Create a program that checks if a number is both positive and even using logical operators.

### Identity and Membership Challenge

Write a program to check if a given element is present in a list and whether it refers to the same object in memory.

### Bitwise Operator Exercise

Implement a program to perform bitwise operations on two numbers and display the results.

### Unary Operator Task

Create a program that demonstrates the use of unary operators on a variable and prints the results.

## Homework

Solve the following problems using the learned operators and write down the steps to understand the process.

### Question 1: `print(47 & 55)`

**Explanation:** The `&` operator performs a bitwise AND operation. Convert 47 and 55 to binary and perform AND operation.
- 47 in binary: `00101111`
- 55 in binary: `00110111`
- Result: `00100111` (which is 39 in decimal)

### Question 2: `print(59 | 44)`

**Explanation:** The `|` operator performs a bitwise OR operation. Convert 59 and 44 to binary and perform OR operation.
- 59 in binary: `00111011`
- 44 in binary: `00101100`
- Result: `00111111` (which is 63 in decimal)

### Question 3: `print(16 ^ 12)`

**Explanation:** The `^` operator performs a bitwise XOR operation. Convert 16 and 12 to binary and perform XOR operation.
- 16 in binary: `00010000`
- 12 in binary: `00001100`
- Result: `00011100` (which is 28 in decimal)

### Question 4: `print(131 // 8)`

**Explanation:** The `//` operator performs floor division. Divide 131 by 8 and take the floor of the result.
- 131 divided by 8 is 16.375
- Floor value: 16

### Question 5: `print(0b1110101)`

**Explanation:** The prefix `0b` denotes a binary literal. Convert the binary number `1110101` to decimal.
- Binary `1110101` is 117 in decimal

### Question 6: `print((2 + 2) ** (2 + 2))`

**Explanation:** Compute the sum inside the parentheses first, then perform exponentiation.
- `(2 + 2)` is 4
- `4 ** 4` is 256

### Question 7: `print(10 * 10 + 2 * (100 / 10))`

**Explanation:** Compute the multiplication and division first, then addition.
- `10 * 10` is 100
- `100 / 10` is 10
- `2 * 10` is 20
- `100 + 20` is 120

### Question 8: `print(11 & 13 * 2 ** 3)`

**Explanation:** Compute exponentiation, multiplication, and then bitwise AND.
- `2 ** 3` is 8
- `13 * 8` is 104
- `11 & 104` is 8 (bitwise AND of `00001011` and `01101000`)

### Question 9: `print((1000 % 30 ^ 17 % 3 ** (1 + 1)) ** 8)`

**Explanation:** Compute the modulus, exponentiation, then bitwise XOR, and finally exponentiation.
- `1000 % 30` is 10
- `3 ** (1 + 1)` is 9
- `17 % 9` is 8
- `10 ^ 8` is 2 (bitwise XOR of `00001010` and `00001000`)
- `2 ** 8` is 256

### Question 10: `print((~bool(None)) ** 2 << 4)`

**Explanation:** Compute `bool(None)`, bitwise NOT, exponentiation, and bitwise left shift.
- `bool(None)` is False (which is 0)
- `~False` is -1
- `(-1) ** 2` is 1
- `1 << 4` is 16 (left shift by 4 places)
