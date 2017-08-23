# To run this script you will use "Python {script_name} {1st argument} {2nd argument} {3rd argument}"
from sys import argv
# Unpack command like params into varibles.
# Taking inputs using command line arguments.
script, first, second, third = argv

print("Your script name : ", script)
print("Your 1st parameter : ", first)
print("Your 2nd parameter : ", second)
print("Your 3rd parameter : ", third)

# Taking inputs using 'input()' function
fate_number = input("Enter your lucky Number: ")
print(f"This is your FATE number : {fate_number}")
