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
	if f[n] != -1:
		return f[n]
	f[n] = fib_rec_memoization(n-1) + fib_rec_memoization(n-2)
	return f[n]


if __name__ == "__main__":
	for i in range(0,51):
		f.append(-1)
	f[0] = 0
	f[1] = 1
	print fib_bruteforce(10)
	print fib_rec(10)
	print fib_rec_memoization(10)
	import timeit
	print timeit.timeit("fib_linear(40)", setup="from __main__ import fib_linear", number=1)
	print timeit.timeit("fib_rec(40)", setup="from __main__ import fib_rec", number=1)
	print timeit.timeit("fib_rec_memoization(40)", setup="from __main__ import fib_rec_memoization", number=1)