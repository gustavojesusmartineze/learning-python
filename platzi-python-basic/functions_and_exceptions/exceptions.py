from os import system
if system("clear") != 0: system("cls")

res = "10"

try:
    divisor = int(input("Enter a divisor: "))
    res = 10 / divisor
except ZeroDivisionError as exception:
    print("ZeroDivisionError occurred")
    print(exception.args)
    print(type(exception))
except ValueError as exception:
    print("ValueError occurred")
    print("The error was:", exception)
    print(exception.args)
    print(type(exception))
except Exception as exception:
    print("Exception error occurred")
    print("The error was:", exception)
    print(exception.args)
    print(type(exception))

def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# Imprimir la jerarquía comenzando desde la clase base Exception
print_exception_hierarchy(Exception)