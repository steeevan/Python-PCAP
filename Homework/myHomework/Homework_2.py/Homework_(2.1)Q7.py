# Create a list of the squares of the first 10 positive integers using list comprehension.
# Create a list formed of characters from a string.
# Create a list of all the prime numbers between 1 and 100 using a helper function to check for primes.
# Create a list of all the even numbers between 1 and 100, replacing odd numbers with 0.

squares = [num**2 for num in range(1,11)]
print(squares)

letters = [character for character in "abracabra"]
print(letters)

def primey(num_num):
    if num_num <= 1 or num_num%1 > 0:
        return False
    for i in range(2,num_num//2):
        if num_num%i == 0:
            return False
    return True

prime = [i for i in range(1,101) if primey(i)]
print(prime)

even = [i if i%2 == 0 else 0 for i in range(1,101)]
print(even)