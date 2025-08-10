from math import pi
from os import system
if system("clear") != 0: system("cls")

radius = 5
area = pi * radius ** 2
circumference = 2 * pi * radius
print(f"Area of circle with radius {radius}: {area}")
print(f"Circumference of circle with radius {radius}: {circumference}")