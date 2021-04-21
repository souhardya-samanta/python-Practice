class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(self.name)
person = Person("Daniel")
person.talk()