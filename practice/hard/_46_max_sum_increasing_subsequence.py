"""
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence
of the given array such that the integers in the subsequence are sorted in increasing order.
For example, if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100),
if the input array is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the
input array is {10, 5, 4, 3}, then output should be 10
"""


def max_sum_increasing_subsequence(a, n): # runs in O(n2)
	max = -float('inf')
	dp = [0 for i in range(n)]
	for i in range(n):
		dp[i] = a[i]
	for i in range(1, n):
		for j in range(i):
			if a[i] > a[j] and dp[i] < dp[j] + a[i]:
				dp[i] = dp[j] + a[i]
	for i in range(n):
		if max < dp[i]:
			max = dp[i]
	return max


if __name__ == "__main__":
	arr = [1, 101, 2, 3, 100, 4, 5]
	n = len(arr)
	print(max_sum_increasing_subsequence(arr,n))
