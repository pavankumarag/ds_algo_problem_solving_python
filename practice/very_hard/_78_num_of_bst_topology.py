#-*- coding:UTF - 8 -*-
"""
Total number of possible Binary Search Trees and Binary Trees with n keys

Total number of possible Binary Search Trees with n different keys
(countBST(n)) = Catalan number Cn = (2n)! / ((n + 1)! * n!)

For n = 0, 1, 2, 3, … values of Catalan numbers are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, ….
So are numbers of Binary Search Trees.

Total number of possible Binary Trees with n different keys (countBT(n)) = countBST(n) * n!
"""


def factorial(n):
	res = 1

	# Calculate value of [1*(2)*---* (n-k+1)] / [k*(k-1)*---*1]
	for i in range(1, n + 1):
		res *= i
	return res


def binomial_coeff(n, k):
	res = 1

	# Since C(n, k) = C(n, n-k)
	if (k > n - k):
		k = n - k

	# Calculate value of [n*(n-1)*---*(n-k+1)] /
	# [k*(k-1)*---*1]
	for i in range(k):
		res *= (n - i)
		res //= (i + 1)

	return res


# A Binomial coefficient based function to find nth catalan number in O(n) time
def catalan(n):
	# Calculate value of 2nCn
	c = binomial_coeff(2 * n, n)

	# return 2nCn/(n+1)
	return c // (n + 1)


# A function to count number of BST with n nodes using catalan
def count_bst(n):
	# find nth catalan number
	count = catalan(n)

	# return nth catalan number
	return count


# A function to count number of binary trees with n nodes
def count_bt(n):
	# find count of BST with n numbers
	count = catalan(n)

	# return count * n!
	return count * factorial(n)


if __name__ == '__main__':
	n = 5
	# find count of BST and binary trees with n nodes
	count1 = count_bst(n)
	count2 = count_bt(n)

	# print count of BST and binary trees with n nodes
	print("Count of BST with", n, "nodes is", count1)
	print("Count of binary trees with", n,
				"nodes is", count2)

