class Animal(object):
    pass


class Dog(Animal):

    def __init__(self, name):
        self.name = name


class Person(object):

    def __init__(self, name):
        self.name = name
        self.pet = None


class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary


class Fish(object):
    pass


class Salmon(Fish):
    pass


class Halibut(Fish):
    pass


# rover is a Dog
rover = Dog("Rover")

# satan is a Cat
satan = Cat("Satan")

# mary is a person
mary = Person("Mary")

# mary has satan as a pet
mary.pet = satan

# frank is an employee
frank = Employee("Frank", 120000)

# frank has rover as a pet
frank.pet = rover

# flipper is a kind of fish
flipper = Fish()

# crouse is a salmon
crouse = Salmon()

# harry is a halibut
harry = Halibut()
