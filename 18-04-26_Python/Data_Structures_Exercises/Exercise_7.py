products = {
"Laptop":75000,
"Mobile":30000,
"Tablet":25000
}

for keys, values in products.items():
    products[keys] += products[keys]*0.10

print(products)