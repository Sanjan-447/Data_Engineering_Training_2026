import json
with open("orders.json", "r") as file:
     data=json.load(file)

orders= data["orders"]

for order in orders:
    print(order)

total_rev=0
for order in orders:
    total_rev+=order["amount"]
print("Total Revenue: ", total_rev)

spend={}
for order in orders:
   customer=order["customer"]
   amount=order["amount"]
   if customer in spend:
       spend[customer] += amount
   else:
       spend[customer] = amount
print("Total spending per customer: ")
print(spend)

highest=max(spend, key=spend.get)
print("Highest spending customer: ", highest)

total_order={}
for order in orders:
    name=order["customer"]
    if name in total_order:
         total_order[name]+=1
    else:
         total_order[name]=1
print("Total order per customer: ")
print(total_order)