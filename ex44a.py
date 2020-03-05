class Parent(object):
    def implicit(self):
        print("PARENT implicit")


class Son(Parent):
    pass


dad = Parent()
son = Son()

dad.implicit()
son.implicit()
