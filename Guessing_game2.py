import random # import the random module from python built-in library

highest = 10
answer = random.randint(1, highest) # we separate the module from the function by the dot notation. ten is included in this range
print(answer) #TODO: Remove after testing

print("Please guess between 1 and {}.".format(highest))
guess = int(input())
if guess == answer:
    print("You got it  first time !")
else:
    if guess < answer:
         print("Please get higher")
    else :
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you finally guessed it !")
    else:
         print("Sorry, you have not guessed corectly .")
print(f"The answer is : {answer}")