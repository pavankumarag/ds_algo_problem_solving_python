'''
Smallest Difference pair of values between two unsorted Arrays


Given two arrays of integers, compute the pair of values (one value in each array) with the smallest (non-negative) difference. Return the difference.


Examples :

Input : A[] = {l, 3, 15, 11, 2}
        B[] = {23, 127, 235, 19, 8}
Output : 3
That is, the pair (11, 8)

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80}
Output : 10
That is, the pair (40, 50)
'''

import sys


def smallest_diff(A,B):
	A.sort()
	B.sort()
	result = sys.maxsize
	a=b=0
	while a < len(A) and b < len(B):
		if abs(A[a] - B[b]) < result:
			result = abs(A[a] - B[b])

		# Move Smaller Value
		if (A[a] < B[b]):
			a += 1
		else:
			b += 1
		# return final sma result
	return result


if __name__ == "__main__":
	A = [1, 2, 11, 5]
	B = [4, 12, 19, 23, 127, 235]
	print smallest_diff(A, B)
