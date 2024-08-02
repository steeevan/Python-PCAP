current_number = 1
sum_of_evens = 0

while current_number <= 50:
    if current_number % 2 == 0:
        sum_of_evens += current_number
    current_number += 1

print("The sum of even numbers between 1 and 50 is:", sum_of_evens)