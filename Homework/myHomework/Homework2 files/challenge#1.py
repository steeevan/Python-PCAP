'''
1:
(I wasn't sure if I should include 50, so I decided to include it.)
'''
# This adds up the even numbers between 1 and 50. It does this by using a while loop to regulate a counter that doesn't go above 51.
# It then checks the counter to see if it's even. If it is, it adds it to the sum. If not, it continues on.
counter2 = 0
sum = 0
while counter2 < 51:
    if counter2 % 2 == 0:
        sum += counter2
        counter2 +=1
    else:
        counter2+=1