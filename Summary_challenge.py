
choice = "-"
while True:

    if choice == "0":
        break
    elif choice in "12345":
        print(f"You chose {choice}")
    else:
        print("Please choose one of the following options: ")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tLearn C++")
        print("4.\tGo swimming")
        print("5.\tRead a book")
        print("6.\tJoin a cooking club")
        print("0.\tExit")

    choice = input()