from os import system

if system("clear") != 0: system("cls")

numbers = {
  1: "one",
  2: "two",
  3: "three",
  4: "four",
  5: "five",
  6: "six",
  "owner": "gustavo",
}

print("Dictionary:", numbers)
print(numbers[1])
print(numbers["owner"])


information = {"gustavo": {"name": "Gustavo",
    "age": 34,
  "job": "Sr. Technical Lead",
  "salary": 150000,
}, "claudia": {
  "name": "Claudia",
  "age": 34,
  "job": "Psychologist",
  "salary": 45000,
}}

print("Information:", information)
information_keys = information.keys()
print("Keys:", information_keys)
print(type(information_keys))
information_values = information.values()
print("Values:", information_values)
print(type(information_values))
information_items = information.items()
print("Items:", information_items)
print(type(information_items))