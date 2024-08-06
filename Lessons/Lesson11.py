'''
13 Modules and Packages in Python
In this lesson we will explore the concept of modules in Python
with a focus on essential modules such as 'os' and 'math' and those relevant
for the Python Associate Certificate.
'''

'''
13.1 Importing Modules
Modules in Python are files containing Python files. These files can define
functions, classes, and variables. Modules also include runnable code.
The 'import' statement is used to include the functionality of one module
into another.


OS Module (Operating System)
The 'os' module provides a way of using operating system dependent functionality
like reading or writing to the file system.
'''
import os

import mypackages.module1
import mypackages.module2

# Get the current working directory
cwd = os.getcwd()
print(cwd)

# List directory Contents
contents = os.listdir(cwd)
print(contents)

# Create a new directory
#os.makedirs('new_directory')

# Remove the directory
#os.rmdir('new_directory')

'''
13.2 Import Math Module
The 'math' module provides access to mathematical functions defined
by the C standard
'''

# import the math module
import math
# calculate the cosine of 90 degrees

# Calculate the cosine of 90 degrees
print(math.cos(math.radians(90))) # Output: 0.0

# Calculate the sine of 90 degrees
print(math.sin(math.radians(90))) # Output: 1.0

# Calculate the tangent of 45 degrees
print(math.tan(math.radians(45))) # Output: 1.0

# Get the value of pi
print(math.pi) # Output: 3.141592653589793

'''
13.3 Python Associate Modules
For the Python Certificate, familiarity with several standard modules is
essential including 'os', 'math', 'sys', and 'random'
'''

# Import the sys module
import sys

# Get the list of command line arguments
print(sys.argv)

# Get the Python version
print(sys.version)

# Examine the sys.path
print(sys.path)

'''
13.4 Module Documentation
Docstrings are string literals that appear right after 
the definition of a function, ethod, class or a module
'''
# Access math module docstrings
print(math.__doc__)

# Access and display a function's docstring
print(math.sqrt.__doc__)

'''
13.5 Help Function
The 'help()' function displays the documentation for a module, class, function
or method
'''
# Diplays help on the math module
#help(math)

# Display help on a specific function
#help(math.sqrt)

'''
13.6 PYC Files
Python automatically compiles your script to compiled code, so-called bytebode
before running it. This compiled code is stored in '.pyc. files
'''
# Generate a byte code file of a module
import py_compile
#py_compile.compile('Lesson10.py')

# Generate a byte code file of a module in a custom location
#py_compile.compile('my_module.py', cfile='/tmp/mymodule.pyc')

'''
14 Packages
A package is a way of structuring Python modules namespace by using
the dotted module names. A package is a collection of modules in directories
'''

'''
14.1 Creating and Importing your own packages

Create a directory structure
mypackage/
    __init__.py
    module1.py
    module2.py
'''

import mypackages

# Import a module from a package
import mypackages.module1 as mod1
pet2 = mod1.Animal()

#print(dir(mypackages))
pet = mypackages.module1.Animal()
pet.set_animal("Waffles")
print(pet.get_animal())

person = mypackages.module2.Human()
person.set_name("Jillis Quidas")
print(person.get_name())