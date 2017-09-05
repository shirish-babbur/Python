# Imports argv from the module sys
from sys import argv
# Unpacks command line arguments.
script, input_file = argv

# function to print all the content of file.
def print_all(f):
    print(f.read())

# function to rewind position of file pointer.
def rewind(f):
    f.seek(0)

# function to print file content line by line.
def print_a_line(line_count, current_file):
    print(line_count,current_file.readline())

# Opens a file.
current_file = open(input_file)

print("First print the whole file:\n")
# Call to print whole content of file.
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# call to reset file pointer to start.
rewind(current_file)

print("Let's print three lines:\n")
# call to print file content line by line.
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

# closes file object.
current_file.close()
