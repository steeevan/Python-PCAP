# Problem 1: Explain the difference between a for loop and a while loop. Provide an example where each would be appropriate to use.
'''
A while loop repeatedly executes a block of code as long as a specified condition is true

A for loop iterates over a sequence (tuple, lists, strings, dictionaries) and executes
a block of code for each element
'''
sigma_counter = 1
list = []
while sigma_counter < 10:
    list.append('What the sigma.')
    sigma_counter+=1
print(list)

hi = ["hello", "sigma", "skibidi"]
for i in hi:
    print(f"{i}: {len(i)}")