# Quantifiers in regex in english


# {n} -> n times
# {n,m} -> n to m times
# {n,} -> n or more times
# {,m} -> 0 to m times


import re
from os import system
if system("clear") != 0: system("cls")


# * -> 0 or more
print("* -> 0 or more")
text = "aaaba"
pattern = r"a*"
matches = re.findall(pattern, text)
print(matches)


# + -> 1 or more
text = "ddd aaa ccc aa bb casa"
pattern = r"a+"
matches = re.findall(pattern, text)
print("+ -> 1 or more")
print(matches)

# ? -> 0 or 1
text = "aaabacbacab"
pattern = r"a?b"
matches = re.findall(pattern, text)
print("? -> 0 or 1")
print(matches)

# Ejercicio: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r"\+?34 \d{9}"

# {n}: Exactamente n veces
text = "aaaaaa         aa   aaaa"
pattern = "a{3}"
matches = re.findall(pattern, text)

print(matches)

# {n, m}: De n a m veces
text = "u uu uuu u uu"
pattern = r"\w{2,3}"
matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa árbol león cinco murcielago"
pattern = r"\b\w{4,6}\b"
matches = re.findall(pattern, words)
print(matches)

# Ejercicio
# Encuentra las palabras de más de 6 letras
words = "ala fantastico casa árbol león cinco murcielago"
pattern = r"\b\w{6,}\b"
matches = re.findall(pattern, words)
print(matches)