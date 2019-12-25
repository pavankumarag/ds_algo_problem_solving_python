# https://www.geeksforgeeks.org/building-heap-from-array/


def heapify_max(arr, n, i):
	'''
	To max heapify a subtree rooted with node i which is an index in arr[]. N is size of heap
	'''
	largest = i # Initialize largest as root
	l = 2 * i + 1 # left child = 2*i + 1
	r = 2 * i + 2 # right child = 2*i + 2

	# If left child is larger than root
	if l<n and arr[l] > arr[largest]:
		largest = l
	# If right child is larger than largest so far
	if r<n and arr[r] > arr[largest]:
		largest = r
	if largest != i:  # If largest is not root
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify_max(arr, n, largest)


def heapify_min(arr, n, i):
	'''
	To min heapify a subtree rooted with node i which is an index in arr[]. N is size of heap
	'''
	smallest = i # Initialize smallest as root
	l = 2 * i + 1 # left child = 2*i + 1
	r = 2 * i + 2 # right child = 2*i + 2

	# If left child is lesser than root
	if l<n and arr[l] < arr[smallest]:
		smallest = l
	# If right child is lesser than smallest so far
	if r<n and arr[r] < arr[smallest]:
		smallest = r
	if smallest != i:  # If smallest is not root
		arr[i], arr[smallest] = arr[smallest], arr[i]
		heapify_min(arr, n, smallest)


def build_max_heap(arr, n):
	start_index = int((n/2)) - 1 # Index of last non-leaf node
	for i in range(start_index, -1, -1):
		heapify_max(arr, n, i)


def build_min_heap(arr, n):
	start_index = int((n/2)) - 1 # Index of last non-leaf node
	for i in range(start_index, -1, -1):
		heapify_min(arr, n, i)


def print_heap(arr, n):
	print "Array representation of heap"
	for i in range(n):
		print arr[i],
	print


if __name__ == "__main__":
	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
	n = len(arr)
	build_max_heap(arr, n)
	print_heap(arr, n)
	arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
	build_min_heap(arr, n)
	print_heap(arr, n)