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
        # print(row)
print("Orders list: ",orders)

products=[]
with open("products.json","r") as file:
    data=json.load(file)

products=data["products"]

product_dict = {}
for p in products:
    product_dict[p["product_id"]] = {"name": p["name"], "price": p["price"]}

print("Product price in dictionary:")
print(product_dict)

with open("website_visits.txt", "r") as file:
    visitors = file.read().splitlines()

unique_visitors = set(visitors)

print("\nUnique Visitors Set:")
print(unique_visitors)

rev_prod={}
for ord in orders:
    prod_id=ord["product_id"]
    name=product_dict[prod_id]["name"]
    price=product_dict[prod_id]["price"]
    
    revenue=ord["quantity"] * price

    if name not in rev_prod:
        rev_prod[name]=revenue
    else:
        rev_prod[name]+=revenue
    
rev_prod_tuples=[]
for name, revenue in rev_prod.items():
    rev_prod_tuples.append((name,revenue))

print("\n Tuples:")
print(rev_prod_tuples)
