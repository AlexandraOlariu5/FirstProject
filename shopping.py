shopping_list = ["fruits", "eggs", "bread", "onion", "pork", "pasta"]
# for item in shopping_list:
#     if item != "bread":
#         print("Buy " + item)
# print()
for item2 in shopping_list:
    if item2 == "onion":
       continue
    print("Buy: " + item2)
print()
for item in shopping_list:
    if item == "bread":
        break
    print(item)