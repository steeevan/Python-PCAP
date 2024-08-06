## Lesson Plan: Functions in Python

### Objectives
'''By the end of this lesson, students will be able to:
- Understand what functions are and why they are used.
- Define and call functions in Python.
- Use parameters and return values.
- Differentiate between built-in and user-defined functions.
- Apply functions to solve problems.

### Lesson Duration
2 hours

### Materials Needed
- Computer with Python installed (or access to an online Python compiler)
- Projector and screen (for teacher demonstrations)
- Printed or digital handouts (optional)

---

### Introduction (15 minutes)

1. What is a Function?
   - Explain that a function is a block of organized, reusable code that performs a single action.
   - Functions help break programs into smaller, manageable, and modular chunks.
   - Use the analogy of a function being like a recipe or a mathematical function.

2. Why Use Functions?
   - Reusability: Write once, use multiple times.
   - Organization: Makes code easier to read and maintain.
   - Abstraction: Hide complex code details and expose simple interfaces.

### Basic Function Syntax (20 minutes)

1. Defining a Function
   - Syntax: 
     ```python
     def function_name(parameters):
         """
         Docstring (optional)
         """
         # Function body
         return value (optional)
     ```

2. Example: A Simple Function
   - Define a function that prints a greeting message:
     ```python
     def greet():
         """
         This function prints a greeting message.
         """
         print("Hello, welcome to the Python lesson!")
     ```
   - Calling the function:
     ```python
     greet()  # Output: Hello, welcome to the Python lesson!
     ```

3. Activity: Define and Call a Function
   - Have students define a function that prints their favorite quote or saying and then call the function.

### Functions with Parameters (25 minutes)

1. Adding Parameters to Functions
   - Explain that parameters allow functions to accept input values.
   - Syntax:
     ```python
     def function_name(parameter1, parameter2):
         # Function body
         return value
     ```

2. Example: Function with Parameters
   - Define a function that calculates the area of a rectangle:
     ```python
     def calculate_area(width, height):
         """
         This function calculates the area of a rectangle.
         """
         area = width  height
         return area
     ```
   - Calling the function:
     ```python
     result = calculate_area(5, 10)
     print(result)  # Output: 50
     ```

3. Activity: Create Functions with Parameters
   - Have students create a function that takes two numbers as parameters and returns their sum.
   - Example:
     ```python
     def add_numbers(a, b):
         return a + b
     
     sum_result = add_numbers(3, 7)
     print(sum_result)  # Output: 10
     ```

### Functions with Return Values (20 minutes)

1. Returning Values from Functions
   - Explain that functions can return values using the `return` statement.
   - Emphasize the difference between printing and returning values.

2. Example: Function with Return Value
   - Define a function that converts Fahrenheit to Celsius:
     ```python
     def fahrenheit_to_celsius(fahrenheit):
         """
         This function converts Fahrenheit to Celsius.
         """
         celsius = (fahrenheit - 32)  5 / 9
         return celsius
     ```
   - Calling the function:
     ```python
     temp_in_celsius = fahrenheit_to_celsius(98)
     print(temp_in_celsius)  # Output: 36.666666666666664
     ```

3. Activity: Functions with Return Values
   - Have students create a function that calculates the circumference of a circle given its radius.
   - Example:
     ```python
     def calculate_circumference(radius):
         return 2  3.14159  radius
     
     circumference = calculate_circumference(5)
     print(circumference)  # Output: 31.4159
     ```

### Built-in vs. User-defined Functions (10 minutes)

1. Built-in Functions
   - Discuss common built-in functions like `print()`, `len()`, `type()`, etc.
   - Show examples and how they are used.

2. User-defined Functions
   - Emphasize the importance of creating custom functions to solve specific problems.
   - Reinforce the syntax and structure of defining functions.

### Student Challenge (30 minutes)

1. Challenge Problem
   - Create a program that calculates the Body Mass Index (BMI).
   - Function to calculate BMI:
     ```python
     def calculate_bmi(weight, height):
         """
         This function calculates BMI.
         """
         bmi = weight / (height  2)
         return bmi
     ```

2. Additional Challenge
   - Create a function that takes a list of numbers and returns the average.

### Review and Q&A (10 minutes)

1. Review Key Concepts
   - Functions, parameters, return values, built-in vs. user-defined functions.

2. Q&A Session
   - Address any questions or concerns students may have.

Sure! Here are some medium and hard exercises for students to practice their understanding of functions in Python.

---

### Medium Exercises

1. **Palindrome Checker**
   - Write a function `is_palindrome(s)` that takes a string `s` and returns `True` if the string is a palindrome (reads the same forwards and backwards) and `False` otherwise.
     ```python
     def is_palindrome(s):
         s = s.replace(" ", "").lower()
         return s == s[::-1]
     
     print(is_palindrome("A man a plan a canal Panama"))  # Output: True
     print(is_palindrome("Hello"))  # Output: False
     ```

2. **Factorial Calculation**
   - Write a function `factorial(n)` that takes an integer `n` and returns the factorial of `n` (n!).
     ```python
     def factorial(n):
         if n == 0 or n == 1:
             return 1
         else:
             return n * factorial(n - 1)
     
     print(factorial(5))  # Output: 120
     print(factorial(0))  # Output: 1
     ```

3. **Fibonacci Sequence**
   - Write a function `fibonacci(n)` that takes an integer `n` and returns the nth number in the Fibonacci sequence.
     ```python
     def fibonacci(n):
         if n <= 0:
             return "Input should be a positive integer."
         elif n == 1:
             return 0
         elif n == 2:
             return 1
         else:
             return fibonacci(n - 1) + fibonacci(n - 2)
     
     print(fibonacci(7))  # Output: 8
     print(fibonacci(10))  # Output: 34
     ```

### Hard Exercises

1. **Prime Number Generator**
   - Write a function `generate_primes(n)` that takes an integer `n` and returns a list of the first `n` prime numbers.
     ```python
     def is_prime(num):
         if num <= 1:
             return False
         for i in range(2, int(num**0.5) + 1):
             if num % i == 0:
                 return False
         return True
     
     def generate_primes(n):
         primes = []
         num = 2
         while len(primes) < n:
             if is_prime(num):
                 primes.append(num)
             num += 1
         return primes
     
     print(generate_primes(10))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
     ```

2. **Anagram Finder**
   - Write a function `find_anagrams(word, candidates)` that takes a string `word` and a list of strings `candidates`. The function should return a list of candidates that are anagrams of the given word.
     ```python
     def find_anagrams(word, candidates):
         sorted_word = sorted(word)
         anagrams = []
         for candidate in candidates:
             if sorted(candidate) == sorted_word:
                 anagrams.append(candidate)
         return anagrams
     
     print(find_anagrams("listen", ["enlist", "google", "inlets", "banana"]))  # Output: ['enlist', 'inlets']
     ```

3. **Sudoku Validator**
   - Write a function `is_valid_sudoku(board)` that takes a 9x9 2D list representing a Sudoku board and returns `True` if the board is valid according to Sudoku rules, and `False` otherwise.
     ```python'''
     def is_valid_sudoku(board):
         def is_valid_unit(unit):
             unit = [i for i in unit if i != '.']
             return len(unit) == len(set(unit))
         
         for row in board:
             if not is_valid_unit(row):
                 return False
         
         for col in zip(*board):
             if not is_valid_unit(col):
                 return False
         
         for i in range(0, 9, 3):
             for j in range(0, 9, 3):
                 square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                 if not is_valid_unit(square):
                     return False
         
         return True
     
     sudoku_board = [
         ["5", "3", ".", ".", "7", ".", ".", ".", "."],
         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."],
         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."],
         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]
     ]
     
     print(is_valid_sudoku(sudoku_board))  # Output: True


