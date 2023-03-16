#Write a program to print out all the numbers from 0 to 20 that aren't divisible by either 3 or 5.

# for number in range(21):
#     if number > 0 and number % 3 != 0 and number % 5 != 0:
#         print(number)
for number in range(21): # continue solution
    if number % 3 == 0 or number % 5 == 0: # we use or in this case because we don't want to display numbers divisible by
        # 3 or 5 and both like 6, 10, 15. also, don't forget about double equals. we are not assigning values, we are verifying
        # the equality
        continue
    print(number)# take place of "else" and is part of the for block, not if's