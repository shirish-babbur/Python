## Animal is-a object (yes, sort of confusing) look at the class
class Animal(Object):
    pass

## Dog is-a Animal and has-a 'name' attribute
class Dog(Animal):
    def __init__(self, name):
        ## saving value of name in this object's state.
        self.name = name

## Cat is-a Animal and has-a 'name' attribute
class Cat(Animal):
    def __init__(self, name):
        ## Saving value of name in this object's state.
        self.name = name

## Person is-a Object and has-a name and pet of some kind
class Person(Object):
    def __init__(self, name):
        self.name = name
        ## Person has pet of some kind
        self.pet = None

## Employee is-a Person and has-a name and salary
class Employee(Person):
    def __init__(self, name, salary):
        ## Setting name of the employee through calling constructor of Person
        super(Employee, self).__init__(name)
        ## Saving salary of the Employee
        self.salary = salary

## Fish is-a Object
class Fish(Object):
    pass

## Salmon is-a Fish of one kind
class Salmon(Fish):
    pass

## Halibut is-a Fish of one kind
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## Satan is-a Cat
satan = Cat("Satan")

## Marry is-a Person
marry = Person("Marry")

## Marry has-a pet named Satan
marry.pet = satan

## Frank is-a Employee having salary 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named Rover
frank.pet = rover

## Flipper is a Fish
flipper = Fish()

## Crouse is-a Salamon
crouse = Salamon()

## Harry is-a Halibut
harry = Halibut()
