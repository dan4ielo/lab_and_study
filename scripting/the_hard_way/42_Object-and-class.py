# This excercise shows the differences between objects and classes.
# In simple terms - classes are the blueprints that are used when 
# creating an object and the object is the thing that fills in the
# class

# Animal is-an object
class Animal(object):
    pass

# Dog is-an object
class Dog(Animal):
    
    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-an object
class Cat(Animal):
    
    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-an object
class Person(object):

    def __init__(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# Employee is-an object
class Employee(Person):

    def __init__(self,name, salary):
        # Employee becomes like a Person
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-an object
class Fish(object):
    pass

#Salmon is-an object
class Salmon(Fish):
    pass

# Halibut is-an object
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a person
mary = Person("Mary")

# mary has-a pet cat - satan
mary.pet = satan

# frank is-an employee
frank = Employee("Frank", 120000)

# frank has-a pet dog - rover
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# harry is a halibut
harry = Halibut()
