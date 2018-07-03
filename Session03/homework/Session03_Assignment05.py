shop = ["T-shirt", "Sweater"]

action = input("Welcome to our shop, what do you want (C, R, U, D)? ")

if action == "r" or action == "R":
    print("Our items: ", end = "")
    print (*shop, sep = ", ")
elif action == "c" or action == "C":
    new_item = input ("Enter new item: ")
    shop.append (new_item)
    print("Our items: ", end = "")
    print (*shop, sep = ", ")
elif action == "U" or action == "u":
    update_item = int(input("Update position? "))
    update_item_name = input("New item? ")
    shop[update_item - 1] = update_item_name
    print("Our items: ", end = "")
    print (*shop, sep = ", ")
elif action == "d" or action == "D":
    del_item = int(input("Delete position? "))
    del shop[del_item - 1]
    print("Our items: ", end = "")
    print (*shop, sep = ", ")
else:
    print("Sorry, wrong action :(")

