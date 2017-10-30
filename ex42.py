## Animal is-a object (yes, sort of confusing) look at the class
class Animal(object):
    # Simple default function for making sound.
    def make_sound(self):
        print("Sounds!")
    pass

## Dog is-a Animal and has-a 'name' attribute
class Dog(Animal):
    def __init__(self, name):
        ## saving value of name in this object's state.
        self.name = name
    # Overrided function to make specific sound for each animal viz. in this case is DOG.
    def make_sound(self):
        print("BOW BOW!")

## Cat is-a Animal and has-a 'name' attribute
class Cat(Animal):
    def __init__(self, name):
        ## Saving value of name in this object's state.
        self.name = name
    # Overrided function to make specific sound for each animal viz. in this case is Cat.
    def make_sound(self):
        print("MEOW MEOW!")

## Person is-a Object and has-a name and pet of some kind
class Person(object):
    def __init__(self, name):
        self.name = name
        ## Person has pet of some kind
        self.pet = []
    # Simple function to feed animal.
    def feed_animal(self):
        print(f"{self.name} Served {self.pet[0].name} with Food!")
    # Add more pets i.e one to many realtion
    def add_pet(self,pet):
        self.pet.append(pet)
    # List all Pets.
    def list_pets(self):
        for pet in self.pet:
            print(f"{self.name} has {pet.name} as pet.")

## Employee is-a Person and has-a name and salary
class Employee(Person):
    def __init__(self, name, salary):
        ## Setting name of the employee through calling constructor of Person
        super(Employee, self).__init__(name)
        ## Saving salary of the Employee
        self.salary = salary
    # Overrided function for employee to feed animal.
    def feed_animal(self):
        print(f"{self.name} Serving {self.pet[0].name} with food!")

## Fish is-a Object
class Fish(object):
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
marry.add_pet(satan)

## Frank is-a Employee having salary 120000
frank = Employee("Frank", 120000)

## Frank has-a pet named Rover
frank.add_pet(rover)

# Marry's pet is hungry and makes sound.
marry.pet[0].make_sound()

# Marry serves food to her pet.
marry.feed_animal()
marry.add_pet(rover)

# Frank's pet is hungry.
frank.pet[0].make_sound()

# Frank  Feeds his pet.
frank.feed_animal()
frank.add_pet(satan)

#List Marry's pets.
marry.list_pets()

#List Frank's pets
frank.list_pets()

## Flipper is a Fish
flipper = Fish()

## Crouse is-a Salamon
crouse = Salmon()

## Harry is-a Halibut
harry = Halibut()
