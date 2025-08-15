from os import getcwd, system
if system("clear") != 0: system("cls")

#get current working directory
current_path = getcwd()
print(f"Current working directory: {current_path}")

#list files in the current directory
from os import listdir
files = listdir(current_path)
print("Files in the current directory:")
for file in files:
    print(file)

# filter and display only text files
txt_files = [file for file in files if file.endswith('.txt')]
print("Text files in the current directory:")
for txt_file in txt_files:
    print(txt_file)

# rename a file
# Uncomment the following lines to rename a file
# from os import rename
# rename("rename.txt", "renamed_file.txt")
# print("File renamed successfully.")

