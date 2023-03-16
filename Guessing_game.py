answer = 5

print("Please guess the number 1 and 10 : ")
guess = int(input())
# import random
# statement = random.randint(5, 10)
# print(statement)
# if guess == statement:
#     print("Congrats ! Your guess is right.")
# elif guess == int(statement) - 1:
#     print("Keep going. You're so close !")
#
# else:
#     print("Sorry. Try again")
# print()

# if guess < answer:
#      print("Please guess higher")
#      guess = int(input())
#      if guess == answer:
#          print("Well done, you guessed it.")
#
#      else:
#          print("Sorry, you have guessed incorrectly")
# elif guess > answer:
#      print("Please guess lower")
#      guess = int(input())
#      if guess == answer:
#          print("Well done, you guessed it.")
#      else:
#          print("Sorry, you haven't guessed correctly.")
# else:
#     print("You got it first time")
if guess == answer:
    print("You got it first time.")
else:
        if guess < answer:
            print("Please guess higher.")
        else: # guess must be greater than answer
            print("Please guess lower")
        guess = int(input())
        if guess == answer:
            print("Well done, you guessed it.")
        else:
            print("Sorry, you have not guessed corectly.")