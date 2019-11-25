
print dir(int)

#1 x+Y in python is creating new obj and adding values of x.p + y.p = new.p  ; x+y = x.__add__(y)
class Amount:
    def __init__(self,price):
        self.price = price
    def __add__(self,other):
        a = Amount(0)
        a.price = self.price + other.price
        return a
    def __str__(self):
        return 'Amount {}'.format(self.price)
    def __repr__(self):
        return str(self)
    
a1 = Amount(50)
a2 = Amount(40)

a3 = a1 + a2 

print a3.price

print(a1)

l = [Amount(10), Amount(12), Amount(30)]

print(l)  #with out __repr__ prints [<__main__.Amount instance at 0x1092cab90>, <__main__.Amount instance at 0x1092cad88>, <__main__.Amount instance at 0x1092cae60>]

