'''
Understanding loops in python
- While loops
- For loops
-utilize the range function in loops
- else keyword in loops nested loops
- break and continue keywords
'''

'''
7 loops
7.1 while loops
A while loop repeatedly executes a block of code as long as a specified condition is true
'''
#example 7.1
n=int(input("Please enter a positive interger value ")) # type cast onew data type to another
if n<1:
    print("please enter a positive number 2 ")
else:
    factorial =1
    counter=1
    while counter <= n:
        factorial *=counter
        counter+=1
    print(f"The factorial of {n} is {factorial}")
'''
7.2 While-else loop
- a while else loop executes the else block if the while loop completes normally (the condition becomes false)
'''
#example 7.2
counter=1
sum=0
while counter<=10:
    sum +=counter
    counter+=1
else:
    print(f'The sum of first 10 positive interger value is {sum}')
'''
7.3 for loop
- A for loop iterates over a sequence (tuple, lists, strings dictionarirs) and executes
a block of code for each element
'''
#ex 7.3
shopping_list=['Apples', 'Bananas','Butter']
for shopping_item in shopping_list:
    print(f'{shopping_item}:{len(shopping_item)}')
'''
7.4 range function
- The range function generates a sequence of nuymbers which is commonly used in for loops
'''
#ex 7.4.1
#range function with single argument
#print 0-9
for n in range(10):
    print(n)
#ex 7.4.2
#range function with two arguments
#prints 10-19
for n in range (10,20):
    print(n)
#example 7.4.3
#range function with three arguments
#prints every second number from 10-18
for n in range(10,20,2):
    print(n)
'''
7.5 for else loops
-A for else loop executes the else bock is the for loop executes normally
    (without encountering a break statement)
'''
#ex 7.5
for n in range(3):
    passwords_attempt= input('please enter your password:')
    if passwords_attempt=='password123!':
        print('Successful authentication')
        break
else:
    print('your account has been locked after 3 failed attempts to login.')
    print('please contact your system administrator to unlock your account.')
'''
7.6 break statement
- the break statement terminates the loop permaturely
'''
#ex 7.6
import random
random_number=random.randint(1,30)
guess_counter=0
guess_limit=5
print('*****guess the number!*****')
print(f'I am thinkinbg of a number between 1 and 30, can you guess it in less than{guess_limit}attempts')
while guess_counter<guess_limit:
    guess=int(input(f'Attempt #{guess_counter+1} enter your guess'))
    guess_counter+=1
    if guess< random_number:
        print('too low')
    elif guess > random_number:
        print('too high')
    else:
        break
if guess == random_number:
    print(f'congratualations! you guessed correctly in {guess_counter} attempts')
else:   
    print(f'sorry! game over! the numnber i was thinking of was{random_number}.')
'''
7.7 countinue statement
-the continue statement skipes the rest of the code inside the loopo for the current iteration and mover to the next iteration
'''
#example7.7
shopping_list=['apples','Bananas','Potatoes','Tomatoes','Milk','Chess', 'Eggs','Butter']
dairy_products=['Milk','Cheese','Eggs','Butter']
for shopping_item in shopping_list:
    if shopping_item in dairy_products:
        continue
    print(shopping_item)
'''
7.8 Nested Loops
-nested loops are loops insides loops. Each time the outer loop runs the inner runs completely.
'''
#example 7.8
number_columns=5
number_row=5
fill_character='*'
for row in range(number_row):
    print(fill_character, end=' ')
    for column in range(number_cinlumns-1):
        print(fill_character, end='')
    print('')
#********************
'''
8 advanced strings in pytthon
- understand and use cahracter encodings
- utilize escape characters
- explain and handle immutable strings
- work with multi line strings
- compare strings effectively
- slicing/cloning techniques
- common string methods and functions
'''
'''
8.1 character encoding
- character encoding are methods of converting characters into bytes and vice versa. unicode
    is the most common encoding used in python
'''
#example 8.1
hosipital_in_french='hospital'
hosipital_in_japanese='病院'
hosipital_in_arabic='hosipi'
print(f'The name for hospital in french is {hosipital_in_french}')
print(f'The name for hosipital in japanese is :{hosipital_in_japanese}')
print(f'The name for hosipital in arabic is :{hosipital_in_arabic}')

#8.1.2 ex
日本の人口=126_500_500

#ex 8.1.4
names=['Quddus','gobmann','Jose']
dragon='龙'
print(f'The unicode code point value for {dragon} is {ord(dragon)}')
'''
8.2 escape sequence
-escape sequence allow the inclusion of special character in strings
'''
#8.2
#escape sequences start with a backslash (\)
#and are followed by a character that indicates the type of special character.
'''
8.3 Immutable strings
-strings in python are immutable, meaning they cannot be changes after they are created
'''
# example 8.3.1
test_string='hello world'
print(test_string[6])
test_string[6]="Q"

# ex 8.3.2
my_first_string='abracadabra'

#example 8.3.3
# while string are immutable, variables can be reassigned to different strings
my_string='I am a data scientist'
print(my_string)
my_string='I am a software engineer'
print(my_string)
'''
8.4 multi-line strings
- multi line strings are created using triple quotes
'''
#example 8.4
my_multiline_string = '''line 1\tEOL
Line 2\t\tEOL
Line 3    EOL'''
print(my_multiline_string)
'''
8.5 strings comparison
- strings can be somparees using comparison operators
'''
# compare string with different code point sequence
'''
8.6 Advanced string slicing
-string slicing allows extracting parts of a string using syntac 'string[start:end:step]'
'''
#ex 8.6
# advanced slicinbg techniques
my_string='abracadabra'
print(my_string[::2])
print(my_string[::-2])
print(my_string[4:10:2])
print(my_string[4::2])
'''
8.7 copying and cloning
-strings can be copied or cloned using slicing
'''
#ex 8.7
'''
8.8 string methods
'''
#ex 8.8
'''
8.9 string functrions
'''
# example 8.9
print(len('abracadabra'))
print(chr(9786))
print(ord('ai'))