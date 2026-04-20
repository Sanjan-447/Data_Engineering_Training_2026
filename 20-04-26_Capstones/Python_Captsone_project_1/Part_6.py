import json
import csv

#Task-23
def load_visits():
    with open("website_visits.txt", "r") as file:
        visit=file.read().splitlines()
        
    return visit

#Task-24
def load_product():
    with open("products.json","r") as file:
        data=json.load(file)

    product_dict = {}
    for p in data["products"]:
        product_dict[p["product_id"]] = {"name": p["name"], "price": p["price"]}

    return product_dict

# Task-25
def load_orders():
    orders=[]
    with open("orders.csv","r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            row["order_id"]=int(row["order_id"])
            row["product_id"]=int(row["product_id"])
            row["quantity"]=int(row["quantity"])
            orders.append(row)

    return orders

#Task-26
def product_revenue(product_dict, orders):
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
        
    return rev_prod

#Task-27
def spend_customer(product_dict, orders):
    cust_spend={}
    for ord in orders:
        customer=ord["customer"]
        prod_id=ord["product_id"]
        price=product_dict[prod_id]["price"]

        revenue= ord["quantity"] * price

        if customer not in cust_spend:
            cust_spend[customer]=revenue
        else:
            cust_spend[customer]+=revenue

    return cust_spend

#Task-28
def top_cust(cust_spend):
    return max(cust_spend, key=cust_spend.get)


visit=load_visits()
print("Visits: ", visit)

products=load_product()
print("\nProduct: ",products)

orders= load_orders()
print("\nOrders: ", orders)

rev_prod= product_revenue(products, orders)
print("\n Revenue per product: ", rev_prod)

customer_spending = spend_customer(products, orders)
print("\nCustomer spending:", customer_spending)

top_customer = top_cust(customer_spending)
print("\nTop Customer:", top_customer)

