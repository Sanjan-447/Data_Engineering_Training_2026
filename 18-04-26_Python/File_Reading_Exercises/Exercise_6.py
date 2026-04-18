import csv

sales=[]
with open("sales.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["quantity"]= int(row["quantity"])
        row["price"]=int(row["price"])
        sales.append(row)

total_rev=0
for row in sales:
    total_rev+=row["price"]
print("Total revenue: ",total_rev)

quantity={}
for row in sales:
    qty=row["quantity"]
    product=row["product"]
    if product in quantity:
        quantity[product]+=qty
    else:
        quantity[product]=qty

print("Quantity sold per product:")
print(quantity)

rev={}
for row in sales:
    product=row["product"]
    revenue=row["price"] * row["quantity"]
    if product in rev:
        rev[product]+=revenue
    else:
        rev[product]=revenue
highest=max(rev, key=rev.get)
print("Highest selling product is : ", highest)

print("Total revenue per product:")
for product,revenue in rev.items():
    print(product,": ",revenue)

print("product with sales above 50000")
for product,revenue in rev.items():
    if revenue > 50000:
         print(product,": ",revenue)
