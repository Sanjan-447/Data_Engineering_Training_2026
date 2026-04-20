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

products=[]
with open("products.json","r") as file:
    data=json.load(file)

products=data["products"]

product_dict = {}
for p in products:
    product_dict[p["product_id"]] = {"name": p["name"], "price": p["price"]}

# print(product_dict)

for ord in orders:
    ord_id=ord["order_id"]
    prod_id=ord["product_id"]
    quantity=ord["quantity"]
    price=product_dict[prod_id]["price"]

    revenue= quantity * price
    ord["revenue"] = revenue

#Task-20
spend_cust={}
for ord in orders:
    
    customer=ord["customer"]
    revenue=ord["revenue"]

    if customer not in spend_cust:
        spend_cust[customer]=revenue
    else:
        spend_cust[customer]+=revenue
print("Total spending per customer:")
print(spend_cust)

#Task-21
highest=max(spend_cust, key=spend_cust.get)
print("Highest spending customer: ",highest)

#Task-22
print("Customers who spend more than 50000:")
for name,price in spend_cust.items():
    if price > 50000:
        print(name)

