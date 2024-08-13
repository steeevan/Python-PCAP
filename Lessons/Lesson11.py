'''
13 Modules and Packages in Python
<<<<<<< HEAD
In this lesson we will explore the conept of modules in Python with 
a focus on essential modules such as 'os' and 'math' and those relevant
=======
In this lesson we will explore the concept of modules in Python
with a focus on essential modules such as 'os' and 'math' and those relevant
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
for the Python Associate Certificate.
'''

'''
13.1 Importing Modules
<<<<<<< HEAD
Modules in Python are files containing Python files. These files can define 
=======
Modules in Python are files containing Python files. These files can define
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
functions, classes, and variables. Modules also include runnable code.
The 'import' statement is used to include the functionality of one module
into another.


OS Module (Operating System)
<<<<<<< HEAD
THe 'os' module provides a way of using operating sytem dependent functionality
=======
The 'os' module provides a way of using operating system dependent functionality
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
like reading or writing to the file system.
'''
import os

import mypackages.module1
import mypackages.module2

<<<<<<< HEAD
# Get te current working directoy
=======
# Get the current working directory
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
cwd = os.getcwd()
print(cwd)

# List directory Contents
contents = os.listdir(cwd)
print(contents)

# Create a new directory
<<<<<<< HEAD
# os.makedirs('new_directory')

# Remove the directory
# os.rmdir('new_directory')

'''
13.2 Importing Math Module
The 'math' module provides acces to mathematical functions define 
=======
#os.makedirs('new_directory')

# Remove the directory
#os.rmdir('new_directory')

'''
13.2 Import Math Module
The 'math' module provides access to mathematical functions defined
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
by the C standard
'''

# import the math module
import math
<<<<<<< HEAD

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
=======
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
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
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
<<<<<<< HEAD
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
=======
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
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

# Generate a byte code file of a module in a custom location
#py_compile.compile('my_module.py', cfile='/tmp/mymodule.pyc')

'''
14 Packages
<<<<<<< HEAD
A package is a way of structuring Pyton modules namespace by using 
the dotted module names. A package is a collection of moudles in directories
'''

'''
14.1 Creating and Importing Your own packages
=======
A package is a way of structuring Python modules namespace by using
the dotted module names. A package is a collection of modules in directories
'''

'''
14.1 Creating and Importing your own packages
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

Create a directory structure
mypackage/
    __init__.py
    module1.py
    module2.py
<<<<<<< HEAD

=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''

import mypackages

<<<<<<< HEAD

=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
# Import a module from a package
import mypackages.module1 as mod1
pet2 = mod1.Animal()

<<<<<<< HEAD
# Create objects using the modules
=======
#print(dir(mypackages))
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
pet = mypackages.module1.Animal()
pet.set_animal("Waffles")
print(pet.get_animal())

person = mypackages.module2.Human()
person.set_name("Jillis Quidas")
print(person.get_name())