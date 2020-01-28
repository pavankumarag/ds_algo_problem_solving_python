"""
Quickselect is a selection algorithm to find the k-th smallest element in an unordered list.
It is related to the quick sort sorting algorithm.

Examples:

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 3
Output: 7

Input: arr[] = {7, 10, 4, 3, 20, 15}
           k = 4
Output: 10
"""


def partition(a, low, high): # this method remains same as quick sort
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


def kth_smallest(a, k):
	def kth_smallest_helper(a, left, right, k):
		index = partition(a, left, right)
		if index == k - 1:
			return a[index]
		if index > k - 1 :
			return kth_smallest_helper(a, left, index - 1, k)
		else:
			return kth_smallest_helper(a, index + 1, right, k)

	return kth_smallest_helper(a, 0, len(a) - 1, k)


if __name__ == "__main__":
	arr = [10, 4, 5, 8, 6, 11, 26]
	print kth_smallest(arr, 5)