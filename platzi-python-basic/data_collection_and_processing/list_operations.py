from os import system

if system("clear") != 0: system("cls")

spam = ['spam'] * 4
print(spam)  # ['spam', 'spam', 'spam', 'spam']

t1 = [1, 2]
t2 = [3, 4]
print(t1 + t2)   # [1, 2, 3, 4]

scramble = ['w', 'c', 'n', 'a', 'b']
print(sorted(scramble))  # ['a', 'b', 'c', 'n', 'w']

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False, different objects
print(a == b)  # True, same content
