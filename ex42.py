## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind.  Daufalt is None
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)

        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")
print (rover)
## Satan is-a Cat
satan = Cat("Satan")
print (satan)
## Mary is-a Person
mary = Person("Mary")

## Mary has-a pet is Satan
mary.pet = satan

## Frank is-a Employee has-a salary 120000
frank = Employee("Frank", 120000)

##Frank has-a pet is Rover
frank.pet = rover
print (frank.pet)
## Fish has-a flipper
flipper = Fish()

## Salmon has-a crouse
crouse = Salmon()

## Halibut has-a harry
harry = Halibut()
