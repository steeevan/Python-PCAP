def is_palindrome(s):
    # Remove any spaces and convert the string to lowercase for case-insensitive comparison
    s = s.replace(" ", "").lower()
    
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Test the function with different strings
test_strings = ["racecar", "madam", "hello", "A man a plan a canal Panama", "no lemon no melon"]

for test in test_strings:
    if is_palindrome(test):
        print(f'"{test}" is a palindrome.')
    else:
        print(f'"{test}" is not a palindrome.')