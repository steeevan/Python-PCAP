numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
numbers2 = [22,23,24,25,26,27,28,29,30]
# Use common list methods like append(), extend(), insert(), remove(), pop(), and clear() to modify a list.
numbers.append(21)
numbers.extend(numbers2)
numbers.insert(15,20)
numbers.remove(20)
numbers.pop(16)
numbers.clear()

# Use methods like index(), count(), sort(), reverse(), and copy() on a list.
print(numbers.index(10))
print(numbers.count(3))
print(numbers.sort())
print(numbers.reverse())
numbers3 = numbers.copy()
print(numbers3)
