# Exercises

# 1
ask = int(input("Enter a radius: "))
def calculate_area(radius):
    return(radius**2*3.14)
print(calculate_area(ask))

# 2
list = [24,90,72,34,56,1,29,182,4]
list.sort()
print(list)
# Easy and convenient

# 3 and 4
name = input("Enter your name:")
while True:
    try:
        test_1 = int(input("Enter a test score as a whole number: "))
        test_2 = int(input("Enter another test score as a whole number: "))
        test_3 = int(input("Enter another test score as a whole number: "))
        break
    except ValueError:
        print("ERROR enter a valid number: ")
print(f"Hello {name}, your test average is {(test_1+test_2+test_3)/3:.3f}")

# 5 and 6
namey = input("Enter your name: ")
salary = int(input("Enter your salary: "))
j = format(salary, ',')
print(f'Hello {namey}, your salary is {j}')

# 7 and 8
def bigboi(num):
    if num == 0:
        return("0")
    elif num > 0:
        return("Your number is positive!")
    elif num < 0:
        return("Your number is negative!")

def prime(number):
    if number <= 1:
        return("Nope")
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return("Your number is not prime!")
    return("Your number is prime")

def palindrome(nums):
    h = str(nums)
    if h == h[::-1]:
        return("Your number is a palindrome!")
    else:
        return("Your number is not a palindrome!")

def main():
    p = int(input("Enter a number: "))
    print(bigboi(p))
    print(prime(p))
    print(palindrome(p))
if __name__ == "__main__":
    main()

# 9 and 10
movie = ["Indiana Jones: The Last Crusade", "Whiplash", "The Breakfast Club", "Fast and Furious", "Mission Impossible"]
movie.remove("Fast and Furious")
movie.insert(2,"LCOD: Take on Me")
print(movie)

import random
list = [random.randint(1,1000) for i in range(100)]
list.sort()
def even_exterminator(tlist):
    return [num for num in tlist if num % 2 != 0]
print(even_exterminator(list))

# 11
movie = ["Indiana Jones: The Last Crusade", "Whiplash", "The Breakfast Club", "Fast and Furious", "Mission Impossible"]
print((movie[1:4])[::-1])

# 12
movie.insert(2,"Uncharted")
movie.insert(6,"Coco")
print(movie)

# 13
movie.pop(3)
print(movie)
print(movie.pop(5))

# 14
q = movie.count("Whiplash")
print(q)
again = ["Indiana Jones: The Last Crusade", "Whiplash", "The Breakfast Club", "Whiplash","Fast and Furious", "Mission Impossible","Whiplash"]
g = again.count("Whiplash")
print(g)

# 15
movie.sort(reverse=True)
print(movie)

# 16
sigma = ["Indiana Jones: The Last Crusade", "Whiplash", "The Breakfast Club", "Whiplash","Fast and Furious", "Mission Impossible","Whiplash"]
print((movie[0:3])[::-1])