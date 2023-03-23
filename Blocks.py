for i in range(1 , 13):
    print("No. {:<2} squared is {:<3} and cubed is {:<4}".format(i , i**2 , i**3))
    print("*" * 40)
    print(i)
print()
name = input("Please enter your name: ")
age = int(input("How old are you , {}? ".format(name)))

print()
if age >= 18:
    print("You are old enough to vote.")
    print("Please put an X in the box.")
else:
    print("Please come back in {} years .".format(18 - age))
if age < 18:
    print("Please come back in {} years .".format(18 - age))
elif age == 300:
    print(f"Sorry,{name}, you don't pass to next level.")
# elif age == 30:
#     import random
#     print(random.randint(1, 5))
else:
    print("You are old enough to vote.")
    print("Please put an X in the box.")