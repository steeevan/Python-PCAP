numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Test whether an element exists in a list using the in operator.
x = 10
if x in numbers:
    print(f'{x} is in numbers!')
else:
    print(f'{x} is not in numbers!')

# Test whether an element does not exist in a list using the not in operator.
if x not in numbers:
    print(f'{x} is not in numbers!')
else:
    print(f'{x} is in numbers!')
