'''
Find the Levenshtein Distance between two strings to transfer one string to another

For example, from "test" to "test" the Levenshtein distance is 0 because both the source and
target strings are identical. No transformations are needed. In contrast, from "test" to "team"
the Levenshtein distance is 2 - two substitutions have to be done to turn "test" in to "team".
'''

import numpy as np


def levenshtein_numpy(seq1, seq2):
	size_x = len(seq1) + 1
	size_y = len(seq2) + 1
	matrix = np.zeros((size_x, size_y))
	for x in xrange(size_x):
		matrix[x, 0] = x
	for y in xrange(size_y):
		matrix[0, y] = y

	for x in xrange(1, size_x):
		for y in xrange(1, size_y):
			if seq1[x - 1] == seq2[y - 1]:
				matrix[x, y] = min(
					matrix[x - 1, y] + 1,
					matrix[x - 1, y - 1],
					matrix[x, y - 1] + 1
				)
			else:
				matrix[x, y] = min(
					matrix[x - 1, y] + 1,
					matrix[x - 1, y - 1] + 1,
					matrix[x, y - 1] + 1
				)
	# print (matrix)
	return (matrix[size_x - 1, size_y - 1])


def lavenshtein_distance_iterative(str1, str2, m, n):
	matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for x in range(m + 1):
		matrix[x][0] = x
	for y in range(n + 1):
		matrix[0][y] = y
	for x in range(1, m + 1):
		for y in range(1, n + 1):
			if str1[x - 1] == str2[y - 1]:
				matrix[x][y] = min(matrix[x - 1][y] + 1, matrix[x][y - 1] + 1, matrix[x - 1][y - 1])
			else:
				matrix[x][y] = min(matrix[x - 1][y] + 1, matrix[x][y - 1] + 1, matrix[x - 1][y - 1] + 1)
	# print matrix
	return matrix[m][n]


def lavenshtein_distance_recursive(str1, str2, m, n):
	if m == 0:
		return n
	if n == 0:
		return m
	if str1[m - 1] == str2[n - 1]:
		return lavenshtein_distance_recursive(str1, str2, m - 1, n - 1)
	return 1 + min(lavenshtein_distance_recursive(str1, str2, m - 1, n - 1),
								 lavenshtein_distance_recursive(str1, str2, m, n - 1),
								 lavenshtein_distance_recursive(str1, str2, m - 1, n))


def lavenshtein_distance_dp(str1, str2, m, n):
	dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
	for x in range(m+1):
		for y in range(n+1):
			if x == 0:
				dp[x][y] = y
			elif y == 0:
				dp[x][y] = x
			elif str1[x-1] == str2[y-1]:
				dp[x][y] = dp[x-1][y-1]
			else:
				dp[x][y] = 1 + min(dp[x-1][y-1], dp[x-1][y], dp[x][y-1])
	return dp[m][n]

if __name__ == "__main__":
	str1 = "test"
	str2 = "team"
	print lavenshtein_distance_iterative(str1, str2, len(str1), len(str2))
	print lavenshtein_distance_recursive(str1, str2, len(str1), len(str2))
	print lavenshtein_distance_dp(str1 , str2, len(str1), len(str2))
	print lavenshtein_distance_recursive("saturday", "sunday", 8, 6)
	print levenshtein_numpy("saturday", "sunday")
	print lavenshtein_distance_iterative("saturday", "sunday", 8, 6)
	print lavenshtein_distance_dp("saturday", "sunday", 8, 6)
