
def print_two(*args):
    one, two = args
    print(f"arg1: {one}, arg2: {two}.")

# Ok, that *args is actually pointless, we can just do this
def print_two_again(one,two):
    print(f"arg1: {one} arg2: {two}.")

# This one takes only one argument
def print_one(one):
    print(f"arg1: {one}")

# This one takes no arguments
def print_none():
    print("I got nothin...!")

print_two("Shirish","Babbur")
print_two_again("Shirish","Babbur")
print_one("Shirish")
print_none()
