password = input("Enter your password: ")

if 0 < len(password) < 50:
    print(password, len(password))
else:
    print("Not enough characters")
