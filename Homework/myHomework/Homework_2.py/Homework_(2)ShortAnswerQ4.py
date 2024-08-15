# Problem 4: Explain what the break and continue statements do in a loop. Provide an example of each.

# The continue statement skips the rest of the code inside the current iteration while the break statement skips through the entire loop

num = [1,2,3,4,5,6]

for n in num:
    if n > 5:
        print(f"First number greater than 5: {n}")
        break


for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)