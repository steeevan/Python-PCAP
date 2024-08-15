'''
16 I/O Basics and Exception Handling
By the end of this lesson, students will be able to:

- Understand the basics of input and output (I/O) in Python.
- Open, read, and write to files.
- ifferentiate between binary and text files.
- Use bytearray objects and their associated methods.
- Understand and implement exception handling using try-except-else-finally blocks.
- Recognize predefined exceptions and their hierarchies.
- Use assertions and understand the anatomy of an exception object.
'''
'''
16.1 Opening Files
Files are opened using the 'open()' function. This function returns a file object, which provides
methods and attributes to interact with file content
-'r' : Read mode (default). OPens the file for reading
- 'w': Write mode. Opens file for writing ( creates a new file or truncates an existing file)
- 'a': append mode. opens the file for writing, appending to the end of the file
- 'b': binary mode. USed in conjuction with other modes to open the file in binary mode
'''
# examples with non-existent files

# Opens in reading mode
#myfile = open('example.txt', 'r')

# Open a file in write mode ( this will create the file)
#myfile = open('example.txt','w')


# Open a file in append mode
#myfile = open('eaxmple.txt','a')

# open a file in binary mode
#myfile = open('example.txt','rb')

# Open a file named Example1.txt
try:
    file = open(r'Lessons\myfiles\Example1.txt','r')
    print("File was opened!")
    content = file.read()
    print(content)
except:
    print("File did not open")

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
TO read a file line by line you can use the readline() method or iterate over the file object directly
'''

with open(r'Lessons\myfiles\Example1.txt','r') as file:
    line = file.readline()
    print(line)
    line = file.readline()
    print(line)

    file.close()

with open(r'Lessons\myfiles\Example1.txt','r') as file:
    line = file.readline()
    while line:
        print(line)
        line = file.readline()
        print(".")
    file.close()

with open(r'Lessons\myfiles\Example1.txt','r') as file:
    for line in file:
        print(line)
    file.close()

# read all line
with open(r'Lessons\myfiles\Example1.txt','r') as file:
    lines = file.readlines()
    print(lines)
    file.close()

'''
16.3 Writing to files 
to write to files we use the write() method
'''
with open(r'Lessons\myfiles\deadpool.txt','w') as file:
    file.write("Hello my name is Deadpool. I am finally in a text file . . .")

    file.close()

lines = ["First line\n", "Second Line\n","Third Line\n"]
with open(r'Lessons\myfiles\deadpool.txt','w') as file:
    file.writelines(lines)
    file.close()

# append to the same file
with open(r'Lessons\myfiles\deadpool.txt','a') as file:
    file.write("This is my fourth line\n")
    file.close()

'''
16.4 Reading and Writing Binary files
Binary files (images, videos)
'''
with open(r'Lessons\myfiles\download (1).jpg','rb') as file:
   binary_file = bytearray(file.read())
   white = b'\x00\x00\x00'
   red = b'xff\x00\x00'

   binary_data = binary_file.replace(white,red)

file.close()




from PIL import Image
# open the jpeg mimage
img = Image.open(r'Lessons\myfiles\download (1).jpg')

# conver the image to rgb mode if its not already
img = img.convert('RGB')

piels = img.load()

width,height = img.size

for i in range(width):
    for j in range(height):
        if piels[i,j] == (255,255,255):
            piels[i,j] = (255,0,0)
        

img.save(r'Lessons\myfiles\download (2).jpg')