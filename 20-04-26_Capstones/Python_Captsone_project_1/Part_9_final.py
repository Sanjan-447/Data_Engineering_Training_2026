import json
import csv

with open("website_visits.txt", "r") as file:
    visits = file.read().splitlines()

orders = []
with open("orders.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        orders.append(row)

visit_count = {}
for name in visits:
    if name in visit_count:
        visit_count[name] += 1
    else:
        visit_count[name] = 1

visit_set = set(visits)
cust_set=[]
for order in orders:
    cust_set.append(order["customer"])
cust_set = set(cust_set)

# Task 29
never_ordered = visit_set - cust_set
print("Visitors who visited but never ordered:")
print(never_ordered)

# Task 30
print("\n Customers who ordered but visited only once:")
for customer in cust_set:
    if visit_count.get(customer, 0) == 1:
        print(customer)