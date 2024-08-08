'''
Continuation of 15
Object Oriented Programming (OOP)
- delete objects
- perfom introspection
- Dynamic modifactions to attributes
- invoke methods and understans the method resolution (MRO) in inheritance
- Use name mangling to create private variables

'''

'''
Create a Car objects thats defined in your package 'mypackages'

'''
import mypackages.car as vehicle
# 15.6
# Created a object
redbull = vehicle.Car(number_doors=0,
                 registration_number='RB 999',
                 make='Red Bull',
                 model='RB9',
                 year=2013,
                 max_speed=210,
                 acceleration_rate=18,
                 deceleration_rate=60)


print(redbull)

# Delete objects

del redbull

# try to print the deleted object
try:
    print(redbull)
except NameError as e:
    print(e)


'''
15.7 Introspection
Acessing Objet attributes and introspection allows us to examine the attributes and methods of
 objects and classes

'''
# Assume mercedez is another car Object
mercedez = vehicle.Car(number_doors=4,
                 registration_number='RB 443',
                 make='Mercedes',
                 model='AMG F1',
                 year=2024,
                 max_speed=300,
                 acceleration_rate=26,
                 deceleration_rate=72)


# Access an objects attribbute references
print(mercedez.__dict__)

# Access a class name
print(vehicle.__name__)

# Acces an objects class name
print(mercedez.__class__.__name__)

print(mercedez.__module__)

print(vehicle.__builtins__)
print(mercedez.__class__.__bases__)


'''
15.8 Adding Attributes
You can add new attributes to an object at runtime using the setattr() function
'''

print(mercedez)
setattr(mercedez,"color","Red")
setattr(mercedez,"Tinted?",True)
setattr(mercedez,"Turbo?",True)

print(mercedez.__getattribute__("color"))
print(mercedez.__getattribute__("Tinted?"))
print(mercedez.__getattribute__("Turbo?"))

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
    def __init__(self, number_doors, registration_number, make, model, year, max_speed, acceleration_rate, deceleration_rate,numberedCar) -> None:
        super().__init__(number_doors, registration_number, make, model, year, max_speed, acceleration_rate, deceleration_rate)
        self.numbered_car = numberedCar
    def __str__(self):
        return f"Car{{'number_doors': {self.number_doors}, 'registration_number': '{self.registration_number}', 'make': '{self.make}', 'model': '{self.model}', 'year_manufactured': {self.year}, 'maximum_speed': {self.max_speed}, 'acceleration_rate': {self.acceleration_rate}, 'deceleration_rate': {self.deceleration_rate}, 'mileage_miles': {self.mileage_miles}, 'speed_mph': {self.speed_mph}, '# of car': {self.numbered_car}}}" 

    def turnON(self):
        print("vroom vroom car is on")

honda = myCar(number_doors=2,
                 registration_number='RB 0000',
                 make='HONDA',
                 model='CIVIC',
                 year=2024,
                 max_speed=1_000_000,
                 acceleration_rate=500,
                 deceleration_rate=0,numberedCar=10)

print(honda)
honda.turnON()

'''
15.11 Constructors
a Constructor uses the __init__ to construct the class. THis is a special keyword in python
'''

class A:
    # the constructor
    def __init__(self) -> None:
        print('A was made')
    
    def print_me(self):
        print("YAY you printed me from the method")


a = A()

# default constructors
class B:
    def print_me(self):
        print("You made B without the constructor")

b = B()
b.print_me()

# Define a class with a constructor that explicitly invokes nother class constructor
class C:
    def __init__(self) -> None:
        A.__init__(self)

    def print_me(self):
        print("C printed from method")

# create the new object
c = C()
c.print_me()


'''
15.12 Name Mangling
Name mangling is when you make an attribute private using the '__' before the variable name
'''
# Define a class with private variables
class User:
    def __init__(self,fname,lname, email,dob,address) -> None:
        self.fname = fname
        self.lname = lname
        self.email = email
        self.__dob = dob
        self.__address = address
    
    def display_dob(self):
        return self.__dob
    
    def display_address(self):
        print(self.__address)

barack_obama_user = User("Barack","Obama","obamabarack@gmail.com","08/04/1961","2569 Chino Hills Pkwy")
print(barack_obama_user.fname)
s = barack_obama_user.display_dob()
print(s)

'''
15.13 Common FUnction for Classes
'''

print(hasattr(barack_obama_user,"Age"))
print(hasattr(barack_obama_user,"fname"))

# type function
print(type(barack_obama_user))
print(type([1,2]))