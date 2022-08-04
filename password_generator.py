import random

password = ""

for i in range(10):
    password += str(random.randint(0, 9))

print(password, len(password))
