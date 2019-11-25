class Person:
    def _private1(self):
        print('private')
    def __private2(self):
        print('private2')
        
p=Person()

p._private1()   #when not sure if a method is not private
#p.__private2()  # when we are absolutely sure if a method is private