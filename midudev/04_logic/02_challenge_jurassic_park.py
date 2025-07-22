"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex, depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma de todos los números pares en la lista).
"""

from os import system
if system("clear") != 0: system("cls")

# Para ver si un número es par
# siempre usamos el módulo % 
# nos da el resto de la división: eggs % 2 == 2

def sum_even_numbers(numbers :list[int]) -> int:
    """This function sums the even numbers in a list"""
    sum = 0

    for number in numbers:
        if number % 2 == 0:
            sum += number

    return sum

print(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_even_numbers([1, 3, 5, 7, 9]))
print(sum_even_numbers([2, 4, 6, 8, 10]))
print(sum_even_numbers([100, 1, 3, 5, 7, 9]))

