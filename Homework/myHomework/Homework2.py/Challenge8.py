# Write a function that takes two lists and returns a new list containing only the elements that are common to both lists.

def common_elements(list1, list2):
    return [element for element in list1 if element in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(common_elements(list1, list2))
