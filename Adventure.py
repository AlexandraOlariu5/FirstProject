available_exits = ["north", "south", "east", "west"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose an exit : ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
else:
    print("Aren't you happy you escaped from there ?")