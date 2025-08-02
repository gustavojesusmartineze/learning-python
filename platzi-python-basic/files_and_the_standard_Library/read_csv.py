from csv import DictReader
from os import system
if system("clear") != 0: system("cls")

with open("products.csv", mode = "r") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(f"Product: {row['name']}, Price: {row['price']}, quantity: {row['quantity']},", end=" ")
        print(f"Brand: {row['brand']}, entry date: {row['entry_date']}")
        print("-" * 80)

print("CSV file read successfully.")