# Functions are a way to group code together
import os

os.system("clear")

""" Define a function that prints a message """

# Function definition
def print_message():
    print("Print Message World!")

print_message()

# Function definition
# Parameters are the values that are passed to the function
# Type hinting is a way to specify the type of the parameter
# It is not a requirement, it is just a suggestion, it is not a requirement, it is just a suggestion
def say_hello(name :str):
    print(f"Hello, {name}!")

say_hello("John")
say_hello("Jane")
say_hello("Jim")
say_hello("Jill")
say_hello("Claudia")

def add_two_numbers(a :int, b :int) -> int:
    return a + b

print(add_two_numbers(1, 2))
print(add_two_numbers(10, 20))
print(add_two_numbers(100, 200))
print(add_two_numbers(1000, 2000))
print(add_two_numbers(10000, 20000))
print(add_two_numbers(100000, 200000))
print(add_two_numbers(1000000, 2000000))

result = add_two_numbers(2, 3)
print(f"The result is: {result}")

# how to document a function
def multiply_two_numbers(a :int, b :int = 2) -> int:
    """This is a function that multiply two numbers"""
    return a + b

result = multiply_two_numbers(2, 3)
print(f"The result is: {result}")
print(multiply_two_numbers.__doc__)
# help(multiply_two_numbers)

def describe_person(name :str, age :int, city :str = "Madrid") -> str:
    """This is a function that describe a person"""
    return f"The person is {name}, {age} years old and lives in {city}"

result = describe_person("Gustavo", 35, "Venezuela")
print(result)

result = describe_person("John", 30)
print(result)

# named arguments
result = describe_person(age=35, name="Gustavo Jesus", city="Carabobo")
print(result)

# *args and **kwargs
def add_numbers(*args :int) -> int:
    """This is a function that add numbers"""
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)
print(result)

def add_args_numbers(*args :int) -> int:
    """This is a function that multiply numbers"""
    result = 0
    for number in args:
        result += number
    return result

result = add_args_numbers(1, 2, 3, 4, 5)
print(result)

# **kwargs
def describe_person_kwargs(**kwargs :str):
    """This is a function that describe a person"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")
        # print(f"The person is {kwargs['name']}, {kwargs['age']} years old and lives in {kwargs['city']} n")

describe_person_kwargs(name="Gustavo Martinez", is_rich=True, city="Carabobo", salary=120000)
print("--------------------------------")
describe_person_kwargs(name="Claudia Ascenzi", age=35, city="Carabobo", children=3)

