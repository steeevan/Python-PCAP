# Write a function that checks if a given string is a palindrome (reads the same forwards and backwards).

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

print(is_palindrome("Racecar"))
print(is_palindrome("Hello"))
