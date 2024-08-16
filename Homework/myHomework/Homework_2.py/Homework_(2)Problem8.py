# Write a function that takes two lists and returns a new list containing only the elements that are common to both lists.

def c(one,two):
    uno = set(one)
    dos = set(two)
    common_set = uno and dos
    return list(common_set)
list1 = [1,2,3,4,5]
list2 = [2,5,3,1,7,2]
print(c(list1,list2))