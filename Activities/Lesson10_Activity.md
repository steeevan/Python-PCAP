# README.md

## Overview

This README provides exercises and challenges on three core Python topics: Tuples, Dictionaries, and Functions. Each section includes information and prompts to help you practice and master these concepts.

## Table of Contents

1. [Tuples](#tuples)
2. [Dictionaries](#dictionaries)
3. [Functions](#functions)

---

## 1. Tuples

### Tuples Information
Tuples are immutable sequences in Python. Once created, their elements cannot be changed. Tuples are defined using parentheses `()` and can contain elements of different data types.

### Exercise 1.1: Defining Tuples
- Create a tuple containing three different data types.
- Print the tuple to the console.

### Exercise 1.2: Accessing Tuple Items
- Access and print the second item in the tuple you created.
- Try to modify the second item in the tuple and observe the result.

### Exercise 1.3: Tuple Methods
- Use the `count()` method to find the number of times a specific item appears in your tuple.
- Use the `index()` method to find the index of a specific item in your tuple.

### Exercise 1.4: Tuple Unpacking
- Create a tuple with three elements and unpack the elements into three variables.
- Print the variables to verify the unpacking.

---

## 2. Dictionaries

### Dictionaries Information
Dictionaries are collections of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are defined using curly braces `{}` and can be modified after creation.

### Exercise 2.1: Defining Dictionaries
- Create a dictionary with at least three key-value pairs.
- Print the dictionary to the console.

### Exercise 2.2: Accessing Dictionary Items
- Access and print the value associated with a specific key in your dictionary.
- Try to access a key that does not exist and handle the exception.

### Exercise 2.3: Modifying Dictionary Items
- Modify the value of an existing key in your dictionary.
- Print the modified dictionary to verify the change.

### Exercise 2.4: Adding Dictionary Items
- Add a new key-value pair to your dictionary.
- Print the dictionary to verify the addition.

### Exercise 2.5: Removing Dictionary Items
- Remove a key-value pair from your dictionary using the `del` keyword.
- Print the dictionary to verify the removal.
- Remove a key-value pair using the `pop()` method.
- Print the dictionary to verify the removal.

### Exercise 2.6: Iterating Dictionaries
- Iterate through the keys of your dictionary and print them.
- Iterate through the values of your dictionary and print them.
- Iterate through the key-value pairs of your dictionary and print them.

### Exercise 2.7: Checking Key Existence
- Check if a specific key exists in your dictionary and print a corresponding message.

### Exercise 2.8: Dictionary Comprehension
- Create a dictionary using dictionary comprehension that maps numbers from 1 to 5 to their squares.
- Print the resulting dictionary.

### Exercise 2.9: Filtering Dictionaries
- Filter the dictionary you created in Exercise 2.8 to include only items where the value is greater than 10.
- Print the filtered dictionary.

### Exercise 2.10: Copying Dictionaries
- Create a shallow copy of your dictionary using the `copy()` method.
- Modify the copied dictionary and print both the original and copied dictionaries to observe the difference.
- Create a deep copy of your dictionary using the `deepcopy()` method from the `copy` module.
- Modify the deep-copied dictionary and print both dictionaries to observe the difference.

### Exercise 2.11: Nested Dictionaries
- Create a nested dictionary to represent a simple menu with categories and items.
- Print the nested dictionary.

### Exercise 2.12: Dictionaries from Tuples
- Convert a list of tuples into a dictionary.
- Print the resulting dictionary.

### Exercise 2.13: Sparse Matrix
- Create a sparse matrix using a dictionary of tuple keys.
- Access and print specific elements of the sparse matrix.

### Exercise 2.14: Common Dictionary Methods
- Use the `clear()` method to remove all items from your dictionary.
- Use the `copy()` method to create a copy of your dictionary.
- Use the `fromkeys()` method to create a new dictionary with specified keys and values.
- Use the `get()` method to access a value for a specified key with a default value.
- Use the `items()` method to iterate over the key-value pairs of your dictionary.
- Use the `keys()` method to get all the keys of your dictionary.
- Use the `pop()` method to remove a specified key and return its value.
- Use the `popitem()` method to remove and return the last inserted key-value pair.
- Use the `setdefault()` method to get the value of a key if it exists, otherwise insert the key with a specified value.
- Use the `update()` method to update your dictionary with another dictionary or an iterable of key-value pairs.
- Use the `values()` method to get all the values of your dictionary.

### Exercise 2.15: Common Dictionary Functions
- Use the `len()` function to get the number of items in your dictionary.

---

## 3. Functions

### Functions Information
Functions are blocks of reusable code that perform a specific task. They are defined using the `def` keyword followed by the function name and parentheses. Functions can have parameters, return values, and can be called multiple times within a program.

### Exercise 3.1: Defining Functions
- Define a function that calculates the area of a rectangle given its length and width.
- Call the function with different sets of arguments and print the results.

### Exercise 3.2: Calling Functions
- Define a function that checks if a number is even.
- Call the function with different numbers and print the results.

### Exercise 3.3: Arbitrary Arguments
- Define a function that takes an arbitrary number of arguments and returns their sum.
- Call the function with different sets of arguments and print the results.

### Exercise 3.4: Unpacking Argument Lists
- Define a function that takes two arguments.
- Call the function using an unpacked list of arguments.

### Exercise 3.5: Keyword Arguments
- Define a function that takes two keyword arguments.
- Call the function using keyword arguments and print the results.

### Exercise 3.6: Arbitrary Keyword Arguments
- Define a function that takes an arbitrary number of keyword arguments and prints them.
- Call the function with different sets of keyword arguments.

### Exercise 3.7: Default Parameter Values
- Define a function with default parameter values.
- Call the function with and without providing arguments to see the default values in action.

### Exercise 3.8: Passing Mixed Arguments
- Define a function that takes positional-only, keyword-only, and mixed arguments.
- Call the function with different sets of arguments and print the results.

### Exercise 3.9: Pass Statement
- Define an empty function using the `pass` keyword.
- Call the function to verify it does nothing.

### Exercise 3.10: None Keyword and Returning None
- Define a function that prints a message but does not return a value.
- Call the function and print the returned value to verify it is `None`.

### Exercise 3.11: Function Recursion
- Define a recursive function to calculate the factorial of a number.
- Call the function with different numbers and print the results.

### Exercise 3.12: Name Scope and Global Keyword
- Define a function that modifies a global variable.
- Call the function and print the global variable to verify the change.

---

These exercises and challenges will help you practice and solidify your understanding of Tuples, Dictionaries, and Functions in Python. Happy coding!