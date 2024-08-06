# Create a list and iterate over it using a while loop.
# Iterate over the list using a for loop with the range function.
# Iterate over the list using a for loop with the in operator.
# Iterate over the list using a for loop with the in operator and the enumerate function.

list = [0,1,2,3,5,1,7,1,7,2,8,3,8,4,2]
i = 0
while i < len(list):
    print(f"List element #{i+1}: {list[i]}")
    i+=1

for i in range(len(list)):
    print(f"List element #{i+1}: {list[i]}")

for idx, i in enumerate(list):
    print(f"List Element #{idx + 1}: {i}")
