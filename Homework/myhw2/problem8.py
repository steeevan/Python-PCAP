def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print("Common elements:", common_elements(list1, list2))