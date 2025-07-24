# sets in regular expressions

import re

# sets are defined using square brackets []
# they match any one of the characters in the set
# for example, [aeiou] matches any of the vowels a, e, i, o, or u
# [0-9] matches any digit from 0 to 9
# [a-z] matches any lowercase letter from a to z
# [A-Z] matches any uppercase letter from A to Z
# [a-zA-Z] matches any letter from a to z or A to Z
# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.$ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
  print("El nombre de usuario es válido: ", match.group())
else:
  print("El nombre de usuario no es válido")


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
# pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
# \b 

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

## Buscar corner cases que no pasa y arreglarlo:
email1 = "lo.que+sea@shopping.online"
email2 = "michael@gov.co.uk"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

match = re.search(pattern, email1)
if match:
  print("El email1 es válido: ", match.group())
else:
  print("El email1 no es válido")

# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)