from csv import DictReader, DictWriter
from os import system
if system("clear") != 0 : system("cls")

new_product = {
    "name": "New Product",
    "price": 19.99,
    "quantity": 100,
    "brand": "New Brand",
    "category": "Electronics",
    "entry_date": "2025-07-29",
}

with open("products.csv", "a", newline="") as file:
    file.write("\n")  # Add a newline before writing the new product
    csv_writer = DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)