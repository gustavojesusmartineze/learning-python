###
# Basic Data Types:
# int - Integer numbers (whole numbers)
# float - Decimal numbers
# str - Strings (text)
# bool - Boolean values (True/False)
# list - Ordered, mutable collections
# tuple - Ordered, immutable collections
# set - Unordered, unique collections
# dict - Key-value pairs (dictionaries)
# None - Represents absence of value

# Additional Data Types:
# complex - Complex numbers (with imaginary parts)
# bytes - Immutable sequence of bytes
# bytearray - Mutable sequence of bytes
# range - Sequence of numbers
# frozenset - Immutable set
# Each data type includes:
# Clear examples of how to create them
# Print statements showing the values
# Type checking using type() function
# Comments explaining their characteristics
# You can now run this file to see all the data types in action! The code demonstrates both the basic types you had listed and some additional ones that are commonly used in Python.

# 1. Integer (int) - whole numbers
age = 25
year = 2024
negative_number = -10
print(f"Integer examples: {age}, {year}, {negative_number}")
print(f"Type: {type(age)}")
print(f"Type: {type(year)}")
print(123334323455582394328)
print(123334323455582394328 + 2)

# 2. Float - decimal numbers
height = 1.75
pi = 3.14159
temperature = -5.5
print(f"Float examples: {height}, {pi}, {temperature}")
print(f"Type: {type(height)}")

# 3. String (str) - text
name = "Python"
message = 'Hello, World!'
multiline = """This is a
multi-line string"""
print(f"String examples: {name}, {message}")
print(f"Type: {type(name)}")

# 4. Boolean (bool) - True or False
is_active = True
is_completed = False
print(f"Boolean examples: {is_active}, {is_completed}")
print(f"Type: {type(is_active)}")

# 5. List - ordered, mutable collection
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
print(f"List examples: {fruits}, {numbers}, {mixed}")
print(f"Type: {type(fruits)}")

# 6. Tuple - ordered, immutable collection
coordinates = (10, 20)
rgb_color = (255, 128, 0)
person = ("John", 30, "Developer")
print(f"Tuple examples: {coordinates}, {rgb_color}, {person}")
print(f"Type: {type(coordinates)}")

# 7. Set - unordered, unique collection
unique_numbers = {1, 2, 3, 4, 5}
vowels = {'a', 'e', 'i', 'o', 'u'}
print(f"Set examples: {unique_numbers}, {vowels}")
print(f"Type: {type(unique_numbers)}")

# 8. Dictionary (dict) - key-value pairs
person_info = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
scores = {"math": 95, "science": 88, "history": 92}
print(f"Dictionary examples: {person_info}, {scores}")
print(f"Type: {type(person_info)}")

# 9. None - represents absence of value
empty_value = None
print(f"None example: {empty_value}")
print(f"Type: {type(empty_value)}")

# Additional data types in Python:

# 10. Complex numbers
complex_num = 3 + 4j
print(f"Complex number: {complex_num}")
print(f"Type: {type(complex_num)}")

# 11. Bytes - immutable sequence of bytes
byte_data = b'Hello'
print(f"Bytes: {byte_data}")
print(f"Type: {type(byte_data)}")

# 12. Bytearray - mutable sequence of bytes
byte_array = bytearray(b'Hello')
print(f"Bytearray: {byte_array}")
print(f"Type: {type(byte_array)}")

# 13. Range - sequence of numbers
number_range = range(1, 10)
print(f"Range: {list(number_range)}")
print(f"Type: {type(number_range)}")

# 14. FrozenSet - immutable set
frozen_set = frozenset([1, 2, 3, 4])
print(f"FrozenSet: {frozen_set}")
print(f"Type: {type(frozen_set)}")

print("\nAll Python data types demonstrated above!")