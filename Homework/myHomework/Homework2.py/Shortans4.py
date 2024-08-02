# Explain what the break and continue statements do in a loop. Provide an example of each.

# The break statement completely stops the loop and let the code automatically move onto the next input

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
index = 0
while index < len(numbers):
    if numbers[index] == target:
        print("Found target number at index:", index)
        break
    index += 1
else:
    print("Target number not found in the list")


# The continue statement is like a fork in the road, if a certain condition is met, then the code continues, but if it is not, then the code keeps doing the loop

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
skip_number = 5
for number in numbers:
    if number == skip_number:
        continue  
    print(number)
