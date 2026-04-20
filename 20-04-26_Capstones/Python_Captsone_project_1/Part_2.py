import json

#Task-7
products=[]
with open("products.json","r") as file:
    data=json.load(file)

products=data["products"]

#Task-8
for prod in products:
    print(prod["name"], " : ", prod["price"])

#task-9
info={}
for prod in products:
    product_id=prod["product_id"]
    name=prod["name"]
    price=int(prod["price"])

    info[product_id] = {"name": name, "price": price}

print(info)

#Task-10

highest=max(products, key=lambda x:x["price"])
print("Most expensive product : ",highest["name"], " - ", highest["price"])

#Task-11
lowest=min(products, key=lambda x:x["price"])
print("least expensive product : ",lowest["name"], " - ", lowest["price"])
