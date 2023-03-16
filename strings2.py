#
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:14:2])
#number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using any separators you like: ")
# separators = number[1::4]
# print(separators)
separators = ""
for char in number:
    if not char.isnumeric():# if char is numeric, the conditions will be evaluated, but with no result, and no value
        # will be displayed, so we're going back to the for line
        separators = separators + char
#print(separators)

# if print would be added in the if block, we would had memorised the first value for char and continously
#adding a new one till the last one (when the program stops).
# in this way, when print is on the for block, we obtain a sequence formed by the values of char.


values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
print(number[-12:-2:2])