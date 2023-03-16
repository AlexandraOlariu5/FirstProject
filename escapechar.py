splitString = "This string has been \nsplit over\nseveral\nlines"
print(splitString)

tabbedString = "1\t2\t3\t4\t5"
print(tabbedString)

print('The pet shop owner said "No, no, \'e \'s uh,...he\'s resting".')
#or
print("The pet shop owner said \"No, no, 'e , 's uh,...he's resting\".")

print("""The pet shop owner said "No, no, \
'e , 's uh,...he's resting".""")

anotherSplitString = """This string has been \
split over \
several \
lines."""

print(anotherSplitString)

print("C:\\Users\\timbuchalka\\notes.txt")
print(r"C:\Users\timbuchalka\notes.txt")


x = [12, 564, 652, -12, 5, -13,12330]
y = [112, 135653, 23, 54]
print(max(max(x) , max(y)))

if max(x) > max(y):
    print("max x greater than max y")
else:
    print("FALSE")
import random
number_displayed = random.randint(1,10)
print("Choose a number between 1 & 10 :" , number_displayed)
#number_choosen = random.randint(1,10)
#choice = ["high", "low"]
#for aproximate in choice:

#if aproximate = choice[0]:
   # print("right")
#else:
    #print("left")
# import time
# time.sleep(5)
# for choice in number_displayed:
#  if choice > number_displayed:
#     print("Go to the right")
#  else:
#     print("Go to the left")