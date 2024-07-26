# 4:
for i in range(101):
    if i % 3 == 0 and i % 5 ==0:
        print("Fizzbuzz")
        continue
    elif i % 3 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Buzz")
        continue
    else:
        print(i)
# This program uses a for loop to check all of the numbers from 1-100, check if they are divisible by 3,5, or both by using mod, and print out the number,
# fizz, buzz, or fizzbuzz. It uses an if/elif/else statement to check the divisors of the number.