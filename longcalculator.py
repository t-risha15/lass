import math
print("WELCOME TO MY CALCULATOR")
while True:
    print("\nchoose an operator:")
    print("1.Addittion(+)")
    print("2. substraction(-)")
    print("3. Multiplication (*)")
    print("4. Division(/)")
    print("5. power (^)")
    print("6. square root")
    print("7. modulus (%)")
    print("8 floor division (//)")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice =="9":
        print("Thank you for using my calculator!")
        break

    if choice =="6":
        number = float(input("Enter a number: "))
        print("Answer =", math.sqrt(number))
        continue
    if choice in ["1","2", "3", "4", "5", "6", "7", "8",]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice =="1":
            print("Answer =", num1 + num2)
        elif choice =="2":
            print("Answer =",num1-num2)
        elif choice =="3":
            print("Answer=", num1 *  num2)
        elif choice =="4":
            if num2 !=0:
                print("Answer =", num1 / num2)
            else:
                print("Error! cannot divide by zero.")
        elif choice == "5":
            print("Answer =", num1 ** num2)
        elif choice =="7":
            print("Answer =", num1 % num2)
        elif choice == "8":
            print("Answer =", num1 // num2)
else:
    print("invalid choice! please try again.")