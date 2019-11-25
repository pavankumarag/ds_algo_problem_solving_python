#needs python 3
def range(n):
    start = -1
    end = n
    def next():
        #nonlocal start   #;supported only in python 3 
        if start == end:
            return 
        start += 1
        return start
    return next


#x = range(5)

def myrange(n):
    i=0
    while i < n :
        yield i
        i +=1
        
print myrange(5)

x = range(5)
print next(x)