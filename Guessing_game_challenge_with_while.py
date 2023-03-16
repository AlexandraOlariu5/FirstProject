import random

highest = 10
answer = random.randint(1, highest)
print(answer)


print(f"Please guess a number between 1 and {highest}.")
guess = int(input())
while guess != answer:
    if guess < answer and guess != 0:
        print("Please guess higher.")
    elif guess == 0:
        print("You may quit")
    else:
        print("Please guess lower.")
    guess = int(input())
print("Well done !")