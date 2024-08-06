'''
13 Modules and Packages in Python
In this lesson we will explore the conept of modules in Python with 
a focus on essential modules such as 'os' and 'math' and those relevant
for the Python Associate Certificate.
'''

'''
13.1 Importing Modules
Modules in Python are files containing Python files. These files can define 
functions, classes, and variables. Modules also include runnable code.
The 'import' statement is used to include the functionality of one module
into another.


OS Module (Operating System)
THe 'os' module provides a way of using operating sytem dependent functionality
like reading or writing to the file system.
'''
import os

import mypackages.module1
import mypackages.module2

# Get te current working directoy
cwd = os.getcwd()
print(cwd)

# List directory Contents
contents = os.listdir(cwd)
print(contents)

# Create a new directory
# os.makedirs('new_directory')

# Remove the directory
# os.rmdir('new_directory')

'''
13.2 Importing Math Module
The 'math' module provides acces to mathematical functions define 
by the C standard
'''

# import the math module
import math

# Calculate the cosine of 90 degrees
print(int(math.cos(math.radians(90))))  # Output: 0.0

# Calculate the sine of 90 degrees
print(math.sin(math.radians(90)))  # Output: 1.0

# Calculate the tangent of 45 degrees
print(math.tan(math.radians(45)))  # Output: 1.0

# Get the value of pi
print(math.pi)  # Output: 3.141592653589793

'''
13.3 Pyton Associate Modules
For the Python Certificate , familiarity with several standard modules is
essential including 'os' , 'math', 'sys', and 'random'
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
Docstrings are string literals that appear riht after 
the definition of a function, method, class, or a module

'''
# Access math module docstrins
print(math.__doc__)

# Acces and display a functions docstring
print(math.sqrt.__doc__)

'''
13.5 help function
THe 'help()' function displays the documentation for a module, class,function
or method
'''
# Displays help on the math module
#help(math)

# Display help on a specific function
help(math.sqrt)

'''
13.6 PYC Files
Python automatically compiles your script to compiled code, so-called bytecode
before running it. THis compiled code is stored in '.pyc. files
'''
# Generate a byte code file of a module
import py_compile
# py_compile.compile('.py')

# Generate a byte code file of a module in a custom location
#py_compile.compile('my_module.py', cfile='/tmp/mymodule.pyc')

'''
14 Packages
A package is a way of structuring Pyton modules namespace by using 
the dotted module names. A package is a collection of moudles in directories
'''

'''
14.1 Creating and Importing Your own packages

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

# Create objects using the modules
pet = mypackages.module1.Animal()
pet.set_animal("Waffles")
print(pet.get_animal())

person = mypackages.module2.Human()
person.set_name("Jillis Quidas")
print(person.get_name())