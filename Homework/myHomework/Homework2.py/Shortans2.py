# Write a function definition for a function that takes two arguments,
# a string and a character, and returns the number of times the character
# appears in the string.



def character(s, char):
    return s.count(char)



count = character('ooga booga', 'o')
print(count)  