from json import load, dump
from os import system
if system("clear") !=0 : system("cls")

path = "products.json"

with open(path, "r") as file:
    products = load(file)
    # print(products)

for product in products:
    print(f"Product: {product['name']}")
    print(f"Price: {product['price']}")
    print(f"Quantity: {product['quantity']}")
    print(f"category: {product['category']}")
    print(f"entry_date: {product['entry_date']}")
    print("-" * 20)
