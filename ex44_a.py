class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

# Inheriting methods and attributes from Parent class.
class Child(Parent):
    pass

# Creating objects of both.
dad = Parent()
son = Child()

# Call to parent's implicit via parent object.
dad.implicit()
# Call to Parent's implicit via son' object since parent's methods are inherited.This is valid
son.implicit()
