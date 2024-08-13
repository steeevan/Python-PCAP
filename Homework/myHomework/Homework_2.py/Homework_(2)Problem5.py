# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).

def palindrome(s):
    return s == s[::-1]
print(palindrome("racecar"))