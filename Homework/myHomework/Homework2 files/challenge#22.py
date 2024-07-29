# Create a list of the squares of the first 10 positive integers using list comprehension.
squares = [num * num for num in range(1,11)]

# Create a list formed of characters from a string.
letters_in_peptidoglycan = [character for character in 'peptidoglycan']

# Create a list of all the prime numbers between 1 and 100 using a helper function to check for primes.
def isPrime(num):
    if num <= 1 or num % 1 > 0:
        return False
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True

prime_numbers = [i for i in range(1, 101) if isPrime(i)]
print(prime_numbers)

# Create a list of all the even numbers between 1 and 100, replacing odd numbers with 0.
even_numbers_zeroed_odd = [i if i % 2 ==0 else 0 for i in range(1,101)]
