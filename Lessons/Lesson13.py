'''
Continuation of 15
Object Oriented Programming (OOP)
- delete objects
- perfom introspection
- Dynamic modifactions to attributes
- invoke methods and understans the method resolution (MRO) in inheritance
- Use name mangling to create private variables

'''
import mypackages.car as vehicle
# 15.6
# Create a instance of the object Car


redbull = vehicle.Car(number_doors=0,
                 registration_number='RB 999',
                 make='Red Bull',
                 model='RB9',
                 year=500,
                 max_speed=210,
                 acceleration_rate=18,
                 deceleration_rate=6)

print(redbull)

# Delete this object

del redbull

try:
    print(redbull)
except NameError as e:
    print(e)

'''
15.7 Introspection
Accessing Objects attributes and introspection allows us to examine the attributes and methods of objects and classes
'''
# Assume mercedes is another car object
mercedez = vehicle.Car(number_doors=4,
                 registration_number='RB 443',
                 make='Mercedes',
                 model='AMG F1',
                 year=2024,
                 max_speed=300,
                 acceleration_rate=26,
                 deceleration_rate=72)

# Access an objects attribute references
print(mercedez.__dict__)

# Acces a class name
print(vehicle.__name__)

# Acces object claa name
print(mercedez.__class__.__name__)

'''
15.8 Adding attributes
You can add new attributes to an object at runtime using the setattr() function
'''
print(mercedez)
setattr(mercedez,"color","Red")
setattr(mercedez,"Tinted",True)
setattr(mercedez,"Turbo",True)


print(mercedez)
print(mercedez.__getattribute__("color"))
print(mercedez.__getattribute__("Tinted"))
print(mercedez.__getattribute__("Turbo"))

'''
15.9 Invoke methods
Methods of an object are invoked when called upon using the dot notation
'''

mercedez.accelerate()

'''
15.10 Inheritance
Understand super classes and sub classes attributes
'''
ferrari = vehicle.Car(number_doors=2,
                 registration_number='RB 442323',
                 make='Ferrari',
                 model='raptor',
                 year=2024,
                 max_speed=300,
                 acceleration_rate=26,
                 deceleration_rate=72)

print(ferrari.number_doors)

class myCar(vehicle.Car):
    def __init__(self, number_doors, registration_number, make, model, year, max_speed, acceleration_rate, deceleration_rate, numberedCar) -> None:
        super().__init__(number_doors, registration_number, make, model, year, max_speed, acceleration_rate, deceleration_rate)
        self.number_of_car = numberedCar
    
    def __str__(self) -> str:
        return super().__str__() + f"'number_of_car' : {self.number_of_car}"
    
    def turnOn(self):
        print("Vroom Vroom Car is on")


becky = myCar(number_doors=2,
                 registration_number='RB 0000',
                 make='HONDA',
                 model='CIVIC',
                 year=2024,
                 max_speed=1_000_000,
                 acceleration_rate=500,
                 deceleration_rate=0,
                 numberedCar=10)

print(becky)
becky.turnOn()

'''
15.11 Constructors
A constructor uses the __init__ method. THis is a special keywork in python
'''
class A:
    # Constructor
    def __init__(self) -> None:
        print("A class was made")
    def print_me(self):
        print("YAY you printed A  from the method")

a = A()
a.print_me()

class B:
    # default constructor

    def print_me(self):
        print("YAY you printed B from the method")

b = B()
b.print_me()

class C:
    def __init__(self) -> None:
        A.__init__(self)
        print("From C")
    
    def print_me(self):
        print("Yay you printed C from the method")

c = C()
c.print_me()

'''
Name Mangling
Name mangling is when you make an attribute private using the '__' before the variable name
'''


# define a class with private variables
class User:
    def __init__(self,fname,lname,email,dob,address) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.__dob = dob
        self.__address = address
    
    def display_dob(self):
        return self.__dob

    def display_address(self):
        print(self.__address)


barack_Obama = User("Barack","Obama","obama@gmail.com","08/04/1961","2569 pkwy Chino Hills")
s = barack_Obama.display_dob()
print(s)

'''
15.13 Common FUnction for Classes
'''

print(hasattr(barack_Obama,"Age"))
print(hasattr(barack_Obama,"fname"))

# type function
print(type(barack_Obama))
print(type([1,2]))