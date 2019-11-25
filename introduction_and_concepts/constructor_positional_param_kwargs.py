class Person:
    def __init__(self,name= None, email = None):
        self.name = name
        self.email = email
    def print_name(self):
        print(self.name)
        
p = Person()
p.print_name()

p = Person(name='pavan')
p.print_name()

p = Person('pavan')
p.print_name()

p = Person(email='pavan@gmail.com')
print p.email