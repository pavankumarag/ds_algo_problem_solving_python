def quick_sort(a):
	quick_sort_helper(a, 0, len(a)-1)


def quick_sort_helper(a, low, high):
	if low < high:
		pivot = partition(a, low, high)
		quick_sort_helper(a,low, pivot-1)
		quick_sort_helper(a, pivot+1, high)


def partition(a, low, high):
	pivot = a[low]
	done = False
	i = low + 1
	j = high
	while not done:
		while i <= j and a[i] <= pivot:
			i += 1
		while j >= i and a[j] >= pivot:
			j -= 1
		if j < i:
			done = True
		else:
			a[i], a[j] = a[j], a[i]
	a[low], a[j] = a[j], a[low]
	return j


if __name__ == "__main__":
	a = [4,5,2,3,9,10]
	print a
	quick_sort(a)
	print a

