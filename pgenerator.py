import random

characters ="ABCDEF123456789"

password =""

for 1 in range(6):
    password+=random.choice(characters)
    print("your password is:",password)