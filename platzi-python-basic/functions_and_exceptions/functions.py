from os import system
if system("clear") != 0: system("cls")


def greet(name: str, last_name: str = "Doesn't Matter") -> None:
    """
    Greets the user with their name.
    
    :param name: The name of the user.
    :return: A greeting message.
    """
    print(f"Hello, {name} {last_name}!")


greet("Gustavo", "Martinez")
greet("Carli")



def add(a: int, b: int) -> int:
    """
    Adds two integers and returns the result.
    
    :param a: The first integer.
    :param b: The second integer.
    :return: The sum of a and b.
    """
    return a + b


def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers and returns the result.
    
    :param a: The first integer.
    :param b: The second integer.
    :return: The product of a and b.
    """
    return a * b

def divide(a: int, b: int) -> float:
    """
    Divides two integers and returns the result.
    
    :param a: The numerator.
    :param b: The denominator.
    :return: The quotient of a and b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def calculator(a: int, b: int, operation: str):
    """
    Performs a calculation based on the specified operation.
    
    :param a: The first integer.
    :param b: The second integer.
    :param operation: The operation to perform ('add', 'multiply', 'divide').
    :return: The result of the operation.
    """
    if operation == "add":
        return add(a, b)
    elif operation == "multiply":
        return multiply(a, b)
    elif operation == "divide":
        return divide(a, b)
    else:
        raise ValueError("Invalid operation. Use 'add', 'multiply', or 'divide'.")
    

a = 10
b = 5
print(f"Addition: {calculator(a, b, 'add')}")
print(f"Multiplication: {calculator(a, b, 'multiply')}")
print(f"Division: {calculator(a, b, 'divide')}")
print(f"Invalid Operation: {calculator(a, b, 'subtract')}")