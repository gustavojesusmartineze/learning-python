from os import system
if system("clear") != 0 : system("cls")

numbers = [1, 2, 3, 4, 5]

squares = [number**2 for number in numbers]

print("Squares of numbers:")
print(numbers)
print(squares)