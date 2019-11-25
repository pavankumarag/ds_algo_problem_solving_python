def cache(foo):
    cache_map = {}
    def wrapped(*args):
        if args not in cache_map:
            print args,foo(*args)
            cache_map[args] = foo(*args)
        else:
            print('Using from cache')
        return cache_map[args]
    return wrapped

@cache
def fib(n):
    return n if n == 0 or n == 1 else fib(n-1) + fib(n-2)

print fib(5)
