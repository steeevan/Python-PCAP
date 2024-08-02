# Creating a list of elements
my_list = [1, 2, 3, 4, 5]
# Testing whether an element exists in the list using the in operator
element_to_test = 3
if element_to_test in my_list:
    print(f"{element_to_test} exists in the list.")
else:
    print(f"{element_to_test} does not exist in the list.")
# Testing whether an element does not exist in the list using the not in operator
element_to_test = 6
if element_to_test not in my_list:
    print(f"{element_to_test} does not exist in the list.")
else:
    print(f"{element_to_test} exists in the list.")