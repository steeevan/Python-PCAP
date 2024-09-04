Here are some practice problems for each of the topics in exam block #5 of the PCAP:

1. List Comprehension:
Problem: Write a list comprehension that takes a list of integers and creates a new list containing only the squares of even numbers.

Example Input:


numbers = [1, 2, 3, 4, 5, 6]
Example Output:


[4, 16, 36]
2. Lambda:
Problem: Use a lambda function inside the sorted() function to sort a list of dictionaries by the value of a specific key.

Example Input:


students = [{'name': 'Alice', 'age': 24}, {'name': 'Bob', 'age': 19}, {'name': 'Charlie', 'age': 22}]
Example Output:


[{'name': 'Bob', 'age': 19}, {'name': 'Charlie', 'age': 22}, {'name': 'Alice', 'age': 24}]
3. Closures:
Problem: Create a closure that keeps track of how many times a function has been called.

Example Input:

counter_function = call_counter()
counter_function()
counter_function()
counter_function()
Example Output:


1
2
3
4. I/O Operations:
Problem: Write a program that reads a text file, counts the number of lines that contain a specific word, and prints the result.

Example Input:


# content of 'textfile.txt'
# This is a test.
# Testing is essential.
# Tests are important for learning.

word_to_search = "test"
Example Output:


2
5. Open/Read:
Problem: Write a program that opens a file called data.txt, reads its contents, and prints each line with its line number.

Example Input:


# content of 'data.txt'
# First line.
# Second line.
# Third line.
Example Output:


1: First line.
2: Second line.
3: Third line.
