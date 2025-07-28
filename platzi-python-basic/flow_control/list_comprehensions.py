from os import system

if system("clear") != 0 : system("cls")

squares = [x**2 for x in range(1, 11)]
print(squares)

# °F = (°C × 1.8) + 32
celsius = [0, 10, 20, 30, 40]
farenheit = [(temp * 1.8) + 32 for temp in celsius]
print(celsius)
print(farenheit)

even = [x for x in range (1, 21) if x % 2 ==0]
print(even)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
# explain above code step by step of the iteration as it runs with real values step by step
# 1st iteration: i = 0, transposed[0] = [1, 4, 7]
# 2nd iteration: i = 1, transposed[1] = [2, 5, 8]
# 3rd iteration: i = 2, transposed[2] = [3, 6, 9] 


print(matrix)

print(transposed)