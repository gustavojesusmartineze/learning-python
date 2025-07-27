from os import system

system("clear")

a = [1, 2, 3, 4, 5]
b = a
a[0] = 10  # Modifying the first element of list a
print("Original list a:", a)
print("Reference list b:", b)
print(id(a), id(b)) # Both lists point to the same object in memory  

del a
print("After deleting a:")
try:
    print("List a:", a)
except NameError as e:
    print("List a is deleted:", e)
print("List b remains:", b)

# To create a copy of the list, use the copy method or slicing
a = [1, 2, 3, 4, 5]
b = a.copy()  # or b = a[:]
c = a[:]  # Another way to copy using slicing
copy = a
a.append(6)  # Modifying list a after copying
print("Copied list a:", a)
print("Copied list b:", b)
print("Copied list c:", c)
print("Copied list copy:", copy)
print(id(a), id(b), id(c), id(copy))  # Now they point to different objects in memory