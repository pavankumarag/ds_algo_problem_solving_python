def bubble_sort(a):
	for i in range(0, len(a) - 1):
		for j in range(i+1, len(a)):
			if a[i] > a[j]:
				a[i], a[j] = a[j], a[i]
	return a


def selection_sort(a):
	for i in range(len(a)):
		minn = i
		for j in range(i+1, len(a)):
			if a[j] < a[minn]:
				minn = j
		a[i], a[minn] = a[minn], a[i]
	return a


def insertion_sort(a):
	for i in range(1, len(a)):
		min = a[i]
		j = i-1
		while j >=0 and a[j] > min:
			a[j+1] = a[j]
			j -= 1
		a[j+1] = min
	return a


if __name__ == "__main__":
	a = [4,5,2,3,1]
	print bubble_sort(a)
	a = [10, 12, 13, 9, 8, 14, 2, 1, 3, 13]
	print bubble_sort(a)
	print selection_sort(a)
	print insertion_sort(a)