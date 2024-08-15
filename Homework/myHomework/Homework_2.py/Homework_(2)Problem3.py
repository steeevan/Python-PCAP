# Write a program that allows a user to input a password up to three times. 
# If the correct password is entered, print "Access Granted". If all three attempts are wrong, print "Access Denied".

correct = "Magikid123"

for attempt in range(3):
    guess = input("Enter the password: ")
    if guess == correct:
        print("Access Granted")
        break
    else:
        print("Incorrect password. Please try again.")
else:
    print("Access Denied")