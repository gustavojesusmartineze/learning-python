from json import load, dump
from os import system
if system("clear") !=0 : system("cls")

path = "new_products.json"

new_product = {
    "name": "New Charger",
    "price": 175,
    "quantity": 100,
    "brand": "Gustavo's Gadgets",
    "category": "Accessories",
    "entry_date": "2025-07-30"
}

with open(path, mode="r") as file:
    products = load(file)

products.append(new_product)

with open(path, mode="w") as file:
    dump(products, file, indent=4)

