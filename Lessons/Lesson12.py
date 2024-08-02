'''
15 Introduction to Object-oriented programming (OOP) in Python

In this section we will introduce the object oriented programming (OOP) paradigm
which means to model the world and our software applications as objects that 
interacts with each other. Supported by hand on examples in python

Keywords:
- Classes
- Class Attributes
- CLass Methods
- Inheritance
- Constructors
- Introspection

'''

'''
15.1 Imperative Programming
This represents a paradigm that uses statements to change a programs state. It focuses on describing
how a program operates
'''
# Example 15.1
# Write a simple program using imperative programming to caluclate the sum
sum = 0
my_number = [1,2,3,4,5]
for number in my_number:
    sum += number
print(f"THe sum of the numbers is {my_number} is: {sum}")

'''
15.2 Functional Programming
This is a paradigm that treats computations as the evaluation of mathematical functions and avoids
chaning the state and mutable data
'''

# import this module
from functools import reduce

def add(x,y):
    return x + y

sum = reduce(add,my_number)
print(sum)

sum = reduce(lambda x, y: x+y, my_number)
print(sum)

'''
15.3 Creating Objects
Objects are instances of classes. Classes define the stucture and behaviour of objects
'''
# importing the module Turtle
import turtle

#screen = turtle.Screen()
my_turtle = turtle.Turtle()

print(my_turtle)
'''
for i in range(4):
    my_turtle.forward(90)
    my_turtle.right(90)
'''
#turtle.mainloop()
#turtle.done()

'''
15.4 Accessing Attributes
Attributes are variables that belong to the object. They are access using
dot notation
'''
print(my_turtle.position)

import mypackages.module1 as mod1
# Creating an object using our own module
pet = mod1.Animal()
pet.set_animal("Dog")
print(pet.my_animal)

'''
15.5 Modify Attributes
Attribyutes can be modified using the dot notation 
(as long the varibale is public)

'''

pet.my_animal = "cat"
print(pet.get_animal())

'''
15.6 Deleting Attributes
Attributes can be deleted using the del keywork
'''
badpet = mod1.Animal()
badpet.set_animal("Scorpion")
print(pet.get_animal())
print(badpet.get_animal())

del badpet.my_animal
print(pet.get_animal())
print(badpet.my_animal)


