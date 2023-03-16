#Binary search
low = 1
high = 1000
print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

guesses = 1
answer_found = False
while not answer_found: # we can't have something like 'while guess != answer', because we don't know the answer
    # True is always True, so our loop goes forever
    print("\tGuessing in the range of {} to {}".format(low, high))
    guess = low + (high - low) // 2 # calculate the midpoint  between the lowest and the highest value
    high_low = input("My guess is {}. Should I guess higher or lower ? "
                     "Enter h or l, or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        low = guess + 1
         # Guess higher. The low end of the range becomes 1 greater than the guess.
    elif high_low == "l":
        high = guess - 1
         # Guess lower. The high end of the range becomes one less than the guess.
    elif high_low == "c":
        print("I got it in {} guesses!".format(guesses))
        answer_found = True
    else:
        print("Please enter h, l or c.")

    guesses = guesses + 1