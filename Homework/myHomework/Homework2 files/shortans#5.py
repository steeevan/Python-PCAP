# 5. List comprehension is a way of created a list using neat syntax. For example:
# This program uses a for loop to check through 0 and 19 and see if it's an even number. If it is then, it adds it to the list.
even_nums = []
for i in range(20):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)

