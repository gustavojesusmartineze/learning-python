from os import system

if system("clear") != 0: system("cls")

name = input("What's your name? ")

age = int(input("How old are you? "))
print(f"Hello, {name}!")
print(f"You are {age} years old!")

print(f"name is of type {type(name)}")
print(f"age is of type {type(age)}")

