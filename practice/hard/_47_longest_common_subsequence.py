#-* - coding:UTF - 8 -*-
"""
longest common subsequence(LCS)

LCS Problem Statement: Given two sequences, find the length of longest subsequence present in both of them.
A subsequence is a sequence that appears in the same relative order, but not necessarily contiguous.
For example, “abc”, “abg”, “bdf”, “aeg”, ‘”acefg”, .. etc are subsequences of “abcdefg”.

Examples:
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""


def lcs_recursion(x, y, m, n):
	if m==0 or n == 0:
		return 0
	elif x[m-1] == y[n-1]:
		return 1 + lcs_recursion(x,y,m-1,n-1)
	else:
		return max(lcs_recursion(x,y,m-1,n), lcs_recursion(x,y,m,n-1))


def lcs_dp(x, y):
	m = len(x)
	n = len(y)
	l = [[0] * (n+1) for i in range(m+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i ==0 and j == 0:
				l[i][j] = 0
			elif x[i-1] == y[j-1]:
				l[i][j] = 1 + l[i-1][j-1]
			else:
				l[i][j] = max(l[i-1][j], l[i][j-1])
	return l[m][n]


if __name__ == "__main__":
	x = "AGGTAB"
	y = "GXTXAYB"
	print lcs_recursion(x, y, len(x), len(y))
	print lcs_dp(x,y)
	x = "ABCDGH"
	y = "AEDFHR"
	print lcs_dp(x, y)