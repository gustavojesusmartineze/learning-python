###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

person = {
    "name": "Gustavo",
    "age": 35,
    "city": "Carabobo",
    "is_rich": True,
    "children": 3,
    "salary": 120000,
    "skills": ["Python", "JavaScript", "SQL", "AI", "PHP", "Docker"],
    "socials": {
        "twitter": "https://twitter.com/gustavo_martinez",
        "linkedin": "https://www.linkedin.com/in/gustavo-martinez-7654321",
        "github": "https://github.com/gustavo-martinez"
    }
}

print(person)
print(person["name"])
print(person["age"])
print(person["city"])
print(person["is_rich"])
print(person["children"])
print(person["skills"][0])
print(person["salary"])
print(person["socials"])
print(person["socials"]["twitter"])
print(person["socials"]["linkedin"])
print(person["socials"]["github"])

person["skills"].append("Angular")
person["skills"].append("Machine Learning")
person["skills"].append("Data Science")

print(person["skills"])

del person["city"]

salary = person.pop("salary")
print(salary)
print(person)

# update a dictionary
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

print(a)
print(b)

a.update(b)
print(a)

# get all keys
print(a.keys())

# get all values
print(a.values())

# get all items
print(a.items())

for key, value in a.items():
    print(f"{key}: {value}")
