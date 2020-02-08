#-* - coding: UTF - 8 -*-
"""
palindrome partitioning min cuts

Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a
 palindrome.

For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. Determine the fewest cuts needed
for palindrome partitioning of a given string. For example, minimum 3 cuts are needed for “ababbbabbababa”.
The three cuts are “a|babbbab|b|ababa”. If a string is palindrome, then minimum 0 cuts are needed.
If a string of length n containing all different characters, then minimum n-1 cuts are needed.
"""


def min_cut_partition(string): # O(n3)
	n = len(string)
	c = [[0 for i in range(n)] # C[i][j] = Minimum number of cuts needed for palindrome
					for i in range(n)]
	p = [[False for i in range(n)] # P[i][j] = true if substring str[i..j] is palindrome, else false
					for i in range(n)]
	# C[i][j] is 0 if P[i][j] is true

	j = 0; k = 0; l = 0
	for i in range(n): # Every substring of length 1 is a palindrome
		p[i][i] = True
		c[i][i] = 0
	# L is substring length. Solution in bottom up manner by considering all substrings of length starting from 2 to n.
	for l in range(2, n+1):
		for i in range(n-l+1): # For substring of length L, set different possible starting indexes
			j = i + l - 1 # Set ending index
			if l == 2: # If L is 2, then we just need to compare two characters
				p[i][j] = (string[i] == string[j])
			else: # else need to check two corner characters and value of P[i + 1][j-1]
				p[i][j] = (string[i] == string[j]) and p[i+1][j-1]

			if p[i][j] == True: # IF str[i..j] is palindrome, then C[i][j] is 0
				c[i][j] = 0
			else: # Make a cut at every possible location starting from i to j,and get the minimum cost cut
				c[i][j] = float('inf')
				for k in range(i, j):
					c[i][j] = min(c[i][j], c[i][k] + c[k+1][j] + 1)
	return c[0][n-1] # Return the min cut value for complete string. i.e., str[0..n-1]


if __name__ == "__main__":
	print min_cut_partition("ababbbabbababa")