from csv import DictReader, DictWriter
from os import system
if system("clear") != 0: system("cls")

file_path = "products.csv"
updated_file_path = "updated_products.csv"

with open(file_path, mode="r") as file:
    csv_reader = DictReader(file)
    #get the fieldnames from the first row
    fildnames = csv_reader.fieldnames + ["total_value"]

    with open(updated_file_path, mode="w", newline="") as updated_file:
        csv_writer = DictWriter(updated_file, fieldnames=fildnames)
        csv_writer.writeheader() # Write the header with the new field

        for row in csv_reader:
            # Calculate the total value for each product
            total_value = float(row["price"]) * int(row["quantity"])
            row["total_value"] = total_value
            csv_writer.writerow(row)  # Write the updated row with the new field
