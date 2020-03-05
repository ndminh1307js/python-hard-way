class Parent(object):
    def override(self):
        print("PARENT override")

    def implicit(self):
        print("PARENT implicit")

    def altered(self):
        print("PARENT altered")


class Child(Parent):
    # using super with __init__
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD AFTER PARENT altered")


dad = Parent()
son = Child('stuff')

dad.override()
son.override()

dad.altered()
son.altered()
