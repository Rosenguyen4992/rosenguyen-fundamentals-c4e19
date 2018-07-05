name = input("Your name is: ")
print ("Your full name: {0}".format(name))

danhsach = list(name.title())
danhsach_cha = []

for index, item in enumerate (danhsach):
    if item == " ":
        if danhsach[index+1] != " ":
            danhsach_cha.append(item)
    else:
        danhsach_cha.append(item)

update_name = ''.join(danhsach_cha)

print ("Update name: {0}".format(update_name))