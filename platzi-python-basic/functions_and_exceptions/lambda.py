from os import system
if system("clear") != 0: system("cls")

# addition
add = lambda a, b : a + b
print(add(2, 3))  # Output: 5

# multiplication
multiply = lambda a, b : a * b
print(multiply(5, 3))  # Output: 15

# list with map
numbers = range(11)
# Using map with a lambda function to square each number
# Using list comprehension to achieve the same result is faster and more readable
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

squared_comprehension = [x ** 2 for x in numbers]
print(squared_comprehension)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(lambda x : x % 2 ==0, numbers))
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]