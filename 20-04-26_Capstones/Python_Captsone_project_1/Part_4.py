import json
import csv

orders=[]
with open("orders.csv","r") as file:
    reader=csv.DictReader(file)
    
    for row in reader:
        row["order_id"]=int(row["order_id"])
        row["product_id"]=int(row["product_id"])
        row["quantity"]=int(row["quantity"])
        orders.append(row)
        print(row)

products=[]
with open("products.json","r") as file:
    data=json.load(file)

products=data["products"]

product_dict = {}
for p in products:
    product_dict[p["product_id"]] = {"name": p["name"], "price": p["price"]}

#Task-16
rev={}
print("Revenue for each order")
for ord in orders:
    ord_id=ord["order_id"]
    prod_id=ord["product_id"]
    quantity=ord["quantity"]
    price=product_dict[prod_id]["price"]

    revenue= quantity * price
    ord["revenue"] = revenue
    if ord_id not in ord:
        rev[ord_id]=revenue
    else:
        rev[ord_id]+=revenue
print(rev)

#Task-17
total=0
for values in rev.values():
    total+=values
print("Total revenue: ",total)

#Task-18
print("Total rev for each product:")
rev_prod={}
for ord in orders:
    
    prod_id=ord["product_id"]
    name=product_dict[prod_id]["name"]
    revenue=ord["revenue"]

    if name not in rev_prod:
        rev_prod[name]=revenue

    else:
        rev_prod[name]+=revenue
print(rev_prod)

#task-19
highest=max(rev_prod, key=rev_prod.get)
print("Highest selling product: ",highest)
