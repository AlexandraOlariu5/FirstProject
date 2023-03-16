name = input("Please enter your name : ")
print(f"Hello, {name}.")
age = int(input("How old are you ?"))

if 18 <= age < 31:
    print("You have the right age , {} . Welcome to the holiday".format(name))
else:
    print("We are sorry, {},  you can't go on the holiday.".format(name))