import random
print("🎮 Welcome to guess the number game!")
secret_number = random.randint(1,10)

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print