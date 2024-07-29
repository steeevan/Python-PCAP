# Define a list
my_list = ["apple", "banana", "cherry", "date"]

# Iterate over the list using a while loop
index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

print()  # Just for separating outputs

# Iterate over the list using a for loop with the range function
for i in range(len(my_list)):
    print(my_list[i])

print()  # Just for separating outputs

# Iterate over the list using a for loop with the in operator
for item in my_list:
    print(item)

print()  # Just for separating outputs

# Iterate over the list using a for loop with the in operator and the enumerate function
for index, item in enumerate(my_list):
    print(f"Index {index}: {item}")