def fib_rec(n):
	#this takes exponential time
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_rec(n-1) + fib_rec(n-2)


def fib_bruteforce(n):
	old, new = 0, 1
	for i in range(0, n):
		new, old = old + new, new
	return old


f = list()


def fib_rec_memoization(n):
	if f[n] != -1:  # O(1)
		return f[n]
	f[n] = fib_rec_memoization(n-1) + fib_rec_memoization(n-2) #insert to list is O(1)
	return f[n]


def fib_formula(n):
	import math
	return math.pow((math.sqrt(5) + 1)/2, n)/math.sqrt(5)

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

if __name__ == "__main__":
	for i in range(0,51):
		f.append(-1)
	f[0] = 0
	f[1] = 1
	print "fib brute force", fib_bruteforce(10)
	print "fib recursion", fib_rec(10)
	print "fib recursion with meoization", fib_rec_memoization(10)
	print "fib with formula", fib_formula(10)
	import timeit
	print "fib(40) Bruteforce time",
	print timeit.timeit("fib_bruteforce(40)", setup="from __main__ import fib_bruteforce", number=1)
	print "fib(40) recursion time",
	print timeit.timeit("fib_rec(40)", setup="from __main__ import fib_rec", number=1)
	print "fib(40) dp or memoization time",
	print timeit.timeit("fib_rec_memoization(40)", setup="from __main__ import fib_rec_memoization", number=1)
	print "fib(40) formula time",
	print timeit.timeit("fib_formula(40)", setup="from __main__ import fib_formula", number=1)
