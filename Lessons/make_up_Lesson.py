'''
(12)Functions, (10)Tuples, and (11)Dictionaries
<<<<<<< HEAD
- Understanding the basics of a function
- Explore advacned usages of functions with tuples and dictionaries
- Learn to create, manipulate, and use functions that integrate with tuples and
dictionaries
=======
- Understanding the basics of a funtion
- Explore advanced usages of functions with tuples and dictionaries
- Learn to create, manipulate, and use functions that integrate with tuples
and dictionaries
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''
'''
Intro to Functions
'''
def function_name():
    '''
    Docstring (optional)
    '''
    print("My function is used")

function_name()

<<<<<<< HEAD
# Create a function with parameters
# Here we have x and y as parameters, these are positional parameters
# meaning that when we invocate the function we have 
# to give two arguments
def add(x,y):
    #print(f"x: {x}")
    #print(f"y: {y}")
    return x + y

# Default parameters
def get_name(name="Jillir"):
=======
#print(function_name.__doc__)

# Create a function with parameters
# Here we have x and y as parameters, these are positional parameters
# meaning that when we invocate the function we have to give two arguments
def add(x,y):
    print(f"x: {x}")
    print(f"y: {y}")
    return x + y
print(add(5,7))

# Default parameters
def get_name(name = "Jillir"):
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
    print(name)

get_name()

<<<<<<< HEAD
# keyword arguments
print(add(y = 7, x = 10))

# Lambda functions
add_lambda = lambda x,y: x+y
=======
# Keyword arguments
print(add(y = 7, x = 10))

# Lambda functions
add_lambda = lambda x,y: x+y # lambda is restricted to one line of code.
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
print(add_lambda(2,9))

'''
Tuples
<<<<<<< HEAD

=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
'''
# Returning tuples from functions
def calculate_stats(numbers):
    total = sum(numbers)
    count = len(numbers)
<<<<<<< HEAD
    average = total / count if count != 0 else 0
    return total, count, average
# Call the function
=======
    average = total/count if count!= 0 else 0
    return total, count, average
# Call teh function
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
stats = (10,20,30,40)
my_results = calculate_stats(stats)
print(my_results)

<<<<<<< HEAD
# return a dictionary from a function
=======
# Return a dictionary from a function
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
def analyze_text(text):
    word_count = len(text.split())
    char_count = len(text)
    unique_words = len(set(text.split()))
<<<<<<< HEAD

    return {
        "word_count":word_count,
        "char_count":char_count,
        "unique_words":unique_words
=======
    return {"word_count":word_count,
            "char_count":char_count,
            "unique_words":unique_words
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
    }

text_analysis = analyze_text("Hello world! Hello everyone.")
print(text_analysis)
print(f"The number of words in this string are {text_analysis["word_count"]}")
<<<<<<< HEAD
text_analysis["word_count"] = 5
print(f"The number of words in this string are {text_analysis["word_count"]}")
=======
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4

# Add an item
text_analysis["magic_word"] = "Python"
print(text_analysis)
print(text_analysis["magic_word"])

<<<<<<< HEAD
# delelte items from dictionary
=======
# delete items from dictionary
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
del text_analysis["magic_word"]
print(text_analysis)


def update_inventory(inventory, item_info):
<<<<<<< HEAD
    item, quantatity = item_info
    if item.lower() in inventory:
        inventory[item.lower()] += quantatity
    else:
        inventory[item] = quantatity
    return inventory

# create a dictionary
inventory ={
    "apples":10,
    "oranges":5
}
# call the functio with a tuple
updated_inventory = update_inventory(inventory,("Apples", 10))
=======
    item, quantity = item_info
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity
    return inventory
# create a dictionary
inventory = {
    "apple":10,
    "oranges":5
}
# call the function with a tuple
updated_inventory = update_inventory(inventory,("banana",10))
>>>>>>> 4ad542bb5e7021416ff630f5878ae5b4b817e3e4
print(updated_inventory)