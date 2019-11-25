
def foo():
    print('foo')
    
#foo()

def log(f):
    def wrapper():
        print('Function execution started') 
        f()
        print('Function execution completed')
        return
    return wrapper   

foo = log(foo)

foo()

#Decorators
print('Now using decorators')
@log
def bar():
    print('bar')
    
bar()    