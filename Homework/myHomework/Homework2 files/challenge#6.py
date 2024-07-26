# 6:
stringy = "This has lots of vowels in it!"
def check_vowels(strinnn):
    As = 0
    Es = 0
    Is = 0
    Os = 0
    Us = 0
    for i in range(len(strinnn)):
        if strinnn[i] == "a" or strinnn[i] == "A":
            As +=1
        elif strinnn[i] == "E" or strinnn[i] == "e":
            Es +=1
        elif strinnn[i] == "i" or strinnn[i] == "I":
            Is +=1
        elif strinnn[i] == "O" or strinnn[i] == "o":
            Os +=1
        elif strinnn[i] == "U" or strinnn[i] == "u":
            Us +=1
    print(f"This string has {As} a's, {Es} e's, {Is} i's, {Os} o's, and {Us} u's!")
check_vowels(stringy)

# This program iterates through the string by using a for loop and checks for a vowel. If it finds one, it adds 1 to the corresponding variable
# Once it's done, it uses a formatted string to print how many of each vowel it found.