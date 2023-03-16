if 0:
    print("True")
else:
    print("False")# 0 will be always evaluated as False
name = input("Please enter your name: ")
if name:# if we don't type a name, the programm will evaluate to False - the output will be the option we provided for else
    print("Hello, {}".format(name))
else:
    print("Are you the one with no name ?")
# there is another way of writing this one more clearly :
if name != "":# we compare the name with an empty string
    print("Nice to meet you, {}".format(name))
else:
    print("You're indeed the one with no name.")