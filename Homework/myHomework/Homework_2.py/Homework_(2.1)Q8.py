# Use common list methods like append(), extend(), insert(), remove(), pop(), and clear() to modify a list.
# Use methods like index(), count(), sort(), reverse(), and copy() on a list.

list = [1,2,3,4,5,6,7,8,9,10]
list.append(11)
list.extend([12,13,14])
list.insert(0,101)
print(list)

list.remove(101)
list.pop()
print(list)

list.clear()
print(list)

list = [5,10,23,685,29,1,5,3]
list.index(1)
print(list)
list.count(5)
print(list)
list.sort()
print(list)
list.reverse()
print(list)
list.copy()
print(list)