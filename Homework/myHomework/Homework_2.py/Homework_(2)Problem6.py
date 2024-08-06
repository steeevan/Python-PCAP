# Write a function to count the number of vowels (a, e, i, o, u) in a given string.

def vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
print(vowels("Hello"))