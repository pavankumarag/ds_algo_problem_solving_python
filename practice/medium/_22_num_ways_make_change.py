#!/usr/bin/python
# - * - coding: UTF - 8 -*-

'''
Given a value N, if we want to make change for N cents, and we have infinite supply of each of
 S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
So output should be 4. For N = 10 and S = {2, 5, 3, 6},
there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''


def count_recursion(s, m , n):
	if n == 0: # If n is 0 then there is 1, solution (do not include any coin)
		return 1
	if n < 0: # If n is less than 0 then no Solution exists
		return 0
	if m <= 0 and n >= 1: # If there are no coins and n is greater than 0, then no Solution exists
		return 0
	# count is sum of solutions (i)including S[m-1] (ii) excluding S[m-1]
	return count_recursion(s, m-1, n) + count_recursion(s, m, n-s[m-1])


def count_dp(s, m, n): # runs in O(mn) and takes O(m+n) auxiliary space
	# table is constructed in bottom up manner using the base case 0 value
	table = [[0 for _ in range(m)] for _ in range(n+1)]
	for i in range(m): # Fill the entries for 0 value case (n = 0)
		table[0][i] = 1
	for i in range(1, n+1):
		for j in range(m):
			x = table[i-s[j]][j] if i - s[j] >= 0 else 0 # Count of solutions including S[j]
			y = table[i][j-1] if j >= 1 else 0 # Count of solutions excluding S[j]
			table[i][j] = x + y # total count
	return table[n][m-1]


def count_dp_optimized(s, m, n): # takes O(n) auxiliary space
	table = [0 for _ in range(n + 1)] # table[i] will be storing the number of solutions for value i. We need n+1 rows
	# Base case (If given value is 0)
	table[0] = 1
	# Pick all coins one by one and update the table[] values after the index greater than or equal to the value of the
	# picked coin
	for i in range(0, m):
		for j in range(s[i], n+1):
			table[j] += table[j-s[i]]
	return table[n]


if __name__ == "__main__":
	s = [1,2,3]
	N = 4
	print count_recursion(s, len(s), N)
	print count_dp(s, len(s), N)
	print count_dp_optimized(s, len(s), N)