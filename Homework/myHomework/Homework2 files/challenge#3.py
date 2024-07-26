# 3:
for i in range(3):
    password_attempt = input("Password please: ")
    if password_attempt == 'thisisverysecure':
        print('Access Granted')
        break
else:
    print('Access Denied')
# This checks if the password is correct 3 times by using a for loop.
# If they are al wrong, it will say access denied.
# If it is correct, it will say access granted and break out of the loop