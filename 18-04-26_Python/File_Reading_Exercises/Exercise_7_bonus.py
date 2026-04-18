import csv

filename = "sales.csv"

summary = {}
with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        quantity = int(row["quantity"])
        price = int(row["price"])

        revenue = quantity * price

        if product not in summary:
            summary[product] = {"qty": 0, "revenue": 0}

        summary[product]["qty"] += quantity
        summary[product]["revenue"] += revenue

print("Product Sales Summary")

for product, data in summary.items():
    print(f"{product} → Qty: {data['qty']} Revenue: {data['revenue']}")

