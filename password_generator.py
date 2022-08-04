password = input("Enter your password: ")

# Validate password and print
if 0 < len(password) < 50:
    print(password, len(password))
else:
    print("Not enough characters")
