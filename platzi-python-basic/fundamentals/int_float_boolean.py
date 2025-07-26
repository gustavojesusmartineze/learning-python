my_flag : bool = True
my_number : int = 42
my_float : float = 3.14

x = 10
y = 5.678

z = 1.2E6
a = 1.2E-6

print(f"my_flag: {my_flag}, type: {type(my_flag)}")
print(f"my_number: {my_number}, type: {type(my_number)}")
print(f"my_float: {my_float}, type: {type(my_float)}")
print(f"x: {x}, type: {type(x)}")
print(f"y: {y}, type: {type(y)}")
print(f"z: {z}, type: {type(z)}")
print(f"a: {a}, type: {type(a)}")

print(x + x)  # This will correctly add the integer and float
print(x + y)  # This will correctly add the integer and float
print(x - y)  # This will correctly subtract the float from the integer
print(x * y)  # This will correctly multiply the integer and float
print(x / y)  # This will correctly divide the integer by the float