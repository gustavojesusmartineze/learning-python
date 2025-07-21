###
# 04 - List methods
# Secuencias mutables de elementos.
# Pueden contener elementos de diferentes tipos.
###

from os import system
if system("clear") != 0: system("cls")

list1 = [1, 2, 3, 4, 5]
print(list1)

list1.append(6)
print(list1)

list1.insert(1, 120000)
print(list1)

list1.extend([7, 8, 22, 10, 12, 9])
print(list1)


list1.remove(120000)
print(list1)

list1.pop()
print(list1)

list1.pop(3)
print(f"Popped element: {list1}")

list1.sort()
print(list1)

print("Deleting elements from 1 to 4")
del list1[1:4]
print(list1)

list1.clear()
print(list1)

numbers = [1, 2, 9, 3, 4, 66, 10, 7, 5]
print(numbers)

numbers.reverse()
print(numbers)

sorted_numbers_reverse = sorted(numbers, reverse=True)
# numbers.sort(reversed=True)
print(sorted_numbers_reverse)

numbers.sort(reverse=False)
print(numbers)

print("Ordenar una lista de cadenas de texto (todo minúscula)")
fruits = ['manzana', 'pera', 'limón', 'manzana', 'pera', 'limón']
sorted_fruits = sorted(fruits)
print(sorted_fruits)


print("Ordenar una lista de cadenas de texto (mezclas mayúscula y minúscula)")
fruits = ['manzana', 'Pera', 'Limón', 'manzana', 'pera', 'limón']
fruits.sort(key=str.lower)
print(fruits)

# Más cositas útiles
animals = ['🐶', '🐼', '🐨', '🐶', '🐼', '🐼']
print(len(animals))
print(animals.count('🐼'))
print('🐼' in animals)
print('🐹' in animals) # -> False 


odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

all_numbers = odd_numbers + even_numbers
print(all_numbers)

# iterate all_numbers and multiply each element by 2
for number in all_numbers:
    print(number * 2)


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.