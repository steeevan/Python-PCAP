'''
9 Advanced lists in python
- Access and manipulating list elements using indexing and slicing
-understand and apply advanced list slicing techniques
- differetiate between shallow and deep copies of list
- multi-dimensinal arrays
'''
'''
9.1 index and negative indexing
- lists in pythom can be accessed using index numbers. negative indexing allows access to elements from the end of the list
'''
#example 9.1
# create a list containing the first twn squares
squares=[1,4,9,16,25,36,49,64,81,100]
'''
9.2 Advanced list slicing
-list slicing allows you to use sytanx 'list[start:end]'
'''
#ex 9.2
# extract elements from a list that have been indexed using the stride size argument
print(squares[::2])
#ex 9.2.2
#using negative indexing stride size argument
print(squares[::-2])
print(squares)
#example 9.2.3
# extract elements at a defined set or known as a subset 
print(squares[4:8:2])
#example 9.2.4
# extract elements with even indexes from the 5th elements
print(squares[4::2])
'''
9.3 advanced list assignment
-list can be modified by assigning values to slices of the list
'''
#ex 9.3.1
my_numbers=[1,3,6,10,15,21,28,36,45,55]
print(f'my list of numbers(first 10 triangle numbers):{my_numbers}')

#substituting a subset of the list with new elements
my_numbers[1:3]=[4,9]
print(f'Mylist of numbers(substitution):{my_numbers}')

#example 9.3.2
#replace every nth elements with a new value where N=3
my_numbers[::3]=[1,16,49,100]
print(f'My list of numbers (nth replacements):{my_numbers}')

#ex 9.3.3
# replace and resize a subset of the list
my_numbers[4:]=[25,36,49,64]
print(f'my list of number(first 8 square numberss):{my_numbers}')
#ex 9.3.4
#delete every nth number starting from the 2nd element
del my_numbers[1::2]
print(f'my list of number(every other square number):{my_numbers}')
'''
9.4 shallow and deep list copies
- shallow copies duplicate the structure of a list but not the elements of the list 
-Deep copies duplicate both  the structure list elements
'''
# 9.4.1 create a shallow copy of the original list using slicing notation
my_phrases=[['a','b','c'],['d','e','f'],['g','h','i']]
print(f'original list of the phrase:{my_phrases}')

my_shallow_phrases=my_phrases[:2]+[['j','k','l']]
print(f'shallow copy of my phrases:{my_shallow_phrases}')
#ex 9.4.2 create a shallow copy using the list() function
my_other_shallow_phrases=list(my_phrases)+[['j','k','l']]
print(f'Another shallow copy of my phrases:{my_other_shallow_phrases}')
#ex 9.4.3 make a change to the original list of phrases
my_phrases[0][0]='Alpha'
my_phrases[0][1]='Beta'
my_phrases[0][2]= 'Gamma'
print(f'\nUpdated original list of phrases:{my_phrases}')
print(f'shallow copy of my phrases:{my_shallow_phrases}')
print(f'Another shallow copy of my phrases:{my_other_shallow_phrases}')
#ex 9.4.4 create a deep copy of the original list
import copy
my_phrase=[['a','b','c'],['d','e','f']],['g','h','i']
my_deep_phrases=copy.deepcopy(my_phrases)
print(f'original list of phrases:{my_phrase}')
print(f'Deep copu of my phrases:{my_deep_phrases}')
my_phrases[0][0]='Alpha'
my_phrases[0][1]='Beta'
my_phrases[0][2]= 'Gamma'
print(f'\nUpdated original list of phrases:{my_phrases}')
print(f'Deep copy of my phrases:{my_deep_phrases}')
'''
9.5 Iterating list
-list can be iterated through using while loops, forr loops and the enumarate function.
'''
#ex 9.5.1
my_diatomic_list=[0,1,1,2,1,3,2,3,1,4,3,5,2,5,3,4]
i=0
while i<len(my_diatomic_list):
    print(f'diatomic sequence-element#{i+1}:{my_diatomic_list[i]}')
    i+=1
#ex 9.5.2 iterarte the list using a for loop
for x in range(len(my_diatomic_list)):
    print(f'Diatomic sequence-element#{x+1}:{my_diatomic_list[x]}')
# example 9.5.3 iterate the list using a for loop with the 'in' operator
for elem in my_diatomic_list:
    print(elem)
#ex 9.5.4 iterate the list using the enumberate function
for idx, elem in enumerate(my_diatomic_list):
    print(f"Diatomic sequence-element #{idx+1}:{elem}")
'''
9.6 list membership
- list membership can be tested using the 'in' and 'not in' operators.
'''
#9.6.1 test wheter an element exists in a list
squares=[1,4,9,16,25]
x=16
if x in squares:
    print(f'{x} exists ini our list of square numbers')
else:
    print(f'{x} does not exist in out list of square numbers')
# ex 9.6.2 test whether an element is not in the list
y=169 
if y not in squares:
    print(f'{y} does not exist in out list of square numbers')
else:
    print(f'{y} exists in our list of square number')
'''
9.7 list comprehension
-list comprehension provides a conscise wat of creating lists
'''
#ex 9.7.1
squares=[num*num for num in range(1,9)]
print(squares)
# example 9.7.2 create a list formed of characters from a string
letters_in_abibliophobia=[charater for charater in'abibliophobia']
print (letters_in_abibliophobia)
#ex 9.7.3
def isPrime(num):
    if num<=1 or num%1>0:
        return False
    for i in range(2, num//2):
        if num%i==0:
            return False 
    return True
prime_numbers=[i for i in range(1,101)if isPrime(i)]
print(prime_numbers)

#ex 9.7.4
even_numbers_zeroed_odd=[i if i%2==0 else 0 for i in range(1,101)]
print(even_numbers_zeroed_odd)
'''
9.8 multi-dimensional arrays
-list that contains other lists
'''
#ex 9.8.1 create a two dimensional array
my_2d_array=[[1,2,3],[4,5,6],[7,8,9]]
for row in my_2d_array:
    for elem in row:
        print(elem,end='')
    print()
# ex 9.8.2 create a two dimensional array with list comprehension
numbers_cols=3
numbers_rows=3
my_2d_array=[[0 for i in range(numbers_cols)]for j in range(numbers_rows)]
for row in my_2d_array:
    for elem in row:
        print(elem, end='')
    print()
#ex 9.8.3 access elements using square brackets and indices
my_2d_array=[[1,2,3],[4,5,6],[7,8,9]]
print(my_2d_array[0][0])
print(my_2d_array[1][1])
print(my_2d_array[2][2])
# ex 9.8.4 manipulate a two-dimnensional arrat
my_2d_array=[[1,2,3],[4,5,6],[7,8,9]]
my_2d_array.insert(2,[9,9,9])
my_2d_array.append([7,4,7])
my_2d_array[0].extend([0,0])
my_2d_array[2].reverse()
del my_2d_array[3]
for row in my_2d_array:
    for elem in row:
        print(elem, end='')
    print()