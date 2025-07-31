from os import system
if system("clear") != 0: system("cls")

class LivingBeing:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"LivingBeing: {self.name}"

    def breathe(self):
        return f"{self.name} is breathing."

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def __str__(self):
        return f"{self.name}, {self.age} years old, Student ID: {self.student_id}"

    #Polymorphism example
    def greet(self):
        return f"Hello, I am {self.name}, a student with ID {self.student_id}."

student = Student("Alice", 20, "S12345")
print(student)
print(student.greet())
print(isinstance(student, Person))  # True, because Student is a subclass of Person
print(isinstance(student, Student))  # True, because student is an instance of Student