correct_password = "securepassword"
for attempt in range(1, 4):
    password = input(f"Attempt {attempt}: Please enter your password: ")
    if password == correct_password:
        print("Access Granted")
        break
else:
    print("Access Denied")