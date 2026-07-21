import random

number=random.randint(1,10)

guess =int(input("Guess a number between 1 and 10:"))
if guess ==number:
    print("correct! you win")
else:
    print("wrong! The number was",number)