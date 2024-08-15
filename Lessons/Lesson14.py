'''
16 I/O Basics and Exception Handling
- Understand the basics of input and output from files
- Open, read, and write to files
- Differentaite betweem binary and text files
- USe 'bytearray' objects and their methods
- UNderstand and implement exception handling 'try-except-else-finally' blocks
- Recognize predefined exceptions and their heirchy
- Use assertion and understand the anamtomy of an exception object
- Apply concepts required for the PCAP exam
'''

'''
16.1 I/O Basics
Opening Files mean creating a connection between the file and a file object in python.
THi is done using the 'open()' function
keywords:
'open()' : funciton to open a file
'mode': specifies the mode in which the file is opened

-'r' : Read mode (default). OPens the file for reading
- 'w': Write mode. Opens file for writing ( creates a new file or truncates an existing file)
- 'a': append mode. opens the file for writing, appending to the end of the file
- 'b': binary mode. USed in conjuction with other modes to open the file in binary mode
'''

# Examples with non-existent file

# Open a file in read mode
#myfile = open('example.txt','r')

# open a file in write mode ( this will create the file)
#myfile = open('example.txt','w')

# open file in append mode
#myfile = open('example.txt','a')

# open file in binary mode
##myfile = open('example.txt','rb')
#content = myfile.read()
#print(content)

# Open a file named book1.txt and read its contents
try:

    file = open(r'Lessons\myfiles\book1.txt','r')
    print("FIle was open successfully")
except:
    print("File did not open")

content = file.read()
#print(content)
file.close()

'''
read(size): Reads the entire file or specified number of bytes.
readline(): Reads one line from the file.
readlines(): Reads all lines and returns a list.
write(string): Writes a string to the file.
writelines(lines): Writes a list of strings to the file.
close(): Closes the file.
'''
'''
16.2 Reading the file line by line
To read a file line by line you can se the readline() method or iterate over the
file object directly
'''
with open(r'Lessons\myfiles\book1.txt','r') as file:
    line = file.readline()
    print(line)
    while line:
        line = file.readline()
        print(line)
        #words = line.split()
        #print(words)
    file.close()

# for loop
with open(r'Lessons\myfiles\book1.txt','r') as file:
    for line in file:
        print(line)
    file.close

# Read all lines into a list
with open(r'Lessons\myfiles\book1.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
    file.close()

'''
16.3 Writing to files
TO write a string to a file use the 'write()' method
'''
with open(r'Lessons\myfiles\output.txt','w') as file:
    file.write("Hello world!\n Mr.E . . . . .")
    file.close()

# write multiple lins
lines = ["First line\n","Second line\n","THird line\n"]
with open(r'Lessons\myfiles\output.txt','w') as file:
    file.writelines(lines)
    file.close()


# append to the same file output.txt
with open(r'Lessons\myfiles\output.txt','a') as file:
    file.write("This is an appended line\n")
    file.close()


'''
16.4 Reading and Writing binarry files
Binary files (e.g images,videos)
'''
print()
with open(r'Lessons\myfiles\python_logo.jpg','rb') as file:
    content = file.read()
    print(content)
    file.close()
    
with open(r'Lessons\myfiles\python_logo2.jpg','wb') as myfile:
    # convert the binary data to a mutable bytearray
    data = bytearray(content)
    #white = bytes([255,255,255])
    #red = bytes([255,0,0])
    
    # replace all occurences of white with red
    #data = data.replace(white,red)

    myfile.write(content)
    myfile.close()

# counting the number of words in file
with open(r'Lessons\myfiles\output.txt','r') as file:
    content = file.read()
    words = content.split()
    word_count = len(words)
    print(f"Word count: {word_count}")
    file.close()

# Count the occurrences of a specific word
with open(r'Lessons\myfiles\output.txt','r') as file:
    content = file.read()
    words = content.split()
    specific_word = "line"
    specific_word_count = words.count(specific_word)
    print(f"{specific_word} count : {specific_word_count}")
    file.close()

# Count the number of lines
with open(r'Lessons\myfiles\output.txt','r') as file:
    lines = file.readlines()
    line_count = len(lines)
    print(f"Line count: {line_count}")
    file.close()



'''
16.5 Bytearray objects
A bytearray is a mutable sequence of bytes which can be used to manipulate bunary data

bytearray(): Function to create a bytearray object.
append(x): Appends a single byte to the end of the bytearray.
extend(iterable): Appends elements from the iterable to the end of the bytearray.
'''

# Creata a byte array
ba = bytearray([65,66,67,68])
print(ba)

# Modifying a bytearray
ba[1] = 98
print(ba)

# convert to bytes
b = bytes(ba)
print(b)
# bytearray methods
ba.append(69)
print(ba)

ba.extend([70,71])
print(ba)

# write binary files and read using byteobjects
with open(r'Lessons\myfiles\mybinary.bin','wb') as file:
    file.write(b'\x00\x01\x02\x03\x04\x05')
    file.close()


with open(r'Lessons\myfiles\mybinary.bin','rb') as file:
    content = file.read()
    print(content)

    ascii_string = content.decode('ascii',errors='ignore')
    print(ascii_string)
    hex_rep = content.hex()
    print(hex_rep)
    file.close()

'''
16.6 Advanced File operations
File positioning refers to moving the file cursor to a specific location in the file

seek(offset, whence): Moves the file cursor to a specific location.
offset: Number of bytes to move.
whence: Reference point (0 for beginning, 1 for current, 2 for end).
'''
with open(r'Lessons\myfiles\output.txt','r') as file:
    #Move the cursor to the 5th byte from the beginnning
    file.seek(10,0)
    

    # Move the cursor 10 bytes from the current position
    file.seek(10, 1)

    # Move the cursor to 5 bytes before the end
    file.seek(-5, 2)
    
    conentent = file.read()
    print(conentent)
    file.close()

'''
If you try to seek beyond the end of the file, seek() 
will place the cursor at the end of the file. Subsequent reads will return an empty string.

If you try to seek before the beginning of the file (using a negative offset from the beginning),
 seek() will place the cursor at the start of the file.

seek() is often used with tell() to save and restore positions within a file. tell() returns 
the current file position, which you can later use with seek() to return to that position.
'''