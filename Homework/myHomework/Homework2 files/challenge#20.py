# Create a list and iterate over it using a while loop.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
counter = 0
while counter < len(numbers):
    print(numbers[counter])
    counter +=1

# Iterate over the list using a for loop with the range function.
for i in range(0,len(numbers)):
    print(numbers[i])

# Iterate over the list using a for loop with the in operator.
for num in numbers:
    print(numbers[num-1])

# Iterate over the list using a for loop with the in operator and the enumerate function.
for idx, num in enumerate(numbers):
    print(numbers[num-1])