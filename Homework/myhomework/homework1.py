'''
def calculate_area(r):
         return r*r*3.14
print(calculate_area(5))



x=[4,2,3,1]
x.sort(reverse=True)
print(x)



name=str(input("What is ur name"))
x=input("ur 1st test score")
if not type(x) is int:
  raise TypeError("Only integers are allowed")
y=input("ur 2nd test score")
if not type(y) is int:
  raise TypeError("Only integers are allowed")
z=input("ur 3rd test score")
if not type(z) is int:
  raise TypeError("Only integers are allowed")
print(f'{name}, ur score is {x*y*z/3}')



name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
print(f"Hello, {name}. Your salary is ${salary:,.2f}")



name = input("Enter your name: ")
salary = float(input("Enter your salary: "))
formatted_salary = "{:,.2f}".format(salary)
print("Hello, {}. Your salary is ${}.".format(name, formatted_salary))



num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print(f"{num} is zero.")
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number.")
            break
    else:
        print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
num_str = str(num)
if num_str == num_str[::-1]:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")



favorite_movies = ["The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction", "Inception"]
favorite_movies.insert(1, "The Matrix")
del favorite_movies[3]
print("Updated list of favorite movies:")
for movie in favorite_movies:
    print(movie)



def remove_even_numbers(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    return odd_numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = remove_even_numbers(numbers)
print("Updated list with only odd numbers:")
print(filtered_numbers)



favorite_movies = [
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction"
]
new_movie = "Inception"
favorite_movies.insert(1, new_movie)
print(favorite_movies)



favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction"
]
removed_movie = favorite_movies.pop(2)
print("Updated list after removing the third movie:", favorite_movies)
last_movie = favorite_movies.pop()
print("Removed last movie:", last_movie)
print("Final updated list of favorite movies:", favorite_movies)



favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Dark Knight",
    "Inception"
]
specific_movie = "Inception"
count_specific_movie = favorite_movies.count(specific_movie)
print(f"'{specific_movie}' appears {count_specific_movie} times in the list.")
extended_favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Dark Knight",
    "Inception",
    "The Godfather",
    "Inception",
    "The Dark Knight",
    "Pulp Fiction",
    "The Godfather",
    "The Shawshank Redemption"
]
movie_counts = {movie: extended_favorite_movies.count(movie) for movie in set(extended_favorite_movies)}
print("Occurrences of each movie in the extended list:")
for movie, count in movie_counts.items():
    print(f"'{movie}': {count} times")



favorite_movies = [
    "The Shawshank Redemption",
    "Inception",
    "The Dark Knight",
    "Inception"
]
favorite_movies.sort(reverse=True)
print(favorite_movies)



combined_list = ["Inception", "The Matrix", "Interstellar", "1984", "Brave New World", "Fahrenheit 451"]
reversed_list = combined_list[::-1]
print("Reversed list:", reversed_list)
reversed_list[:3] = reversed_list[:3][::-1] 
print("Updated combined list:", reversed_list)
'''