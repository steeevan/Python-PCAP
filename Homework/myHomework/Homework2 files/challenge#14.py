# 14:
def rand_num(n,num1,num2):
    import random
    list3 = []
    for i in range(n):
        list3.append(random.randint(num1,num2))
    return list3
print(rand_num(10,1,100))

# This program works by using the random module. It accepts 3 parameters, the amount of random numbers, the smallest number,
# and the biggest number allowed. It then uses a loop to generate the numbers and append them to a list.
# This list is returned after.