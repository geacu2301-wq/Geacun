correct_user = "python"
correct_pass = "rules"
tries = 0
while tries < 5:
    user = input("Username: ")
    password = input("Password: ")
    if user == correct_user and password == correct_pass:
        print("Welcome")
        break
    else:
        tries += 1
if tries == 5:
    print("Access denied")
