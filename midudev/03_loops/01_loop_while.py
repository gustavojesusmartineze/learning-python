import os

os.system("cls")

print("While loop")

counter = 0

while counter < 10:
    print(counter)
    counter += 1

print("End of loop")


counter = 0
while True:
    print(f"Counter: {counter}")
    if counter == 5:
        break
    counter += 1

print("End of loop with break")


counter = 0
while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    print(counter)
else:
    print(f"End of loop with else: {counter}")

print("End of loop Global")


counter = 0
while counter < 10:
    counter += 1

    if counter % 2 == 0:
        continue

    if counter % 7 == 0:
        break

    print(counter)

else:
    print(f"End of loop with else: {counter}")

print("End of loop It did not entered else condition")


number = -1
while number < 0:
    try:
        number = int(input("Enter a positive number: "))

        if number < 0:
            print("The number is not positive")

    except ValueError:
        print("Invalid input, please enter a number")

print(f"The number is: {number}")