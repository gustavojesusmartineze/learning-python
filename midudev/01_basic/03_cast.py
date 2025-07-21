# What is Casting in Python?
# Casting (also called type conversion) is the process of converting a value from one data type to another. 
# In Python, casting is done using built-in functions that act as constructors for different data types.
#
# PYTHON IS STRONGLY TYPED BUT DYNAMICALLY TYPED:
# - Strongly typed: Type checking is enforced at runtime, no implicit type coercion
# - Dynamically typed: Variable types are determined at runtime, not compile time
#
# Types of Casting in Python
# 1. Implicit Casting (Automatic)
# Python automatically converts smaller data types to larger data types when needed:
# int → float (when doing arithmetic)
# int → complex (when adding complex numbers)
# 2. Explicit Casting (Manual)
# You manually convert between types using constructor functions:
# int() - converts to integer
# float() - converts to float
# str() - converts to string
# bool() - converts to boolean
# list() - converts to list
# tuple() - converts to tuple
# set() - converts to set
# dict() - converts to dictionary

print("=== CASTING IN PYTHON ===\n")

# 1. IMPLICIT CASTING (Automatic)
print("1. IMPLICIT CASTING (Automatic):")
print("-" * 40)

# Integer to Float (automatic)
a = 5
b = 2.5
result = a + b  # 5 is automatically converted to 5.0
print(f"int + float: {a} + {b} = {result} (type: {type(result)})")

# Integer to Complex (automatic)
c = 3 + 4j
result2 = a + c  # 5 is automatically converted to 5+0j
print(f"int + complex: {a} + {c} = {result2} (type: {type(result2)})")

print()

# 2. EXPLICIT CASTING (Manual)
print("2. EXPLICIT CASTING (Manual):")
print("-" * 40)

# String to Integer
print("String to Integer:")
string_num = "123"
integer_num = int(string_num)
print(f"'{string_num}' → {integer_num} (type: {type(integer_num)})")

# String to Float
string_float = "3.14"
float_num = float(string_float)
print(f"'{string_float}' → {float_num} (type: {type(float_num)})")

# Float to Integer (truncates decimal part)
float_val = 3.9
int_val = int(float_val)
# Round the float value to the nearest integer
float_val_rounded = round(float_val)
print(f"{float_val} → {int_val} (type: {type(int_val)})")
print(f"{float_val} → {float_val_rounded} (type: {type(float_val_rounded)})")


# Integer to String
number = 42
string_val = str(number)
print(f"{number} → '{string_val}' (type: {type(string_val)})")

print()

# 3. BOOLEAN CASTING
print("3. BOOLEAN CASTING:")
print("-" * 40)

# Truthy values
print("Truthy values:")
print(f"bool(1): {bool(1)}")
print(f"bool(42): {bool(42)}")
print(f"bool(3.14): {bool(3.14)}")
print(f"bool('hello'): {bool('hello')}")
print(f"bool([1, 2, 3]): {bool([1, 2, 3])}")

# Falsy values
print("\nFalsy values:")
print(f"bool(0): {bool(0)}")
print(f"bool(0.0): {bool(0.0)}")
print(f"bool(''): {bool('')}")
print(f"bool([]): {bool([])}")
print(f"bool(None): {bool(None)}")

print()

# 4. COLLECTION CASTING
print("4. COLLECTION CASTING:")
print("-" * 40)

# String to List
text = "Python"
char_list = list(text)
print(f"'{text}' → {char_list}")

# String to Tuple
char_tuple = tuple(text)
print(f"'{text}' → {char_tuple}")

# String to Set (removes duplicates)
word = "hello"
char_set = set(word)
print(f"'{word}' → {char_set}")

# List to Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"{my_list} → {my_tuple}")

# Tuple to List
my_tuple2 = (10, 20, 30)
my_list2 = list(my_tuple2)
print(f"{my_tuple2} → {my_list2}")

print()

# 5. COMMON CASTING SCENARIOS
print("5. COMMON CASTING SCENARIOS:")
print("-" * 40)

# User input (always string) to number
print("User input conversion:")
user_input = "25"  # Simulating input()
age = int(user_input)
print(f"User input: '{user_input}' → Age: {age}")

# Number formatting
price = 19.99
price_string = str(price)
print(f"Price: {price} → String: '{price_string}'")

# List of strings to list of integers
string_numbers = ["1", "2", "3", "4", "5"]
integer_numbers = [int(x) for x in string_numbers]
print(f"String numbers: {string_numbers}")
print(f"Integer numbers: {integer_numbers}")

print()

# 6. CASTING ERRORS AND HANDLING
print("6. CASTING ERRORS AND HANDLING:")
print("-" * 40)

# Invalid conversions
print("Invalid conversions (will cause errors):")
try:
    invalid_int = int("hello")
except ValueError as e:
    print(f"int('hello') → ValueError: {e}")

try:
    invalid_float = float("abc")
except ValueError as e:
    print(f"float('abc') → ValueError: {e}")

# Safe conversion with error handling
def safe_int_conversion(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

print(f"\nSafe conversion examples:")
print(f"safe_int_conversion('123'): {safe_int_conversion('123')}")
print(f"safe_int_conversion('abc'): {safe_int_conversion('abc')}")
print(f"safe_int_conversion('12.34'): {safe_int_conversion('12.34')}")

print()

# 7. ADVANCED CASTING
print("7. ADVANCED CASTING:")
print("-" * 40)

# Binary, Octal, Hexadecimal strings to int
binary_str = "1010"
octal_str = "12"
hex_str = "1A"

binary_int = int(binary_str, 2)  # Base 2
octal_int = int(octal_str, 8)    # Base 8
hex_int = int(hex_str, 16)       # Base 16

print(f"Binary '{binary_str}' → {binary_int}")
print(f"Octal '{octal_str}' → {octal_int}")
print(f"Hexadecimal '{hex_str}' → {hex_int}")

# Complex number creation
real_part = 3
imaginary_part = 4
complex_num = complex(real_part, imaginary_part)
print(f"complex({real_part}, {imaginary_part}) → {complex_num}")

print("\n=== CASTING COMPLETE ===")

print()