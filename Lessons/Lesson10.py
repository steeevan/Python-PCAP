'''
12 Function, generateor function, and lamba function in python
'''
'''
12.1 definingh functions
functions are defined using the 'def' keyword follow by the name of the fuynction and parantheses.
methods are more specific
'''
#example 12.1
# A simple example of a user defined function
def product(number1,number2):
    return number1*number2
#call the function(invoke)
a=12
b=10
c=product(a,b)
'''
12.2 Aribitraty 
function can acceot an arbitary number of arguments using the '*args'  keywords(syntax)
'''
#define a function to expect an aribitrary number of arguements
def product(*nums):
    x=1
    for num in nums:
        x*=num
    return x
# call the function with a tuple as argument
print(product(10,5,10,2))
#unpack the arguments lists
def is_prime(num):
    if num<=1 or num%1>0:
        return False
    for i in range(2,num//2):
        if num%i==0:
            return False
    return True
def findPrimebetween(start_num,end_num):
    return[num for num in range(start_num,end_num) if is_prime(num)]
args=[1,100]
print(findPrimebetween(*args))
# use keywords arguments
print(findPrimebetween(start_num=100,end_num=200))
'''
12.3 Arbitrart keyword arguments

'''
def concanate_words(**words):
    return ' '.join(words.values())
print(concanate_words(word1="wonderful",word2="world",word3="of",word4="python"))# with the values
'''
12.4 pass statement
the 'pass' statement is used as a placeholder for future code, allowing the creation of empty functions
'''
#ex 12.4
def my_empty_function():
    pass
'''
12.5
'''
# define a function that does not return a value
def my_logging_function(message):
    print(message)
log =my_logging_function("Hello I am")
print(type(log))
print(log)
'''
12.6 function recursion
recursion occurs when a function calls itself
'''
# calculate the nth element in the fiboncci sequence
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))
'''
12.7 local scope variables
variables are defined inside a function and are onlu accessible within the function
'''
measurements=15.5
def calculate_weight(height, age):
# global give access for the variable in side the function
    total_weight= height*age
    print(total_weight)
    print(measurements)
'''
12.8 generator functions 
generator function use the 'yield' keyword to return a value and suspend their exection, 
allowing them to be resumed
'''
#ex 12.8 
def infinite_sequence_generator():
    counter=0
    while True:
        yield counter
        counter+=1
# call this generator function and lazily evaluate the next element in the iterable object
infinite_gen=infinite_sequence_generator()
print(next(infinite_gen))
print(next(infinite_gen))
print(next(infinite_gen))
for i in range(1,10):
    print(next(infinite_gen))
'''
12.9 generator termination
generators raise a 'stopiteration' exception when ther are no further elements to generate
'''
#define a generator to lazily return ordered sequence of letters
def letter_seq_gen(start,stop,step=1):
    for ord_unicode in range(ord(start.lower()), ord(stop.lower()),step):
        yield chr(ord_unicode)
alphabet=letter_seq_gen('a','e')
print(next(alphabet))
print(next(alphabet))
print(next(alphabet))
print(next(alphabet))

alphabet=letter_seq_gen('a','{')
for letter in alphabet:
    print(letter,end='')
'''
12.10 generator expressions
generator expressions are similar to list comprehension but use parane
'''
print()
#ex12.10
first_million=(num for num in range(1,1000))
print(first_million)
print(next(first_million))
print(next(first_million))
print(next(first_million))
# ex 12.10.2
#create a lazily ecaluated generator object
alphabet=letter_seq_gen("a","z")
#convert the generator object into a list
alphabet_list=list(alphabet)
print(alphabet_list)
'''
12.11 lambda functions
lambda function are anonynous functions defined using the 'lambda' keyword. they can have any number of parameters but
only one expression
'''
#ex 12.11.1
#create a simple lambda function to square a given number
square= lambda n:n*n
#call this function
print(square(5))
# ex 12.11.2
#create a simple lambda function with three arguments
volume = lambda x,y,z:x*y*z
#call this lambda function
print(volume(3,10,5))


#activity 1.1
my_tuple = (42, "Hello, World!", 3.14)
print(my_tuple)

#activity 1.2
print(my_tuple[1])
#activity 1.3
print(my_tuple.count(42))

print(my_tuple.index(42))
#Exercise 1.4: Tuple Unpacking
num, name, value = my_tuple

# Printing the unpacked variables
print("num:", num)
print("name:", name)
print("value:", value)
#2.1
my_dictionary = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

print(my_dictionary)
# 2.2
print("Name:", my_dictionary["name"])

# Attempting to access a key that does not exist and handling the exception
key_to_access = "country"

try:
    value = my_dictionary[key_to_access]
    print(f"The value associated with the key '{key_to_access}' is: {value}")
except KeyError:
    print(f"The key '{key_to_access}' does not exist in the dictionary.")
#2.3
my_dictionary["name"]=45
print(my_dictionary)
#2.4
my_dictionary[123]=45
print(my_dictionary)
#2.5
del my_dictionary["name"]
print(my_dictionary)

my_dictionary.pop(123)
print(my_dictionary)