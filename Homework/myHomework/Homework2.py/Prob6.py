num = [1, 2, 3, 4, 5]
print(num)
# Test whether an element exists in a list using the in operator.
x = 10
if x in num:
    print(f"{x} is in the list")
else:
    print(f"{x} is not in the list")

# Test whether an element does not exist in a list using the not in operator.
x = 3
if x not in num:
    print(f'{x} is not in the list')
else:
    print(f'{x} is in the list')