print("===WELCOME TO THE QUIZ APP ===")
score =0
answer =input("1.what is the capital cityof Tanzania?")
if answer.lower() =="dodoma":
    print("correct!")
    score += 1
else:
    print("wrong!")
answer = input("2. how many days are in a weeks?")
if answer =="7":
    print("correct!")
    score +=1
else:
    print("wrong!")
answer = input("3. what is 5 + 3? ")
if answer =="8":
    print("correct!")
    score += 1
else:
    print("wrong!")
print("\nQuiz Finished!")
print("Your score is:", score)