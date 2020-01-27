#-* - coding: UTF - 8 -*-
"""
Given a sorted array of integers A(0 based index) of size N, find the starting and ending position of a given
integar B in array A.

Your algorithm’s runtime complexity must be in the order of O(log n).

Return an array of size 2, such that first element = starting position of B in A and second element = ending position
 of B in A, if B is not found in A return [-1, -1].


For Example

Input 1:
    A = [5, 7, 7, 8, 8, 10]
    B = 8
Output 1:
    [3, 4]
Explanation 1:
    First occurence of 8 in A is at index 3
    Second occurence of 8 in A is at index 4
    ans = [3, 4]

Input 2:
    A = [5, 17, 100, 111]
    B = 3
Output 2:
    [-1, -1]
"""


def binary_search(a, ele, occurence="default"):
	low = 0
	high = len(a) - 1
	index = -1
	while low <= high:
		mid = (low + high) / 2
		if a[mid] == ele:
			index = mid
			if occurence == "default":
				return index
			elif occurence == "first":
				high = mid -1
			elif occurence == "last":
				low = mid + 1
		elif ele > a[mid]:
			low = mid + 1
		else:
			high = mid - 1
	return index


def find_range(a, ele):
	first_index = binary_search(a, ele, occurence="first")
	if first_index == -1:
		return [-1, -1]
	last_index = binary_search(a, ele, occurence="last")
	if first_index == last_index:
		return [first_index, -1]
	else:
		return [first_index, last_index]


if __name__ == "__main__":
	print find_range([3,5,6,6,6,7,8,9], 6)
	print find_range([3, 5, 6, 7, 8, 9], 6)
	print find_range([3, 5, 7, 8, 9], 6)