from os import system
if system("clear") !=0 : system("cls")

#read a file line by lines
# Uncomment the following lines to execute this part
"""with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())"""

#read all lines at once
# This will read all lines and return a list of lines
# Uncomment the following lines to execute this part
"""with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)"""

#add some text atthe end of the files
# Uncomment the following lines to execute this part
"""with open('caperucita.txt', 'a') as file:
    file.write("\n\nBy:ChatGPT")"""

#Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write("\n\nBy:ChatGPT")