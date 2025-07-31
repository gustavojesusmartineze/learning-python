from os import system
if system("clear") != 0: system("cls")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # This is a method to greet the person
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

print(person1.greet())
print(person2.greet())