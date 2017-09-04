# Imports argv from the sys module.
from sys import argv

# unpacks values from argv (command line) into scrit and filename.
script, filename = argv

# opens file in the default read mode.
txt = open(filename)

# Prints name and contents of the file.
print(f"Here's your file {filename}:")
print(txt.read())

# Takes input from user in the form of filename.
print("Type the filename again:")
file_again = input("> ")

# Opens the specified file in the default read mode.
txt_again = open(file_again)

# Prints the contents of the file.
print(txt_again.read())

# Close opened file objects.
txt.close()
txt_again.close()
