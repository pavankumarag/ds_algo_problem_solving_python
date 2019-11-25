class Person:
    def __init__(self, **kwargs):
        for key,val in kwargs.items():
            setattr(self,key,val)
    
    def print_name(self):
        print(self.name)
        
p = Person(name='pavan', email='p@gmail.com',age=3)

print p.name, p.email, p.age

p.print_name()

print dir(Person)

print dir(p)