class Car:  #old class style
    pass

class Person(object): 
    pass

c = Car()
print type(c), type(Car)

p = Person()

print type(p), type(Person)


class B(object):
    def foo(self):
        print('b')

class B1(B):
    pass
    
class B2(B):
    def foo(self):
        print('b2')
        
class E(B1,B2): 
    pass


e = E()
print E.mro()  #MRO - Method Resolution Order
e.foo()    

class E1(B2,B1):
    pass
e1 = E1()
e1.foo()