'''
Basic Strings in Python
 - Create and manipulate strings
 - use string indexing and slicing
 - calculate string length
 - test string membership
 - concatenate strings
 - handle escape characters
 - user raw ans unicode string literals
 - compare strings
 - utilize various string methods
'''

'''
6.1 Creating Strings
- Simple strings: strings are sequences of characters in Python. They can be created by enclosing
     characters in single quotes (') or double quotes (")
- Multiline Strings: For strings that span multiple lines, use triple quotes (""") or singles are used
'''
# Example 6.1
# Creaate a simple string
first_name = "Jillur"
print(first_name)

# Create a multiline string
envelope_label = '''Jillur Quddus
1600 Pennsylvania Ave NW
Washington
DC 20500
United States'''
print(envelope_label)

'''
6.2 Indexing and Slicing
- Indexing: Access individual characters in a string using their position(index) with the first character at index 0
- Slicing: Extract a substring by specifiying a rance of indeces. The syntax is 'string[start:end]'
    start is inclusive, and end is exclusive
'''
# Example 6.2
# Create a simple string
lorem_ipsum = "lkdsj flkdsj fksjguhisdj kglj davjklgnshd bmg,.isjdklgnhbkf djnigo uhjdfkisouew hjfiodghujnkvlm cdjfshcknvhisfjb snvckjhfsbjv czkjhdagjfbdzchdgfjdsvbcz kjhdsj"

# Print the 13th character
print(lorem_ipsum[12])

# Print the substring between the 29th and 56th characters
print(lorem_ipsum[28:56])

# Print the last word
print(lorem_ipsum[-7:-1])

'''
6.3 String Length
- Length of a string: use the 'len()' function to determine the number f characters in a string,
    this includes spaces and punctuation
'''
# Example 6.3
# Calculate the length of a string
print(len(lorem_ipsum))


'''
6.4 String Membership
- Membership operator: Use the 'in' keyword to check if a substring exists within a string
    This returns 'True' if the substring is found and 'False' otherwise
'''
# Example 6.4
# Test whether a given sequence of characters can be found in a string
if "lkdsj" in lorem_ipsum:
    print("lkdsj has been found!")

'''
6.5 Concatenating Strings
- String concatentation: Use the '+' operator to join two or more strings into a single string.
'''
# Example 6.5
lorem_ipsum_continued = "Ut enim ad minim veiam, qius nostrud exercitation ullamco laboris nisi ut aliquip ez eq commodo consequat"
lorem_ipsum_updated = lorem_ipsum + " " + lorem_ipsum_continued
print(lorem_ipsum_updated)

'''
6.6 Escape Characters
- Escape characters: Use '\' backslash to include special characters in a string, 
    such as quotes or newlines characters
'''
# Example 6.6
# Try to create a string containing illegal characters
#illegal_string = "My name is "Jillur""
# Syntax Error: Invalid syntax

# Escape the illegal characters using the backslash character
legal_string = "My name is \"Jillur\""
print(legal_string)

'''
# 6.7 Raw and Unicode String Literals
- Raw strings: prefix a string with 'r' to create a raw string where escape sequences are not processed
- Unicode string: Prefix with a string with 'u' to create a unicode string(necessary for Python 2)
    but all strings in Python 3 are unicode
'''
# Example 6.7
# Create and print a raw string literal
raw_string_literal = r"My name is Jillur Quddus\nI am a Chief Data Scientist and Principal Polyglot Software Engineer. Please find attached my résumé"
print(raw_string_literal)

# Create and print a unicode string literal
unicode_string_literal = u"My name is Jillur Quddus\nI am a Chief Data Scientist and Principal Polyglot Software Engineer. Please find attached my résumé"
print(unicode_string_literal)

'''
6.8,Comparing Strings
- String Comparison: Use comparision operators ('==', '!=', '<', '>', '<=', '>=') to compare
    strings lexicographically on their ASCII values
'''
# Example 6.8
# Compare two strings
individual1_first_name = "Jillur"
individual2_first_name = "jillur"
if individual1_first_name == individual2_first_name:
    print("Both indivuals share the same first name")
elif individual1_first_name.upper() == individual2_first_name.upper():
    print("Both individuals share teh same first name when uppercased")
else:
    print("No name match found")

'''
6.9 String Methods
String methods: Python provides a variety of built-in methods for string maniuplation, such as
 lower(), upper(), strip(), replace(), find(), startswith(), endswith(), split(), and join()
'''
# Example 6.9
# Create a new string literal
my_string = "   Hello! My name is Jillur Quddus and I am a Chief Data Scientist and Principal Polyglot Software Engineer.    "
print(my_string)

# str.lower()
print(my_string.lower())

# str.upper()
print(my_string.upper())

# str.strip()
stripped_string = my_string.strip()
print(stripped_string)

# str.replace('find', 'replacewith')
initialized_string = stripped_string.replace('Jillur', 'J').replace('Quddus', 'Q')
print(initialized_string)

# str.find('substring)
print(initialized_string.find("Data Scientist"))

# str.startswith('substring')
print(initialized_string.startswith('Hello!'))

# str.endswith('substring')
print(initialized_string.endswith("Good Bye!"))

# str.split('delimiter')
print(initialized_string.split('!'))

# delimiter.join([list])
print('|'.join(['Chief Data Scientist', 'Principal Polyglot Software Engineer', "Technical Architect"]))




# Activity 1
full_name = "Brista Lin"
address = "12345 HappyLife Lane"
print(full_name)
print(address)

# Activity 2
quote = "The quick brown fox jumps over the lazy dog."
print(quote[4])
print(quote[4:10])
print(quote[-4:-1])

# Activity 3
sentence = "Did you know that math is math?"
print(len(sentence))

# Activity 4
text = "Caden and Jasper are good friends."
if "friends" in text:
    print("The word friends is in the text!")
else:
    print("The word friends is not in the text.")

# Activity 5
string1 = "Hi there! "
string2 = 'Life is lifing!'
print(string1 + string2)

# Activity 6
legal = "Jillur should come back to make Jasper \"happy\""
print(legal)

# Activity 7
raw = r'Happy!'
unicode = u'Happy!'
print(raw)
print(unicode)

# Activity 8
strin1 = "This is a string"
strin2 = "This is also a string"
if strin1 == strin2:
    print("Strin1 and strin2 are equal!")
else:
    print("Strin1 and strin2 are not equal!")

# Activity 9 
my_string2 = "   Hi there! This is a string that uses double quotation marks!    " #I made it my_string2 because my_string already exists
print(my_string2.lower())
print(my_string.upper())
stripped  = my_string2.strip()
print(stripped)
replaced = stripped.replace("Hi", "Hello")
print(replaced)
if stripped.startswith("Hi"):
    print("stripped starts with \'Hi\'")
else:
    print("stripped doesn't start with \'Hi\'")

if stripped.endswith("marks!"):
    print("stripped ends with \'marks!\'")
else:
    print("stripped doesn't end with \'marks!\'")

listy = stripped.split(" ")
print(listy)

print(" ".join(listy))

