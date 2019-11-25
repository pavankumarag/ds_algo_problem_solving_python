class Car:
    def __init__(self,name):
        self.name = name
    
    def drive(self):
        print('The car called {} is being driven'.format(self.name))
        

class SuperCar(Car):
    def drive(self): #Diff behavior on same method of super class
        print('Super car {} is being driven'.format(self.name))
    def fly(self):  #Adding more behavior than base class
        print('The car {} is flying '.format(self.name))

c=Car('i20')
print c.drive()

sc = SuperCar('Zest')
print sc.drive(), sc.fly()