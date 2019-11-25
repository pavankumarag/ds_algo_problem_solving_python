class Person:
    def __init__(self,name):
        self.name = name
    def print_name(self):
        print(self.name)
        
        
person = Person("Pavan")
person.print_name()