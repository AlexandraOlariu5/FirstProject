age = 24
shopping  = "I want to buy : some {} , a few pieces of {} , and a jar of {} ."
item1 = "prawns"
item2 = "salami"
item3 = "jam"

y = (shopping.format(item1 , item2 , item3))
print(y)
txt = "banana"
for x in txt:
    print(x)
print(len(shopping))
print(y.replace("prawns" , "octopus"))
print(y.upper())
print(shopping.lower())
print(y.split(","))
print("In the fridge we have" "{0} ".format(age) , "{0}".format(item1) , "as well as many {0}".format(item2))
print("Attempt number " + str(1))
print()
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31 , "January", "March", "May", "July", "August", "October", "December"))

print("I want to buy {1} and {0} even if you would like {2}".format(item1 , item2 , item3))
print("January : {0} , February : {1} , March : {0}, April : {2}".format(31 , 28 , 30))
print("""January : {0}
February : {1}
March : {0}
April : {2}""".format(31 , 28 , 30))
print(shopping.format(item1, item2, item3))