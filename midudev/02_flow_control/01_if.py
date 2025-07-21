### 1. IF
import os

os.system("clear")

my_age : int = int(input("Enter your age:\n"))
has_driver_license : bool = input("Do you have a driver license? (y/n):\n").lower() == "y"

# if my_age > 18:
#     print("You are an adult")
#     print("Second message")
# else:
#     print("You are a minor")


# if my_age > 18 and has_driver_license:
#     print("You are an adult and have a driver license")
# else:
#     print("You are a minor or you don't have a driver license")


message = "You are an adult" if my_age > 18 else "You are a minor"
print(message)