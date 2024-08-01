# Create a list and iterate over it using a while loop.
list = [1, 2, 3, 4, 5]

# Iterate over the list using a for loop with the range function.
for x in range(len(list)):
    print(f'Numbers: {list[x]}')

# Iterate over the list using a for loop with the in operator.
for e in list:
    print(e)

# Iterate over the list using a for loop with the in operator and the enumerate function.
for idx, l, in enumerate(list):
    print(f'Number: {l}')

