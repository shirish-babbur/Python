class Parent(object):
    def altered(self):
        print("PARENT altered()!")

class Child(Parent):
    def altered(self):
        print("In Child, BEFORE PARENT altered()!")
        # Calling function of parent through super function.
        super(Child, self).altered()
        print("In Child, AFTER PARENT altered()!")

#Creating objects for both
dad = Parent()
son = Child()

# Parent's altered method call
dad.altered()
# child's altered method call which will call parent's method too.
son.altered()
