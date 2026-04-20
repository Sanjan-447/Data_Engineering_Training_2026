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

products=[]
with open("products.json","r") as file:
    data=json.load(file)
products=data["products"]

product_dict = {}
for p in products:
    product_dict[p["product_id"]] = {"name": p["name"], "price": p["price"]}

with open("website_visits.txt","r") as file:
    visit=file.read().splitlines()

total_visits=len(visit)
unique_visit=len(set(visit))

rev_prod={}
total_rev=0

for ord in orders:
    prod_id=ord["product_id"]
    name=product_dict[prod_id]["name"]
    price=product_dict[prod_id]["price"]

    revenue=ord["quantity"] * price
    total_rev += revenue

    if name not in rev_prod:
        rev_prod[name]=revenue
    else:
        rev_prod[name]+=revenue

cust_spend={}
for ord in orders:
    customer=ord["customer"]
    prod_id=ord["product_id"]
    price=product_dict[prod_id]["price"]

    revenue = ord["quantity"] * price

    if customer not in cust_spend:
        cust_spend[customer]=revenue
    else:
        cust_spend[customer]+=revenue

top_cust=max(cust_spend, key=cust_spend.get)

# Write report
with open("sales_report.txt", "w") as file:
    file.write("E-Commerce Sales Report\n\n")
    file.write(f"Total Website Visits: {total_visits}\n")
    file.write(f"Unique Visitors: {unique_visit}\n\n")
    file.write(f"Total Revenue: {total_rev}\n\n")

    file.write(f"Top Customer: {top_cust}\n\n")
    file.write("Product Sales\n")

    # Print in fixed order like example
    for product in ["Laptop", "Mouse", "Keyboard", "Monitor"]:
        file.write(f"{product} -> {rev_prod[product]}\n")

print("sales_report.txt created successfully!")