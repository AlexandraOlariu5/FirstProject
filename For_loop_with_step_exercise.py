for i in range(100):
    if i % 7 == 0:
        print("{}".format(i))
print("*" * 10)# this method uses a step value
for i in range(0, 101, 7):
    print(i)
print("*" * 10)
for i in range(100)[::7]:# using the slice method
    print(i)