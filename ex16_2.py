# imports argv from the module sys
from sys import argv

# unpacks argv into script and filename
script, filename = argv

print(f"We are going to read {filename}.")
print("If you don't want that, Hit CTRL-C (^C).")
print("If you do want that, Hit RETURN.")

input("?")

print("Opening the file...")
# Opens file in the read mode.
target = open(filename,"r")

print("Reading the file contents...")
# Reads the whole content of file and prints it on console.
print(target.read())

print("And Finally, we close it.")
# File object closed.
target.close()
