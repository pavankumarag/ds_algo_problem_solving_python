def two_sum_n2(a, k):
	pairs = list()
	for i in range(0, len(a)):
		if i != len(a) - 1:
			for j in range(i+1, len(a)):
				if a[i] + a[j] == k:
					pairs.append((a[i], a[j]))
					pairs.append((a[j], a[i]))
	# instead of set, can also check in above if that pair exists in list before adding
	return set(pairs)   #takes O(n)


def two_sum_nlogn(a, k):
	pairs = list()
	a.sort() # sort takes O(nlogn)
	for i in range(0, len(a)):
		if a[i] <= k :
			if binary_search(a[i+1:], k - a[i]) != -1:
				pairs.append((a[i], k - a[i]))
				pairs.append((k - a[i], a[i]))
		else:
			break
	# instead of set, can also check in above if that pair exists in list before adding
	return set(pairs)  #n and total time complexity is nlogn + logn + n = nlogn


def two_sum_n(a, k):
	pairs = list()
	d = dict()
	for i in range(0, len(a)):
		d[a[i]] = i   # takes O(n)
	for i in range(0, len(a)): # takes O(n)
		if k - a[i] in d.keys() and  d[k - a[i]] != i:
			pairs.append((a[i], k - a[i]))
			pairs.append((k - a[i], a[i]))
	# instead of set, can also check in above if that pair exists in list before adding
	return set(pairs)  # O(n), overall time complexity = O(n) + O(n) + O(n) = O(n)


def binary_search(a, ele): # takes O(logn)
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if a[mid] == ele:
			return mid
		elif ele < a[mid]:
			high = mid - 1
		elif ele > a[mid]:
			low = mid + 1
	return -1


if __name__ == "__main__":
	a = [1,2,6,5,3,4,0]
	k = 4
	print two_sum_n(a, k)
	print two_sum_nlogn(a, k)
	print two_sum_n2(a, k)