# Problem 2: Write a function definition for a function that takes two arguments, a string and a character, 
# and returns the number of times the character appears in the string.

def hi(string,character):
    return string.count(character)

print(hi("Hello World!", "o"))