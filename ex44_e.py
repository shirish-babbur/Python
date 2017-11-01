class Other(object):
    def override(self):
        print("OTHER's override()!")

    def implicit(self):
        print("OTHER's implicit()!")

    def altered(self):
        print("OTHER's altered()!")

class Child(object):
    # constructor initialzes the other object.i.e. Composition.
    def __init_(self):
        self.other = Other()

    def implicit(self):
        # calls to other's implicit function
        self.other.implicit()

    def override(self):
        # calls to other's override function.
        self.other.override()

    def altered(self):
        print("In Child, BEFORE OTHER's altered()!")
        # call to other's override function.
        self.other.altered()
        print("In Child, AFTER OTHER's altered()!")

son = Child()

son.implicit()

son.override()

son.altered()
