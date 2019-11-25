class Person:
    count=0
    @classmethod
    def inc_count(cls):
        cls.count +=1
    
    def __init__(self):
        Person.inc_count()
        
p = Person()

p2 = Person()

print p.count  #prints 2

print p2.count

print Person.count #prints 2