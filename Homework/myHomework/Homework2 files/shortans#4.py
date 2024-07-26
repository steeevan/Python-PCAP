# 4. "break" in a loop will completey get out of the loop. A "continue" will skip the current iteration and move on to the next one.

# 'break' example:
# This program will only run 5 times because at the 6th time, it will 'break' out of the loop
for i in range(10):
    if i >= 5:
        break
    print("printed!")

# 'continue' example:
# This program will only run 5 times because at the 6th time, it will start to 'continue' and skip the current iteration
for i in range(10):
    if i >= 5:
        continue
    print("printed!")