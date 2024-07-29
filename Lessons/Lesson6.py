'''
Basic Strings in Python
- Create and manipulate strings
- Use string indexing and slicing
- Calculate string length
- Test string membership
- Concatenate strings
- Handle escape characters
- Use raw and unicode string literals
- Compare strings
- Utilize various string methods
'''

'''
6.1 Creating Strings
- Simple strings: Strings are sequences of characters in Python. They can be created by enclosing 
    characters in single quotes (') or double quotes (")
- Multiline Strings: For strings that span multiple lines, use triple quotes (""") or single three single quotes
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
- Indexing: Access individual characters in a string using their position(index) with the first charater at index 9
- Slicing: Extract a substring by specifying a range of indeces. The syntax is 'string[start:end]'
    start is inclusive, and end is exclusive
'''

# Example 6.2
# Create a simple string 
lorem_ipsum = "MMMM MMMMMMMMMMMM MMMMMMMMMMMMMMMMMM MMMMMMMMMM MMMMMMMM MMMMMMMM MMMMMMMMm mmmmmmm mmmmmmmmmmm mmmmmm mmmmmmmm"

# Print the 13th character
print(lorem_ipsum[12])

# Print the substring between the 29th and the 58th characters
print(lorem_ipsum[28:55])

# print the last word
print(lorem_ipsum[-7:-1 ])

'''
6.3 String Length
- Length of a string: Use the 'len()' function to determine the number if characters in a string,
    includes spaces and punctuation
'''
# Example 6.3
# Calculate the length of a string
print(len(lorem_ipsum))

'''
6.4 String Membership
- Membership Operator: Uses the 'in' keyword to check of a substring exists within a string.
    this returns 'True' if the substring is found and 'False' otherwise.
'''
# Example 6.4
# Test whether a given sequence of characters can be found in a string
if "MMMMMMMM" in lorem_ipsum:
    print("The latin word for yummy has been found!")

'''
6.5 Concatenation Strings
- String Concatenation: Uses the '+' operator to join two or more strinf in to a single string.
'''
# Example 6.5
lorem_ipsum_continued = "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
lorem_ipsum_updated = lorem_ipsum + " " + lorem_ipsum_continued
# print(lorem_ipusm_updated)

'''
6.6 Escape Characters
- Escape Characters: Uses '\' the backslash to include special characters in a string,
    such as quotes or newlines characters
'''
# Example 6.6
# Try to create a string containing illegal characters
# illegal_string = "My name is "Jillur""
# SyntaxError: invalid syntax

# Escape the illegal characters using the backslsh character
legal_string = "My name is \"Jiller\""
print(legal_string)

'''
6.7 Raw and Unicode String Literals
- Raw strings: Prefix a string with 'r' to create a raw string where escape sequences are not processed
- Unicode strings: Prefix with a string with 'u' to create a unicode strinf(necessary for Python 2)
    but all strings in Python 3 are unicode
'''
# Example 6.7
# Create and print a raw string literal
raw_string_literal = r"My name is Jiller Quddus\nI am a Chief Data Scientist and Principal Polygot Siftware Engineer. Please find attached my resume"
print(raw_string_literal)

# Create and print a unicode stirnf literal
unicode_string_literal = u"My name is Jillur Quddus\nI YAP ALL THE TIME"
print(unicode_string_literal)

'''
6.8 Comparing Strings
- String Comparison: Uses comparison operators ('==', '!=', '<', '>', '<=', '>=') to compare 
    strings lexicograpgically on their ASCII values
'''
# Example 6.8
# Compare 2 strings
individual1_first_name = "Jillur"
individual2_first_name = "jillur"
if individual1_first_name == individual2_first_name:
    print("Both individuals share the same first name")
elif individual1_first_name.upper() == individual2_first_name.upper():
    print("Bother individuals share the same first name when uppercased")
else:
    print("No name match found")

'''
6.9 String Methods
String Methods: Python provides a variety of built-in methods for string manipulation, such as
lower(), upper(), strip(), replace(), find(), startswith(), endswith(), split(), and join().
'''
# Example 6.9
# Create a new string literal
my_string = "   Hello! My name is Jillur Quddus and I am a certified yapper.    "
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
print(initialized_string.find('yapper'))

# str.startswith('substring)
print(initialized_string.startswith("Hello!"))

# str.endswith('substring')
print(initialized_string.endswith("Good Bye!"))

# str.split('delimiter')
print(initialized_string.split('!'))

# delimiter.join([list])
print('|'.join(['yappasaurus', 'mega yapper', 'omega yapper']))


# Activity 1
full_name = "Caden"
address = "1234567 ooga dr."
print(f'I am {full_name} and i in in {address}')

# Activity 2
quote = "The quick brown fox jumps over the lazy dog."
print(quote[4])
print(quote[5:11])
print(quote[-5:-1])

# Activity 3
sentence = "a b c d e f g h i j k l m n o p q r s t u v w x y z "
print(len(sentence))

# Activity 4
text = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20"
if "15" in text:
    print("Hooray")

# Activity 5
string1 = "Ooga"
string2 = "Booga"
string3 = string1 + " " + string2
print(string3)

# Activity 6
n = "Jillur and Jasper sittong on a '\"tree\"'"
print(n)

# Activity 7 
raw_string = r"Caveman\nOoga Booga"
print(raw_string)
unicode_string = u"Caveman\nOoga Booga"
print(unicode_string)

# Activity 8
string1 = "Skibidi"
string2 = "skibidi"
if string1 == string2:
    print('YAY')
else:
    print("nuh uh")

# Activity 9
my_string = "We are venom".lower()
print(my_string)
my_string = "we are venom".upper()
print(my_string)