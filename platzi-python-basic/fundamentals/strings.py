name = "Gustavo"
character = 'G'
name_with_underscore = '''Gustavo with underscore'''
print(type(name))
print(type(character))
print(type(name_with_underscore))

name = "Gustavo Martinez"
print(name.capitalize())  # This will raise an AttributeError because 'ascii' is not a method of str
print(name.upper())  # This will correctly convert the string to uppercase
print(name.lower())  # This will correctly convert the string to lowercase
print(name.title())  # This will correctly convert the string to title case
print(name.replace("Gustavo", "Gus"))  # This will correctly replace 'Gustavo' with 'Gus'
print(name.split(" "))  # This will correctly split the string into a list of words
print(name.find("Martinez"))  # This will correctly find the index of 'Martinez' in the string
print(name.index("Martinez"))  # This will correctly find the index of 'Martinez' in the string
print(name.startswith("Gustavo"))  # This will correctly check if the string starts with 'Gustavo'
print(name.endswith("Martinez"))  # This will correctly check if the string ends with 'Martinez'
print(name.isalpha())  # This will correctly check if the string contains only alphabetic characters
print(name.isalnum())  # This will correctly check if the string contains only alphanumeric characters
print(name.isdigit())  # This will correctly check if the string contains only digits
print(name.islower())  # This will correctly check if the string is in lowercase
print(name.isupper())  # This will correctly check if the string is in uppercase
print(name.isspace())  # This will correctly check if the string contains only whitespace characters
print(name.strip())  # This will correctly remove leading and trailing whitespace
print(name.lstrip())  # This will correctly remove leading whitespace
print(name.rstrip())  # This will correctly remove trailing whitespace
print(name.count("a"))  # This will correctly count the occurrences of 'a' in the string
print(name.splitlines())  # This will correctly split the string into lines (though there are no newlines in this example)
print(name.center(30))  # This will correctly center the string within a width of 30 characters
print(name.ljust(30))  # This will correctly left-justify the string within a width of 30 characters
print(name.rjust(30))  # This will correctly right-justify the string within a width of 30 characters
print(name.zfill(30))  # This will correctly pad the string with zeros to a width of 30 characters
print(name.swapcase())  # This will correctly swap the case of all characters in the string
print(name.removeprefix("Gustavo "))  # This will correctly remove the prefix 'Gustavo ' from the string
print(name.removesuffix("Martinez"))  # This will correctly remove the suffix 'Martinez' from the string
print(name.translate(str.maketrans("G", "g")))  # This will correctly translate 'G' to 'g' in the string
print(name.format())  # This will correctly format the string (though there are no placeholders to format)
print(name.format_map({"name": "Gustavo"}))  # This will correctly format the string using a mapping
print(name.casefold())  # This will correctly case-fold the string for case-insensitive comparisons
print(name.partition("Martinez"))  # This will correctly partition the string into a tuple of three parts
print(name.rpartition("Martinez"))  # This will correctly partition the string into a tuple of three parts
print(name.join(["Hello", "World"]))  # This will raise a TypeError because '

carla = "Carla  Marcela"
address = "Calle 123"
print(carla + " " + address)  # This will correctly concatenate the two strings
print(carla)
print(len(carla))
print(len(address))