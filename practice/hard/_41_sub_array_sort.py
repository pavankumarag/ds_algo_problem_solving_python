#-* - coding:UTF - 8 -*-
"""
Sorting array except elements in a subarray

Given an array A positive integers, sort the array in ascending order such that element in given subarray
(start and end indexes are input) in unsorted array stay unmoved and all other elements are sorted.

Examples :

Input : arr[] = {10, 4, 11, 7, 6, 20}
            l = 1, u = 3
Output : arr[] = {6, 4, 11, 7, 10, 20}
We sort elements except arr[1..3] which
is {11, 7, 6}.

Input : arr[] = {5, 4, 3, 12, 14, 9};
            l = 1, u = 2;
Output : arr[] = {5, 4, 3, 9, 12, 14 }
"""


def sort_subarray(a, l, u, n):
	b = list()
	for i in range(l):
		b.append(a[i])
	for i in range(u+1, n):
		b.append(a[i])
	b.sort()
	for i in range(l):
		a[i] = b[i]
		k = i
	k += 1
	for i in range(u+1, n):
		a[i] = b[k]
		k += 1
	print a


if __name__ == "__main__":
	a = [10, 4, 11, 7, 6, 20]
	sort_subarray(a, 1, 3, len(a))
	a = [5, 4, 3, 12, 14, 9]
	sort_subarray(a, 1, 2, len(a))
	a = [5, 4, 3, 12, 14, 9]
	sort_subarray(a, 2, 4, len(a))