from os import system
if system("clear") != 0 : system("cls")

class Calculator:
    def add_numbers(self, first_number, second_number):
        result = first_number + second_number 
        return result

calc = Calculator()

print(calc.add_numbers(5, 3))