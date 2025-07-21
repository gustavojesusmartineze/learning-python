### 5. INPUT
print("5. INPUT:")
print("-" * 40)

name = input("Hello, Enter your name:\n")
print(f"Hello, {name}! Nice to meet you!")

age = input("Enter your age:\n")
# age = int(age)
# age = int(input("Enter your age:\n"))
print(f"You are {age} years old.")

country, city = input("Enter your country and city:\n").split(",")
print(f"You are from {country} and live in {city}.")

# print(f"in 20 years you will be {age + 20} years old.")
print(f"in 20 years you will be {int(age) + 20} years old.")

print("-" * 40)