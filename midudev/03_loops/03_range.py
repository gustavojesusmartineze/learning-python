import os

#  Range is a sequence of numbers, it is not a list, it is a generator
# it does not generate all the numbers at once, it generates them one by one
# it is more efficient than a list, because it does not generate all the numbers at once
# it does not store all the numbers in memory, it generates them one by one


os.system("clear")

print("Range from 0 to 9")

numbers = range(3)
print(type(numbers))
print(type([1, 2, 3]))

for i in numbers:
    print(i)


for num in range(5, 10):
    print(num)

for num in range(5, 20, 2):
    print(num)

for num in range(5, 100, 5):
    print(num)

for num in range(-10, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)


# Create a list of numbers from 0 to 9
numbers = list(range(10))
print(f"Numbers: {numbers}")


# Range to excecute an action 10 times
for i in range(10):
    print(f"Iteration {i}")


# Range to excecute an action 10 times with a step of 2
for i in range(0, 10, 2):
    print(f"Iteration {i}")

# Range to excecute an action 10 times
for _ in range(10):
    print("Doing Something")


###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")