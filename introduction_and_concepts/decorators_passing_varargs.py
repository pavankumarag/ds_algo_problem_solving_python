
def log(f):
    def wrapper(*args,**kwargs):
        print('Function execution started') 
        x=f(*args,**kwargs)
        print x
        print('Function execution completed')
        return x
    return wrapper 

@log
def sum(x,y):
    return x + y

sum(3,4)