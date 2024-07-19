# PCAP Certification Practice - Homework

This homework is designed to help you practice various Python programming concepts that are essential for the PCAP (Python Certified Associate Programmer) Certification. The topics covered include functions and methods, input and output, formatting, conditional statements, and basic lists.

## Homework Topics

### 1. Functions and Methods
- **Explanation**: 
  - **Functions** are blocks of code that perform a specific task and can be called using their name. They are defined using the `def` keyword.
  - **Methods** are functions that are associated with an object and are called using the dot notation on that object.

#### Exercise
1. Define a function named `calculate_area` that takes the radius of a circle as an argument and returns the area of the circle. Use this function to calculate and print the area of a circle with a radius of 5.
2. Create a list of numbers and use the `sort` method to sort the list in descending order. Explain how this method is different from a standalone sorting function.

### 2. Input and Output
- **Explanation**:
  - **input()**: Function to get user input.
  - **print()**: Function to print output to the console.
  - **int()**: Function to convert a value to an integer.
  - **float()**: Function to convert a value to a floating-point number.
  - **str()**: Function to convert a value to a string.

#### Exercise
1. Write a program that asks the user for their name and three test scores. Calculate the average score and print a message saying "Hello, [name]. Your average test score is [average]."
2. Modify the program to handle invalid inputs, such as non-numeric values for the test scores, by using try-except blocks.

### 3. Formatting
- **Explanation**:
  - **Formatted String Literals** (f-strings): Allows you to include expressions inside string literals, using `{}`.
  - **String Formatting**: Using the `format()` method or `%` operator to format strings.

#### Exercise
1. Write a program that takes a user's name and salary as input, and prints a message using an f-string that says "Hello, [name]. Your salary is $[salary:,.2f]."
2. Modify the program to format the output using the `format()` method, ensuring the salary is formatted with commas as thousands separators and two decimal places.

### 4. Conditional Statements
- **Explanation**:
  - **if**: Executes a block of code if a condition is true.
  - **if-else**: Executes one block of code if a condition is true, otherwise executes another block of code.
  - **if-elif-else**: Checks multiple conditions, executing the corresponding block of code for the first true condition.
  - **pass**: A null statement that is used as a placeholder.

#### Exercise
1. Write a program that asks the user for a number and prints whether the number is positive, negative, or zero. Additionally, print whether the number is a prime number.
2. Modify the program to include additional checks to determine if the number is a palindrome.

### 5. Basic Lists
- **Explanation**:
  - **Constructing Lists**: Creating a list using square brackets `[]`.
  - **Accessing Lists**: Using indices to access elements in a list.
  - **Manipulating Lists**: Adding, removing, and modifying elements in a list.

#### Exercise
1. Create a list of your five favorite movies. Add a new movie to the list at the second position, and remove the fourth movie from the list. Print the updated list.
2. Write a program that takes a list of numbers and removes all even numbers from the list. Print the updated list.

## New Problems and Exercises

### 6. Slicing a List
Extract a sublist from the predefined list `favorite_movies` that includes the second, third, and fourth movies.

- **Explanation**: Use slicing to extract a sublist. The syntax for slicing is `list[start:end]`, where `start` is the index to start from (inclusive), and `end` is the index to stop at (exclusive).

#### Exercise
1. Extract a sublist from the predefined list `favorite_movies` that includes the second, third, and fourth movies. Then, reverse the sublist and print it.

### 7. Using `insert()`
Insert a new movie at the second position of your list of favorite movies and print the updated list.

#### Exercise
1. Insert a new movie at the second position of your list of favorite movies and print the updated list. Then, insert another movie at the end of the list without using the `append` method.

### 8. Using `pop()`
Remove the third movie from your list using the `pop()` method and print the updated list.

#### Exercise
1. Remove the third movie from your list using the `pop()` method and print the updated list. Then, use the `pop()` method to remove and print the last element of the list.

### 9. Using `count()`
Count how many times a specific movie appears in your list of favorite movies.

#### Exercise
1. Count how many times a specific movie appears in your list of favorite movies. Then, create a new list where each movie appears multiple times and count the occurrences of each movie.

### 10. Using `sort()`
Sort your combined list of movies and books in alphabetical order and print the sorted list.

#### Exercise
1. Sort your combined list of movies and books in alphabetical order and print the sorted list. Then, sort the list in reverse alphabetical order and print it.

### 11. Using `reverse()`
Reverse the order of your combined list of movies and books and print the reversed list.

#### Exercise
1. Reverse the order of your combined list of movies and books and print the reversed list. Then, reverse the order of a sublist (the first three elements) and print the updated combined list.

Good luck with your homework! These exercises will help reinforce your understanding of fundamental Python concepts that are crucial for the PCAP Certification. Happy coding!
