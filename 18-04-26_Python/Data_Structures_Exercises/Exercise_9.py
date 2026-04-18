sales = [
{"product":"Laptop","qty":5},
{"product":"Mouse","qty":20},
{"product":"Laptop","qty":3},
{"product":"Keyboard","qty":10}
]


total_sales = {}

for item in sales:
    product = item["product"]
    qty = item["qty"]

    if product in total_sales:
        total_sales[product] += qty
    else:
        total_sales[product] = qty

print("Total sales :", total_sales)

highest_product = max(total_sales, key=total_sales.get)

print("Highest selling product:", highest_product, "-", total_sales[highest_product])