if __name__ == "__main__":
	a = [1, 3, 5, 6, 4, 2, 8]
	d = dict()
	K = 6
	found = 0
	for i in range(len(a)):
		d[a[i]] = i

	print(d)

	for i in range(len(a)):
		if ((K - a[i]) in d.keys()) and (d[K - a[i]] != i):
			found += 1
			print("Pair found %r %r" % (K - a[i], a[i]))

	if found > 0:
		print("There are total %d pairs found " % found)
	else:
		print("No pairs found ")
