numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# Extract and print elements from a list that have even indexes.
for i in range(len(numbers)):
    if i % 2 ==0:
        print(numbers[i])

# Extract and print elements in reverse order.
numbers.reverse()
for i in range(len(numbers)):
    print(numbers[i])

# Extract and print a subset of elements with a stride size of 2 within that subset.
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(numbers[1:9:2])

# Extract and print elements with even indexes starting from the 5th element.
for i in range(4,len(numbers)):
    if i % 2 ==0:
        print(numbers[i])
