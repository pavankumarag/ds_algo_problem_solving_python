'''
Given an array of integers, find the maximum sum of subsequence of given array where subsequence contains
no adjacent elements.

Example:

Input: {1,2,9,4,5,0,4,11,6}
output: Maximum sum is 26 formed by the subsequence {1,9,5,11}
'''


def max_sum_subarray_non_adjacent(a, i, prev, n): # runs in O(n)
	if i == n:  # Base case: all elements are processed
		return 0
	excl = max_sum_subarray_non_adjacent(a, i+1, prev, n) # recursion by excluding current element
	incl = 0
	if prev+1 != i: # include cur ele only if it is not adjacent to prev ele considered
		incl = max_sum_subarray_non_adjacent(a, i+1, i, n) + a[i]
	return max(excl, incl) # return max sum we obtain by including and excluding cur ele


def max_sum_subarray_dp(a, n): # runs in O(n) and takes O(n) space
	'''The idea is to create auxiliary array lookup[] to store solutions of sub problems
	In the bottom-up approach we will solve the smaller sub problems first and the larger sub problem'''
	if n == 1: # base case
		return a[0]
	lookup = list() # lookup[i] stores max sum possible till index i
	lookup.append(a[0])  # Trivial case
	lookup.append(max(a[0], a[1]))
	for i in range(2, n):
		# 1. excluding cur ele & take max sum till i-1
		# 2. including cur ele a[i] and take max sum till i-2
		lookup_i = max(lookup[i-1], lookup[i-2] + a[i])
		lookup.append(max(lookup_i, a[i])) # if cur ele is more than the max sum till cur ele
	return lookup[n-1] # return max sum


def max_sum_subarray_dp_opt_space(a, n): # runs in O(n) and takes O(1) space
	'''
	constant space dp to calculate max sum subarray of non adjacent elements
	'''
	if n == 1:
		return a[0]
	prev_prev = a[0]
	prev = max(a[0], a[1])
	for i in range(2, n):
		curr = max(a[i], max(prev, prev_prev + a[i]))
		prev_prev = prev
		prev = curr
	return prev


if __name__ == "__main__":
	a = [1,2,9,4,5,0,4,11,6]
	print max_sum_subarray_non_adjacent(a, 0, -float('inf'), len(a))
	print max_sum_subarray_dp(a, len(a))
	print max_sum_subarray_dp_opt_space(a, len(a))