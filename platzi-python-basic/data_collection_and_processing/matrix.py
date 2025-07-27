from os import system

if system("clear") != 0: system("cls")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)
print(matrix[0])
print(matrix[1])
print(matrix[2])