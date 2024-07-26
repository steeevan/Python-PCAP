# 3. A nested loop is a loop inside a loop. Every time the outer loop is run, the inner loop fully runs. For example:
# This program will run a loop of 2 10 times, making it a nested loop, and making it print a total of 20 times.
for i in range(10):
    for i in range(2):
        print("This should print 20 times because its in a nested loop!")