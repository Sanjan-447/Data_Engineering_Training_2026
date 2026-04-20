import csv

#Task-12
orders=[]
with open("orders.csv","r") as file:
    reader=csv.DictReader(file)
    
    #Task-13
    for row in reader:
        row["order_id"]=int(row["order_id"])
        row["product_id"]=int(row["product_id"])
        row["quantity"]=int(row["quantity"])
        orders.append(row)
        print(row)

#Task-14
qty_prod={}
for prod in orders:
    prod_id=prod["product_id"]
    qty=prod["quantity"]
    if prod_id not in prod:
        qty_prod[prod_id]=qty
    else:
        qty_prod[prod_id]+=qty

print(qty_prod)

#Task-15
ord_cust={}
for ord in orders:
    cust=ord["customer"]
    if cust not in ord_cust:
        ord_cust[cust]=1
    else:
        ord_cust[cust]+=1

print(ord_cust)