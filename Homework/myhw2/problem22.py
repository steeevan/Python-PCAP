#Create a list of the squares of the first 10 positive integers using list comprehension.
squares = [x**2 for x in range(1, 11)]
print("Squares of the first 10 positive integers:", squares)
#Create a list formed of characters from a string.
string = "hello"
char_list = [char for char in string]
print("List of characters 'hello':", char_list)
#Create a list of all the prime numbers between 1 and 100 using a helper function to check for primes.
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
primes = [x for x in range(1, 101) if is_prime(x)]
print("List of all prime numbers between 1 and 100:", primes)
#Create a list of all the even numbers between 1 and 100, replacing odd numbers with 0
even_replaced = [x if x % 2 == 0 else 0 for x in range(1, 101)]
print("List of all even numbers between 1 and 100:", even_replaced)