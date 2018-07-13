price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3

}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15

}

total = 0

for k_p, v_p in price.items():
    print(k_p)
    print("Price: ", price[k_p])
    print("Stock: ", stock[k_p])
    print()
    total += price[k_p]*stock[k_p]

print("Total money you will make is: ", total)