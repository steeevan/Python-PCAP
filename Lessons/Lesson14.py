'''
16 I/O Basics and Exception Handling
By the end of this lesson, students will be able to:

- Understand the basics of input and output (I/O) in Python.
- Open, read, and write to files.
- ifferentiate between binary and text files.
- Use bytearray objects and their associated methods.
- Understand and implement exception handling using try-except-else-finally blocks.
- Recognize predefined exceptions and their hierarchies.
- Use assertions and understand the anatomy of an exception object.
'''
'''
16.1 Opening Files
Files are opened using the 'open()' function. This function returns a file object, which provides
methods and attributes to interact with file content
'''
# Open a file to read
file = open('Example1.txt','r')

