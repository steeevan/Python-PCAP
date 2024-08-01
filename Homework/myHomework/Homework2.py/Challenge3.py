# Write a program that allows a user to input a password up to three times.
# If the correct password is entered, print "Access Granted".
# If all three attempts are wrong, print "Access Denied".

correct_password = "secret"
max_attempts = 3
for attempt in range(max_attempts):
    user_input = input("Enter password: ")

    if user_input == correct_password:
        print("Access Granted")
        break
    else:
        print("Access Denied")
