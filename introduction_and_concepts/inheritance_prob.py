class B:
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
print E.mro()
e.foo()    

class E1(B2,B1):
    pass
e1 = E1()
e1.foo()