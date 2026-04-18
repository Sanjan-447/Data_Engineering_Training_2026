orders = [
{"order_id":1,"customer":"Rahul","amount":2500},
{"order_id":2,"customer":"Sneha","amount":1800},
{"order_id":3,"customer":"Rahul","amount":3200},
{"order_id":4,"customer":"Amit","amount":1500}
]
count={}
order_count={}
for order in orders:
    cust=order["customer"]
    amt=order["amount"]
    if cust in count:
        count[cust]+=amt
    else:
        count[cust]=amt
    if cust in order_count:
        order_count[cust]+=1
    else:
        order_count[cust]=1
print(count)

spending_cust=max(count , key=count.get)
print("Highest spending customer:", spending_cust)

print("Order count per customer: ", order_count)
