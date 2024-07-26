# 8:
list1 = [0,1,2,3,4,5,6,7,8,9,10]
list2 = [1,2,3,4,6,7,8,9,10,11,12]
def list_comparor(list1,list2):
    list3 = []
    for i in range(len(list1)):
        if list1[i] in list2:
            list3.append(list1[i])
    return list3

print(list_comparor(list1,list2))

# This compares the two lists by iterating through the first list and checking if the item in the first list is in the second one.
# If so, it adds it to an extra list that is only used in the function and then returns this extra list once done.