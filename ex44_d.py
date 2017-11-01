class Parent(object):
    def implicit(self):
        print("PARENT's implicit()!")

    def override(self):
        print("PARENT's override()!")

    def altered(self):
        print("PARENT's altered()!")

# Inheriting methods and attributes from parent class.
class Child(Parent):
    # Overrides parent's method here.
    def override(self):
        print("CHILD's overrride()!")

    # Overrides parent's altered method.
    def altered(self):
        print("In Child, BEFORE PARENT altered()!")
        # Calls to parent's altered method.
        super(Child, self).altered()
        print("In Child, AFTER PARENT altered()!")

dad = Parent()
son = Child()

dad.implicit()
dad.override()
dad.altered()

# Inherited form the parent, So valid call.
son.implicit()
# This one overrides parent's method.
son.override()
# This one overrides parent's method and calls back again using super.
son.altered()
