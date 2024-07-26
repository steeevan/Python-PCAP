
# exercise 1.1
import math
def calculate_area(radius):
    area = (radius**2) * math.pi
    return area
print(calculate_area(5))

# exercise 1.2
list_1 = [10, 293, 1, 3, 10000, 309]
list_1.sort(reverse=True)
print(list_1)
# this sort function is different because normally it sorts in ASCENDING order, but in this case it sorted in DESCENDING order

# exercise 2.1 and 2.2
name = input("Please enter your name: ")
def get_score1():
    global t_score1
    try:
        t_score1 = int(input("Enter your first test score: "))
        return t_score1
    except:
        print("That's not a number, please try again!")
        get_score1()
    
def get_score2():
    global t_score2
    try:
        t_score2 = int(input("Enter your second test score: "))
        return t_score2
    except:
        print("That's not a number, please try again!")
        get_score2()
    
def get_score3():
    global t_score3
    try:
        t_score3 = int(input("Enter your third test score: "))
        return t_score3
    except:
        print("That's not a number, please try again!")
        get_score3()
    

get_score1()
get_score2()
get_score3()
print(f'Hello {name}, your average test score is {(t_score1+t_score2+t_score3)/3}.')

# exercise 3.1
name2 = input("Please enter your name: ")
salary = int(input("Please enter your salary: "))
print(f'Hello, {name2}. Your salary is ${salary:,.2f}.')
# exercise 3.2
print('Hello, {}. Your salary is ${:,.2f}.'.format(name2, salary))

# exercise 4.1 and 4.2
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True
num1 = int(input("Enter a number  to check: "))

if num1 == 0:
    print("The number is 0!")
elif num1 < 0:
    print("this number is negative.")
    if is_prime(num1) == True:
        print("This number is also prime!")
    else:
        print("This number is not prime.")
elif num1 > 0:
    print("This number is positive")
    if is_prime(num1) == True:
        print("This number is also prime!")
    else:
        print("This number is not prime.")
else:
    pass
if str(num1) == str(num1)[::-1]:
    print("This number is also palindrome!")

# exercise 5.1
fav_movies = ["Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", "Super Mario Bros", "Hunger Games Catching Fire"]
fav_movies.insert(1,"Spider-Man: Across the Spider-Verse")
del fav_movies[3]
print(fav_movies)

# exercise 5.2
num_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
if len(num_list) % 2 == 1:
    for i in range(0,len(num_list)//2 + 1):
        if num_list[i] % 2 == 0:
            del num_list[i]
else:
    for i in range(0,len(num_list)//2):
        if num_list[i] % 2 == 0:
            del num_list[i]
print(num_list)

# exercise 6.1
new_fav_movies = fav_movies[1:4]
new_fav_movies.reverse()
print(new_fav_movies)

# exercise 7.1
fav_movies.insert(1,"Harry Potter and the Order of the Phoenix")
fav_movies.insert(len(fav_movies),"Garfield")

# exercise 8.1
fav_movies.pop(2)
print(fav_movies)
last = fav_movies.pop(-1)
print(last)

# exercise 9.1
fav_movies.count("Garfield")
fav_movies_multi = ["Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire","Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire","Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire","Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire","Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire","Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", \
                    "Garfield", "Hunger Games Catching Fire"]
print(fav_movies_multi.count("Garfield"))
print(fav_movies_multi.count("Harry Potter and the Deathly Hallows Part 2"))
print(fav_movies_multi.count("Hunger Games Mockingbird"))
print(fav_movies_multi.count("Harry Potter and the Sorceror's Stone"))
print(fav_movies_multi.count("Hunger Games Catching Fire"))

# exercise 10.1
fav_movies = ["Harry Potter and the Deathly Hallows Part 2", "Hunger Games Mockingbird", "Harry Potter and the Sorceror's Stone", "Super Mario Bros", "Hunger Games Catching Fire"]
fav_books = ["Hunger Games", "Harry Potter", "Artemis Fowl", "Renegades", "Shadow and Bone"]
fav_books_and_movies = fav_books + fav_movies
fav_books_and_movies.sort()
print(fav_books_and_movies)
fav_books_and_movies.sort(reverse=True)
print(fav_books_and_movies)

# exercise 11.1
fav_books_and_movies.reverse()
print(fav_books_and_movies)

fav_books_and_movies[0:3].reverse()
print(fav_books_and_movies)