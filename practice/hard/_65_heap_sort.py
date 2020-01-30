"""
One of the main reasons Heap Sort is still used fairly often, even though it's often outperformed by a well-implemented
Quick Sort, is its reliability.

Heap Sort's main advantage here are the O(n*logn) upper bound as far as time complexity is concerned, and security
concerns. Linux kernel developers give the following reasoning to using Heap Sort over Quick Sort:

Sorting time of Heap Sort is O(n*logn) both on average and worst-case. While qsort is about 20% faster on average,
it suffers from an exploitable O(n*n) worst-case behavior and extra memory requirements that make it less suitable
for kernel use.

Furthermore, Quick Sort behaves poorly in predictable situations, and given enough knowledge of the internal
implementation, it could create a security risk (mainly DDoS attacks) since the bad O(n2) behavior could easily be
triggered.

Another algorithm that Heap Sort is often compared to is Merge Sort, which has the same time complexity.

Merge Sort has the advantage of being stable and intuitively parallelizable, while Heap Sort is neither.

Another note is that Heap Sort is slower than Merge Sort in most cases, even though they have the same complexity,
since Heap Sort has larger constant factors.

Heap Sort can, however, be implemented much more easily in-place than Merge Sort can, so it's preferred when memory is
a more important factor than speed.
"""
def heapify(arr, n, i):
	"""
	to build max heap
	"""
	largest = i
	l = 2*i +1
	r = 2*i + 2

	if l < n and arr[l] > arr[largest]: # See if left child of root exists and is greater than root
		largest = l
	if r < n and arr[r] > arr[largest]: # See if right child of root exists and is greater than root
		largest = r
	if largest != i: # Change root, if needed
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, n, largest) # Heapify the root


def heap_sort(arr): # in-place, no need of extra space
	n = len(arr)
	for i in range(n, -1, -1): # Build a max heap
		heapify(arr, n, i)
	for i in range(n-1, 0, -1): # one by one swap with arr[0] and heapify
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)


def heap_sort_2(arr): # using built in functions and extra space
	from heapq import heappush, heappop
	heap = []
	for ele in arr:
		heappush(heap, ele)
	ordered = []
	while heap:
		ordered.append(heappop(heap))
	return ordered


if __name__ == "__main__":
	arr = [12, 11, 13, 5, 6, 7]
	print "Input array", arr
	heap_sort(arr)
	print "heap sorted", arr
	arr = [12, 11, 13, 5, 6, 7]
	print "Input array", arr
	print "heap sorted", heap_sort_2(arr)

