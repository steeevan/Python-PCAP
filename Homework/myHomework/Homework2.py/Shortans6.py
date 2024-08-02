# Explain the difference between mutable and immutable types in Python. Provide examples of each.

# Mutable in Python means that you can change the item inside of it while immutable means that once it is created, you cannot change anything inside if it, except for a few special commands

# A list is mutable

num = [1, 2, 3, 4, 5]
num.append(87)
print(num)

# A tuple is not

nums = (1, 2, 3, 4, 5)
nums.append(65)
print(nums)