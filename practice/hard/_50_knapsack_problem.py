# -* - coding:UTF - 8 -*-
"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value
in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and
 weights associated with n items respectively. Also given an integer W which represents knapsack capacity,
 find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
 You cannot break an item, either pick the complete item, or don’t pick it
"""


def knapsack_recursive(W, wt, val, n):
	"""
	Time complexity of this naive recursive solution is exponential (2^n).
	"""
	if n == 0 or W == 0:  # Base Case
		return 0
	# If weight of the nth item is more than Knapsack of capacity W, then this item can't be included in the optimal sol.
	if wt[n - 1] > W:
		return knapsack_recursive(W, wt, val, n - 1)
	# return the maximum of two cases:
	# (1) nth item included
	# (2) not included
	return max(val[n - 1] + knapsack_recursive(W - wt[n - 1], wt, val, n - 1), knapsack_recursive(W, wt, val, n - 1))


def knapsack_dp(W, wt,val, n):
	dp = [[0 for x in range(W+1)] for x in range(n+1)]
	for i in range(n+1): # Build table dp[][] in bottom up manner
		for w in range(W+1):
			if i==0 or w == 0:
				dp[i][w] = 0
			elif wt[i-1]<=w:
				dp[i][w] = max(val[i-1]+dp[i-1][w-wt[i-1]], dp[i-1][w])
			else:
				dp[i][w] = dp[i-1][w]
	return dp[n][W]


if __name__ == "__main__":
	val = [60, 100, 120]
	wt = [10, 20, 30]
	W = 50
	n = len(val)
	print knapsack_recursive(W, wt, val, n)
	print knapsack_dp(W, wt, val, n)
