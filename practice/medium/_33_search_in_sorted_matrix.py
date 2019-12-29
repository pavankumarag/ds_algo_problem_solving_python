#-* - coding:UTF - 8 -*-
"""
Search element in a sorted matrix

Given a sorted matrix mat[n][m] and an element ‘x’. Find position of x in the matrix if it is present, else print -1. Matrix is sorted in a way such that all elements in a row are sorted in increasing order and for row ‘i’, where 1

Example:
Input : mat[][] = { {1, 5, 9}, {14, 20, 21}, {30, 34, 43} } x = 14 Output : Found at (1, 0)

Input : mat[][] = { {1, 5, 9, 11}, {14, 20, 21, 26}, {30, 34, 43, 50} } x = 42 Output : -1

https://www.geeksforgeeks.org/search-element-sorted-matrix/
"""
import numpy


def bruteforce_search(a, ele): # takes O(n*m) time
	n = len(a)
	m  = len(a[0])
	for i in range(n):
		for j in range(m):
			if a[i][j] == ele:
				return (i,j)
	return -1


def search_typecast_2D_to_1D(a, ele): # takes log(n*m) time
	npa = numpy.array(a)
	np_flatten = npa.flatten()
	ret = binary_search(np_flatten, ele)
	if ret != -1:
		print "ele found"
	else:
		print "ele not found"


def binary_search(a, ele):
	low = 0
	high = len(a) - 1
	while low <= high:
		mid = (low + high)/2
		if ele == a[mid]:
			return mid
		elif ele < a[mid]:
			high = mid - 1
		elif ele > a[mid]:
			low = mid + 1
	return -1


def search_sorted_matrix(a, ele): # Takes  O(log n + log m)
	"""
	Time complexity:. O(Log n) time is required to find the two desired rows.
	Then O(Log m) time is required for binary search in one of the four parts with size equal to m/2.
	"""
	n = len(a)
	m = len(a[0])
	if n == 1:
		return binary_search_matrix(a, ele, 0, 0, m-1)
	i_low = 0
	i_high = n - 1
	j_mid = m/2
	# Do binary search  in middle column. Condition to terminate the loop when the 2 desired rows are found
	while i_low+1  < i_high:
		i_mid = (i_low + i_high)/2
		if ele == a[i_mid][j_mid]:
			return (i_mid, j_mid)
		elif ele < a[i_mid][j_mid]:
			i_high = i_mid
		else:
			i_low = i_mid

	# If element is present on the mid of the two rows
	if a[i_low][j_mid] == ele:
		return i_low, j_mid
	elif a[i_low+1][j_mid] == ele:
		return i_low+1, j_mid

	# search element on 1st half of 1st row
	elif ele <= a[i_low][j_mid-1]:
		return binary_search_matrix(a, ele, i_low, 0, j_mid-1)
	# Search element on 2nd half of 1st row
	elif ele >= a[i_low][j_mid+1] and ele <= a[i_low][m-1]:
		return binary_search_matrix(a, ele,i_low, j_mid+1, m-1)
	# Search element on 1st half of 2nd row
	elif ele <= a[i_low+1][j_mid-1]:
		return binary_search_matrix(a, ele,i_low+1, 0, j_mid-1)
	# search element on 2nd half of 2nd row
	else:
		return binary_search_matrix(a, ele,i_low+1, j_mid+1, m-1)


def binary_search_matrix(a,ele, i, j_low, j_high):
	"""
	This function does Binary search for x in i-th row.
	It does the search from mat[i][j_low] to mat[i][j_high]
	:param a:
	:param ele:
	:param i:
	:param j_low:
	:param j_high:
	:return:
	"""
	while j_low <= j_high:
		j_mid = (j_low + j_high)/2
		if a[i][j_mid] == ele:
			#print "Ele found at %d,%d" %(i,j_mid)
			return (i, j_mid)
		elif ele < a[i][j_mid]:
			j_high = j_mid - 1
		elif ele > a[i][j_mid]:
			j_low = j_mid + 1
	return -1



if __name__ == "__main__":
	a = [[3,6,9],[11, 14,17],[19,26,29]]
	search_typecast_2D_to_1D(a, 14)
	search_typecast_2D_to_1D(a, 31)
	print bruteforce_search(a, 14)
	print bruteforce_search(a, 31)
	print search_sorted_matrix(a, 14)
	print search_sorted_matrix(a,31)

