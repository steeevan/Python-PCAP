'''

Basic String in python
- create ad manipulate and slicing 
-use string indexing and slicing
-calculate string length
- test string membership
- concatenate strings
- handle escape characters
- user raw and unicode string literals
- compare strings
- utilize various string methods
'''
'''
6.1 Creating strings
-simple strings: String are sequences of characters in python. They can be created by enclosing
    characters in single quotes(') or double quotes(")
- Multiline strings: For strings that span multiple lines, triple quotes(""") or singles are used
'''
#example 6.1 
#create a simple string
first_name='Jillur'
print(first_name)
#create a multiple string

envelope_label=""" Jillur Quddus
1600 Pennsylvanua Ave NW
Washington
DC 20500
United States"""
print(envelope_label)

'''
6.2 Indexing and slicing
- Indexin: Access indoiovidual characters in a string using their position(index) with the first
    character at index 0
-slicing : Extract a substring by specifying a rance of indeces. the syntax is 'string[start:end]
    start is inclusice, and end is exclusive
'''
'''
6.3 String Length
- Length of a string : use the 'len()' function to determine the number of characters in a string,
    includes spaces and punctuation
    
'''
#Example 6.3
# Calculate the length of a string

'''
6.4 String membership
- membership operator: Use the 'in' keywork to check if a substring exists within a string.
    This returns 'true' is the substring is found and 'false' otherwise
'''
lorem_ipsum='gggggg'
#Example 6.4
# Test whether a given of characters can be found in a string
if "tempor" in lorem_ipsum:
    print("The Latin word for tine has been found!")
'''
6.5 concatenatin strings
-string concatenation: Use the '+' operator to join two or more string into a single string.

'''
'''
#Example 6/5
lorem_ipsum_continued="ggghhhhhha"
lorem_ipsum_updated= lorem_ipsum+" "+ lorem_ipsum_continued
print(lorem_ipsum_updated)
'''
'''
6.6 Escape characters
- Escape characters: UUse '\' backslsh to include special characters in a string,
    such as quotes or newlines characters
'''
#Example 6.6 
#Try to create a string containing illgal characters
illegal_string = "My name is Jillur"
#syntax error: invalid syntax
#escape the illegal characters using the backslash character
legal_string="My name is \"jllur\""
print(legal_string)
'''
6.7 Raw and unicode string literals 
-raw strings: prefix a string with 'r' to create a raw string where escape sequences are not processed 
-unicode strings: prefix with a string with 'u' to create a unicode string(necessart for python2)
    but all strings in python 3 are unicode
'''
#ex 6.7
'''
6.8 Comparing strings
- String comparison: Use comparison operators('==','!=','<','>','<=','>=') to compare
    strings lexicogrphically on their AsCII values
'''
#Example 6.8
#compare twp strings
indicidual1_first_name ="Jillur"
indicidual2_first_name= "jillur"
if indicidual1_first_name==indicidual2_first_name:
    print("Both indiciduals share the same first name")
elif indicidual1_first_name.upper()== indicidual1_first_name.upper():
    print("Both individuals share the same first name when uppercased")
else:
    print("no name match found")

'''
6.9 string methods
string methods: python provides a variety of built-in methods for string manipulation, such as lower(), uppper(), strip(), replace(), find(), startswith(),
endswith(), split(), and join().
'''
# ex 6.9
# Create a new string literal
my_string="Hello my name is Jillur quddus and I am a cheif data scientist and priciple"
print(my_string)

# str.lower
print(my_string.lower())

#str.upper()
print(my_string.upper())

#str.strip()
stripped_string = my_string.strip()
print(stripped_string)

#str.replace('find', 'replacewith)
initialized_string=stripped_string.replace('Jillur','J').replace('Quddus','Q')
print(initialized_string)

#str.find('substring')
print(initialized_string.find('Data Scientist'))

#str.startswith('substring')
print(initialized_string.startswith('Hello!'))

#str.endswith('substring')
print(initialized_string.endswith("Good bye!"))

#str.split('delimter')
print(initialized_string.split('!'))

#delimiter.join([list])
print('|'.join(['Chief']))
#activity 1
fullname="Steven"
address="15555 ca"
print(fullname,address)
#activity 2
quote="The quick brown fox jumps over the lazy dog"
print(quote[4])
print(quote[4:10])
print(quote[-1])
#3
x="sssss"
print(len(x))
#4
x="s,s,s,s,s"
if "s" in x:
    print("yes")
#5
x="t"
y="d"
print(x+y)
#6
string_with_quotes = 'He said, "It\'s a beautiful day!"'
print(string_with_quotes)
#7
raw_string = r'This is.'
print(raw_string)
unicode_string = u'This is: \u963A'
print(unicode_string)
#8
string1="x"
string2="y"
strings_are_equal = (string1 == string2)

if strings_are_equal:
    print("The strings are equal.")
else:
    print("The strings are not equal.")

#9
my_string = "  Hello  "

lowercase_string = my_string.lower()
print("Lowercase:", lowercase_string)

uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)

stripped_string = my_string.strip()
print("Stripped:", stripped_string)

replaced_string = my_string.replace("he", "llo")
print("Replaced:", replaced_string)

substring_position = my_string.find("hello")
print("Position of 'hello':", substring_position)

starts_with_hello = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)

ends_with_hello = my_string.endswith("hello.")
print("Ends with 'hello.':", ends_with_hello)

split_string = my_string.split()
print("Split:", split_string)

list_of_strings = ["hello", "and", "he", "are", "yy", "xx."]
joined_string = " ".join(list_of_strings)
print("Joined:", joined_string)