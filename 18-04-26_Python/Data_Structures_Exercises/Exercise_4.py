inventory = {
"laptop":10,
"mouse":25,
"keyboard":15
}

inventory["monitor"] = 8
print(inventory)

inventory["laptop"] -=2
print(inventory)

for item,stock in inventory.items():
    if stock < 10:
        print(item, " : ", stock)
        