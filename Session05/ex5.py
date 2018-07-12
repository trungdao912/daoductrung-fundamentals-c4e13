price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

total = 0

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for item in price:
    print(item)
    print("price:{0}".format(price[item]))
    print("stock:{0}".format(stock[item]))
    print("\n")

for item2 in price:
    cost = price[item2] * stock[item2]
    total = total + cost
print("total:", total)