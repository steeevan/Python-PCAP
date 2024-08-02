# Create a list of the squares of the first 10 positive integers using list comprehension.
squares = [n + 1 for n in range(0,10)]
print(squares)

# Create a list formed of characters from a string.
word = [character for character in 'skibidi']
print(word)
# Create a list of all the prime numbers between 1 and 100 using a helper function to check for primes.
def is_prime(num):
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num // 2):
        if num % i == 0:
            return False
    return True

def findPrimeBetween(start_num, end_num):
    return [num for num in range(start_num, end_num) if is_prime(num)]

args = [1,100]
print(findPrimeBetween(*args))

# Create a list of all the even numbers between 1 and 100, replacing odd numbers with 0.

