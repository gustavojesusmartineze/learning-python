from os import system

if system("clear") != 0: system("cls")

todo = ["Go out for breakfast",
    "Lunch with friends",
    "Visit the museum",
    "Go back home",
    "Dinner with family"]

print(todo)
print(type(todo))

mix = [1, "Hola", 3.14, True, None]
print(mix)
print(type(mix))
print(len(mix))
print(mix[2])  # 3.14
print(mix[-1])  # None (last element)

print(mix[1:3])  # ["Hola", 3.14] (slice from index 1 to 2)
print(mix[1:])  # ["Hola", 3.14, True, None] (slice from index 1 to end)
print(mix[:3])  # [1, "Hola", 3.14] (slice from start to index 2)
print(mix[-3:])  # [3.14, True, None] (slice from third last to end)
print(mix[-4:-1])  # ["Hola", 3.14, True] (slice from fourth last to second last)


mix.append("New item")  # Add an item to the end
print(mix)
mix.extend(["Another item", 42, 19755968])  # Extend the list with multiple items
print(mix)

mix.insert(2, "Inserted item")  # Insert an item at index 2
print(mix)
print(mix.index("Hola"))  # Find the index of "Hola"

numbers = [1, 2, 100.01, 90, 3, 55, 4, 5]
print("max Value: ", max(numbers))  # Maximum value
print("min Value: ", min(numbers))  # Minimum value
print("sum Value: ",sum(numbers))  # Sum of all elements
print(sorted(numbers))  # Sorted list
print(numbers)  # Original list remains unchanged
numbers.sort()  # Sorts the list in place
print(numbers)  # Now the list is sorted

del numbers[-1]  # Delete the first element
print(numbers)  # List after deletion

del numbers
# print(numbers) # This will raise an error since numbers is deleted


t = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(t)  # ['a', 'b', 'c']
t.pop(1)  # Remove and return the item at index 1
print(t)  # ['a', 'c']
t.remove('e')  # Remove the first occurrence of 'a'
print(t)  # ['a', 'b', 'c', 'd', 'f', 'g']