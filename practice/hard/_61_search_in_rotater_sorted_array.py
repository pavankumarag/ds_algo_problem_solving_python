"""
search in rotated sorted array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""


def find_in_sorted_array(a, ele):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if a[mid] == ele: # case 1 found x at mid position
			return mid
		if a[mid] <= a[high]: #case2: right part of array is sorted
			if ele <= a[high] and ele > a[mid]:
				low = mid + 1 # go search in right sorted half
			else:
				high = mid - 1
		elif a[low] <= a[mid]: # case 3 left half is sorted
			if ele <= a[mid] and ele >= a[low]: # go search in left sorted half
				high = mid - 1
			else:
				low = mid + 1
	return -1


if __name__ == "__main__":
	a = [12, 13, 14, 2, 3, 4]  # no duplicates, if duplicates then needs linear search
	print find_in_sorted_array(a, 13)
	print find_in_sorted_array(a, 3)

