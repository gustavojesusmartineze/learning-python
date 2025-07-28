from os import system
if system("clear") !=0 : system("cls")

my_list = [1, 2, 3, 4]
my_iterator = iter(my_list)
print(next(my_iterator))  # Prints 1
print(next(my_iterator))  # Prints 2 
print(next(my_iterator))  # Prints 3
print(next(my_iterator))  # Prints 4

# Uncommenting the next line will raise StopIteration error
# print(next(my_iterator))  # Raises StopIteration

text = "Hello, World!"
text_terator = iter(text)

for caracter in text_terator:
    print(caracter)

# print the odd numbers from 1 to 10
limit = 10
for number in range(1, limit+1, 2):
    print(number)

# define a generator function
def my_generator():
    yield 1
    yield 2
    yield 3

# Usar el generador
for valor in my_generator():
    print(valor)

# Fibonacci generator
def fibonacci(number):
    a, b = 0, 1
    while a < number:
        yield a
        a, b = b, a + b

print("fibonacci numbers up to 10:")
for num in fibonacci(10):
    print(num)