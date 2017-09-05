# imports argv from the module sys
from sys import argv

# unpacks argv into script and filename
script, filename = argv

print(f"We are going to erase {filename}.")
print("If you don't want that, Hit CTRL-C (^C).")
print("If you do want that, Hit RETURN.")

input("?")

print("Opening the file...")
# Opens file in the write mode.
target = open(filename,"w")

print("Truncating the file. Goodbye!")
# Truncates file contents.
# target.truncate()  Redundant since its 'w' mode.

print("Now I'm going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I'm going to write these to file.")

target.write(f"{line1}\n{line2}\n{line3}\n")

print("And Finally, we close it.")
target.close()
