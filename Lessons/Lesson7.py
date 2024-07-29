'''
Understanding Loops in Python

- While loops
- For loops
- Utilize the range function in loops
- Else keyword in loops
- nested loops
- break and continue
'''

'''
7 LOOPS

7.1 While loops

- A while loop repeatedly executes a block of code as long as a specified condition is true
'''

# Example 7.1

n = int(input("Please enter a positive integer value: "))       # typecast one data type to another
if n < 1:
    print("Please enter a positive number")
else:
    factorial = 1
    counter = 1
    while counter <= n:
        factorial *= counter
        counter += 1
    print(f"The factorial of {n} is {factorial}")

'''
7.2 While-else Loop
- A while else loop executes the else block if the while loop completes normally 
(the condition becomes false)
'''
# Example 7.2
counter = 1
sum = 0
while counter <= 10:
    sum += counter
    counter += 1
else:
    print(f"The sum of the first 10 positive integer values is {sum}")

'''
7.3 For loop
- A for loop iterates over a sequence (tuple, lists, strings, dictionaries) and executes
a block of code for each element
'''
# Example 7.3
shopping_list = ["Apples", "Bananas", "Butter"]
for shopping_item in shopping_list:
    print(f"{shopping_item}: {len(shopping_item)}")

'''
7.4 Range Function
- The range function generates a sequence of numbers which is commonly used in for loops
'''
# Example 7.4.1
# Range function with single argument
# prints 0 - 9
for n in range(10):
    print(n)
# Examples 7.4.2
# Range function with two arguments
# prints 10 - 19
for n in range(10, 20):
    print(n)
# Example 7.4.3
# Range function with three arguments
# prints every second number from 10 - 18
for n in range(10, 20, 2):
    print(n)

'''
7.5 For-else loops
- A for else loop executes the else block if the for loop executes normally 
(without encountering a break statement)
'''
# Examples 7.5
for n in range(3):
    password_attempt = input("Please enter your password: ")
    if password_attempt == "Passw0rd123!":
        print("successful authentication")
        break
else:
    print("Your account has been locked after 3 failed attempts to login.")
    print("Please contact your system administrator to unlock your account.")

'''
7.6 Break Statement
- The break statement terminates the loop prematurely
'''
# Example 7.6
import random
random_number = random.randint(1, 30)
guess_counter = 0
guess_limit = 5
print('******** Guess the Number! ********')
print(f'I am thinking of a number between 1 and 30. Can you guess it in less than {guess_limit} attempts?')
while guess_counter < guess_limit:
    guess = int(input(f"Attempt #{guess_counter+1} Enter your guess:"))
    guess_counter += 1
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print('Too high!')
    else:
        break

if guess == random_number:
    print(f"Congratlations! You guessed correctly in {guess_counter} attempts!")
else:
    print(f"Sorry! Game Over! The number I was thinking of was {random_number}")

'''
7.7 Continue Statement
- The continue statement skips the rest of the code inside the loop for the current iteration and
moves to the next iteration
'''

# Example 7.7
shopping_list = ["Apples", "Bananas", "Potatoes", "Tomatoes", "Milk", "Cheese", "Eggs", "Butter"]
dairy_products = ["Milk", "Cheese", "Eggs", "Butter"]
for shopping_item in shopping_list:
    if shopping_item in dairy_products:
        continue
    print(shopping_item)

'''
7.8 Nested Loops
- Nested Loops are loops inside loops. Each time the outer loop runs, the inner loop runs completely.
'''
# Example 7.8
number_columns = 5
number_rows = 5
fill_character = '*'
for row in range(number_rows):
    print(fill_character, end=' ')
    for column in range(number_columns -1):
        print(fill_character, end=' ')
    print(' ')
'''
Explanation:
The outer loop runs for each row.
The inner loop runs for each column.
The end=' ' parameter in print keeps the cursor on the same line.
The rectangle is printed with the specified dimensions.
'''
# **************************************************************************************************
'''
8 Advanced Strings in Python
- Understand and use character encodings
- Ultilize escape characters
- Explain and handle immutable strings
- Work with multi line strings
- Compare strings effectively
- Slicing/cloning techniques
- Common string methods and functions
'''

'''
8.1 Character Encoding
- Character encodings are methods of converting characters into bytes and vice versa. Unicode
is the most common encoding used in Python
'''
# Example 8.1.1
hospital_in_french = "hoppytal"
hospital_in_japanese = "bean ren"
hospital_in_arabic = "mustafash"

# Examples 8.1.2
nya = 126_500_000
print(f"The population of Japan is: {nya}")

# Example 8.1.3
directions = "The name of the hospital"

#ASCII works for special characters

'''
8.2 Escape Sequences
- Escape sequences allow the inclusion of special characters in strings
'''
# Example 8.2
print("Escaping a \' single quote character")

# Escape sequences start with a backslash (\)
# and are followed by a character that indicates the type of special character.

'''
8.3 Immutable Strings
- Strings in Python are immutable, meaning they cannot be changed after they are created
'''
# Example 8.3.1
test_string = "Hello World"
print(test_string[6])
#test_string[6]="Q"

# Example 8.3.2
my_first_string = 'abracadabra'
my_second_string = 'abracadabra'
print(f"id(my_first_string) = {id(my_first_string)}")
print(f"id(my_second_string) = {id(my_second_string)}")
for idx in range(0, len(my_first_string)):
    print(f'{my_first_string[idx]} = {id(my_first_string[idx])}')

# Example 8.3.3
# While strings are immutable, variables can be reassigned to different strings
my_string = "I am a Data Scientist"
print(my_string)
my_string = "I am a Software Engineer"
print(my_string)

'''
8.4 Multi-Line Strings
- Multi Line strings are created using triple quotes
'''
# Example 8.4
my_multiline_string = '''Line 1\tEOL
Line 2\t\tEOL
Line      EOL'''
print(my_multiline_string)

'''
8.5 String Comparison
- Strings can be compared using comparison operators
'''
# Compare strings with different code point sequences

'''
8.6 Advanced String Slicing
- String slicing allows extracting parts of a string using syntax 'string[start:end:step]'
'''
# Example 8.6
# Advanced slicing techniques
my_string = "abracadabra"
print(my_string[::2])
print(my_string[::-2])
print(my_string[4:10:2])
print(my_string[4::2])

'''
8.7 Copying and Cloning
- Strings can be copied or cloned using slicing
'''
# Example 8.7

'''
8.8 String Methods
'''
# Example 8.8

'''
8.9 String Functions
'''
# Example 8.9