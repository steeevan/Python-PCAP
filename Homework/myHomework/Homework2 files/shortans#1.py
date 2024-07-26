'''
1. A for loop iterates through a certain range, using the range function, or through items in something like a list.
    A while loop iterates while a certain condition is satisfied. 
'''
# 'for' loop example:
# This program will determine how many a's are in a string by iterating through each letter in the string and checking if it's an a
test = "how many a's are in this: aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
As = 0
for i in range(len(test)):
    if test[i] == "a" or test[i] == "A":
        As += 1
print(f"There are {As} a's in there!")

# 'while' loop example:
# This program will count all numbers from 0 to 9 (inclusive)
# This is because it prints out counter and adds 1 to it until counter becomes greater than or equal to 10.
counter = 0
while counter > 10:
    print(counter)
    counter +=1