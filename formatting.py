for i in range(1, 13): # 'i' will take values from 1 to 12 (13 is not included)
   print(" No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # adding the allocated space for each value : 2/4/4 spaces
print()
x = "abcdefghijklmnopqrstuvwxyz"
print(x[25:0:-1])# this will print the alphabet inverted , but without the 'a'. specifying the end , the last digit will not be inlcluded.
# for the alphabet inverted , with 'a' :
print(x[25::-1]) #or
print(x[::-1])# there's no need the specify the first letter either
print()
for i in range(1, 13):
   print(" No. {0:2} squared is {1:<4} and cubed is {2:^4}".format(i, i ** 2, i ** 3))
print()

for i in range(1 , 10):
   print("No. {:2} squared is {:<3} and doubled is {:^2}".format(i , i**2 , i * 2))
print()
print("The pi number equals {0:}".format(22/7))# this shows the width default : 15 digits precision after the floating point
print("The pi number equals {0:12f}".format(22/7))# shows the default of 6 digits precision
print("The pi number equals {0:12.50f}".format(22/7))# python doesn't truncate . It ignores the width of 12.
print("The pi number equals {0:52.50f}".format(22/7))# there's no space before our number even if 52>50 just because the all number has exactly 52 digits so
# all places specified in the width are already filled.
print("The pi number equals {0:62.50f}".format(22/7))
print("The pi number equals {0:72.50f}".format(22/7))# 72 is > 50 and the number will be aligned to the right
print("The pi number equals {0:<72.54f}".format(22/7))# the highest precision in python is of 51 to 53 digits , that's why we got the "000"
print()
personal_data = "My name is {myname} and I am {years} years old."
print(personal_data.format(myname = "Alexandra" , years = 19 ))# we can identify placeholders by giving them names
print("The pi number equals {:10.4f}".format(22/7))
print("I'll pay only {:7.3f} pounds for this product.".format(round(7/3))) # adding 7. we add 7-4 spaces before our number . The number for spaces
# must be > the number of our precision digits.
print("Five divided by five more precisely is {:4f}".format(5/5))# adding "f" we get the floating number point with a precision of 6 , which is the default
print("The pi number equals {:30.5f}".format(22/7))
print("The pi number equals {:f}".format(22/7))
print("The pi number equals {:30}".format(22/7))
print("This will show us the number '20' converted to binary : {:b}".format(20))
print("this is how to use an undescore as a thousand separator {:_}".format(100000000))
print("Print the percentage with no decimal places {:.0%}".format(0.8))
print("Use  a plus sign to indicate if the result is negative or positive {:+}".format(-3 * 4))
print("Use the equal to for placing the sign to the left most position.{:=8}".format(-4))
print()
print("The pi number equals {:12.8f}".format(22/7))