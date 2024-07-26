# 2:
# This program checks if a character is in a string by iterating through the string and checking each letter
def check_in_string(strin,character):
    counter = 0
    for i in range(len(strin)):
        if strin[i] == character:
            counter += 1
        else:
            continue
    return counter