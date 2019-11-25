class B1:
    def foo(self):
        print('b1')
    
class B2:
    def foo(self):
        print('b2')
        
class E(B1,B2): 
    pass


e = E()

e.foo()    

class E1(B2,B1):
    pass
e1 = E1()
e1.foo()