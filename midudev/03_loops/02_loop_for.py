import os

os.system("clear")

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits:
    print(fruit)

for index, fruit in enumerate(fruits):
    print(f"Index: {index} - Fruit: {fruit}")

string_midu = "midudev"

for letter in string_midu:
    print(letter)

animals = ["dog", "cat", "bird", "fish", "horse", "cow", "sheep"]

for index, animal in enumerate(animals):
    print(animal)

    if animal == "fish":
        print(f"the fish is hidden in index {index}")
        break

# Continue for fish
for index, animal in enumerate(animals):
    if animal == "fish":
        continue

    print(animal)

#  List comprehension
animals_list = ["dog", "cat", "bird", "fish", "horse", "cow", "sheep"]
animals_upper = [animal.upper() for animal in animals_list]
print(animals_upper)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numbers_squared = [number ** 2 for number in numbers]

print(numbers_squared)

#  List comprehension with condition
numbers_even = [number for number in numbers if number % 2 == 0]
print(numbers_even)