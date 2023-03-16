shopping_list = ["fruits", "eggs","juice", "milk", "bread", "onion", "pork", "pasta"]
item_to_find = "onion"
position = None

# for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         position = index
#         break

if item_to_find in shopping_list:
    position = shopping_list.index(item_to_find)
if position is not None:
    print("Item found at position {}".format(position))
else:
    print("{} not found".format(item_to_find))