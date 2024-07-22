'''
Basic String in Python
 - Create ad manipulate strings
 - use string indexing and slicing
 - calculate string length
 - test string membership
 - concatenate strings
 - handle escape characters
 - user raw and unicode string literals
 - compare strings
 - utilize various string methods
'''

'''
6.1 Creating Strings
- Simple strings: String are sequences of characters in Python. They can e created by enclosing
     characcters in singl quotes (') or double quotes (")
- Multiline Strings: For strings that span multiple lines, triple quotes (""") or singles are used
'''
# Example 6.1 
# Create a simple string
first_name = 'Jillur'
print(first_name)

# Create a multiline string
envelope_label = """Jillur Quddus
1600 Pennsylvania Ave NW
Washington
DC 20500
United States"""
print(envelope_label)

'''
6.2 Indexing and Slicing
- Indexin: Access individual characters in a string using their position(index) with the first
    character at index 0
- Slicing: Extract a substring by specifying a rance of indeces. The syntax is 'string[start:end]'
    start is inclusive, and end is exclusive
'''
#Example 6.2
# Create a simple string
lorem_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

# Print the 13th character
print(lorem_ipsum[12])

# Print the substring between the 29th and 56th characters
print(lorem_ipsum[28:55])

# Print the last word
print(lorem_ipsum[-7:-1])

'''
6.3 String Length
- Length of a string: use the 'len()' function to determine the number of characters in a string, 
    includes spaces and punctuation
'''
# Example 6.3 
# Calculate the length of a string
print(len(lorem_ipsum))

'''
6.4 String Membership
- Membership Operator: Use the 'in' keyword to check if a substring exists within a string.
    This returns 'True' if the substring is found and 'False' otherwise
'''
# Example 6.4
# Test whether a given sequence of characters can be found in a string
if "tempor" in lorem_ipsum:
    print("The latin word for time has been found!")

'''
6.5 Concatenatin Strings
- String Concatenation: Use the '+' operator to join two or more string into a single string.
'''
# Example 6.5
lorem_ipsum_continued = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
lorem_ipsum_updated = lorem_ipsum + " " + lorem_ipsum_continued
print(lorem_ipsum_updated)

'''
6.6 Escape Characters
- Escape characters: Use '\' backslash to include special characters in a string, 
    such as quotes or newlines characters
'''
# Example 6.6
# Try to create a string containing illegal characters
illegal_string = "My name is Jillur"
# SyntaxError: invalid syntax

# Escape the illegal characters using the backslash character
legal_string = "My name is \"Jillur\""
print(legal_string)

'''
6.7 Raw and Unicode String Literals
- Raw strings: prefix a string with 'r' to create a raw string where escape sequences are not processed
- Unicode strings: Prefix with a string with 'u' to create a unicode string(necessary for Python 2)
    but all string in python 3 are unicode
'''
# Example 6.7
# Create and print a raw string literal
raw_string_literal = r"My name is Jillur Quddus\nI am a Chief Data Scientist and Principal Polyglot Software Engineer. Please find attached my résumé"
print(raw_string_literal)

# Create and print a unicode string literal
unicode_string_literal = u"My name is Jillur Quddus\nI am a Chief Data Scientist and Principal Polyglot Software Engineer. Please find attached my résumé"
print(unicode_string_literal)

'''
6.8 Comparing Strings
- String Comparison: Use comparsion operators ('==', '!=', '<', '>', '<=', '>=') to compare
    strings lexicographically on their ASCII values
'''
#Example 6.8
# Compare two strings
individual1_first_name = "Jillur"
individual2_first_name = "jillur"
if individual1_first_name == individual2_first_name:
    print("Both individuals share the same first name")
elif individual1_first_name.upper() == individual2_first_name.upper():
    print("Both individuals share the same first name when uppercased")
else:
    print("No name match found")

'''
6.9 String Methods
String methods: Python provides a variety of built-in methods for string manipulation, such as
 lower(), upper(), strip(), replace(), find(), startswith(), endswith(), split(), and join().
'''
# Example 6.9
# Create a new string literal
my_string = "    Hello! My name is Jillur Quddus and I am a Chief Data Scientist and Principal Polyglot Software Engineer.    "
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

# str.find('substring')
print(initialized_string.find('Data Scientist'))

# str.startswith('substring')
print(initialized_string.startswith('Hello!'))

# str.endswith('substring')
print(initialized_string.endswith("Good Bye!"))

# str.split('delimiter')
print(initialized_string.split('!'))

# delimiter.join([list])
print('|'.join(['Chief Data Scientist', 'Principal Polyglot Software Engineer', 'Technical Architect']))
