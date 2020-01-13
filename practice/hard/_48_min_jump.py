"""
Minimum number of jumps to reach end
Given an array of integers where each element represents the max number of steps that can be made forward
from that element. Write a function to return the minimum number of jumps to reach the end of the array
(starting from the first element). If an element is 0, then cannot move through that element.

Example:

Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
Output: 3 (1-> 3 -> 8 ->9)
First element is 1, so can only go to 3. Second element is 3, so can make at most 3 steps eg to 5 or 8 or 9.
"""


def min_jum_naive(a, l , h):
	if h == l: # base case when source and destination are same
		return 0
	if a[l] == 0: # when nothing is reachable from given source
		return float('inf')
	min = float('inf')
	# Traverse through all the points reachable from arr[l]. Recursively get the minimum number of jumps
	for i in range(l+1, h+1):
		if i < l+a[l]+1:
			jumps = min_jum_naive(a,i,h)
			if jumps != float('inf') and jumps+1 < min:
				min = jumps+1
	return min


def min_jum_dp(a, n):
	dp = [0 for i in range(n)]
	if n == 0 or a[0] == 0:
		return float('inf')
	for i in range(1, n):
		dp[i] = float('inf')
		for j in range(i):
			if i <= j+a[j] and dp[j] != float('inf'):
				dp[i] = min(dp[i], dp[j]+1)
				break
	return dp[n-1]


if __name__ == "__main__":
	a=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
	print min_jum_naive(a, 0, len(a) - 1)
	print min_jum_dp(a, len(a))

