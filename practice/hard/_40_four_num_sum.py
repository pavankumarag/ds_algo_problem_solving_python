#-* - coding:UTF - 8 -*-
"""
Find four elements that sum to a given value

Given an array of integers, find all combination of four elements in the array whose sum is equal to a given value X.
For example, if the given array is {10, 2, 3, 4, 5, 9, 7, 8} and X = 23,
then your function should print “3 5 7 8” (3 + 5 + 7 + 8 = 23).
"""


from collections import defaultdict


def find_four_n4(a, n, sum):
	for i in range(n):
		for j in range(i+1, n):
			for k in range(j+1, n):
				for l in range(k+1, n):
					if a[i] + a[j] + a[k] + a[l] == sum:
						print a[i], a[j], a[k], a[l]


def find_four_n2(a, n, k): # Takes O(n2), best possible
	d = defaultdict(list)
	for i in range(n):
		for j in range(i+1, n):
			sum = a[i] + a[j]
			if (k - sum) in d.keys():
				num = d[k - sum]
				print "four sum found", a[i], a[j], a[num[0]], a[num[1]]
		for l in range(i):
			d[a[i]+a[l]] = [i, l]


if __name__ == "__main__":
	a = [1,2,3,4,12,43,32,53,8,-10,4]
	find_four_n2(a, len(a),17)
	#find_four_n2(a, len(a), 59)
	find_four_n4(a, len(a),17)
