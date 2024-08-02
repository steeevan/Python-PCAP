def count_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    vowel_count = 0
    for char in s.lower():
        if char in vowels:
            vowel_count += 1
    return vowel_count
test_strings = ["Hello", "ola", "hi", "one"]

for test in test_strings:
    print(f'Number of vowels in "{test}":', count_vowels(test))