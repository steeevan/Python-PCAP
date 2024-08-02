# Initial list
my_list = [1, 2, 3]

# Append an element to the end of the list
my_list.append(4)
print("After append(4):", my_list)

# Extend the list by appending elements from another list
my_list.extend([5, 6])
print("After extend([5, 6]):", my_list)

# Insert an element at a specific position
my_list.insert(2, 2.5)
print("After insert(2, 2.5):", my_list)

# Remove the first occurrence of an element
my_list.remove(2)
print("After remove(2):", my_list)

# Pop the last element from the list
last_element = my_list.pop()
print("After pop():", my_list)
print("Popped element:", last_element)

# Clear all elements from the list
my_list.clear()
print("After clear():", my_list)