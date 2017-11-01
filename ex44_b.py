class Parent(object):
    def override(self):
        print("PARENT's Override!")

# Inheriting oveerride function from the parent
class Child(Parent):
    def override(self):
        print("CHILD's Override!")

# creating objects for both
dad = Parent()
son = Child()

# calling parent's overrride function
dad.override()
# Calling son's override function which actuallu overrides parent's inherited function.
son.override()
