#-* - coding:UTF - 8 -*-
"""
Given a text and a wildcard pattern, find if wildcard pattern is matched with text. The matching should cover the
entire text (not partial text).

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

Example:

Text = "baaabab",
Pattern = “**ba**ab", output : true
Pattern = "baaa?ab", output : true
Pattern = "ba*a?", output : true
Pattern = "a*ab", output : false

Reference:
https://www.geeksforgeeks.org/wildcard-pattern-matching/
https://www.geeksforgeeks.org/dynamic-programming-wildcard-pattern-matching-linear-time-constant-space/
"""


def pattern_match(string, pattern, n, m): # has O(m x n) time and O(m x n) space complexity
	if m == 0: # empty pattern can only match with empty string
		return n == 0
	dp = [[False] * (m+1) for i in range(n+1)] # dp table for storing results of subproblems
	dp[0][0] = True # empty pattern can match with empty string
	for j in range(1, m+1): # Only '*' can match with empty string
		if pattern[j-1] == '*':
			dp[0][j] = dp[0][j-1]
	for i in range(1, n+1):  # fill the table in bottom-up fashion
		for j in range(1, m+1):
			# Two cases if we see a '*'
			# (a) We ignore '*'' character and move to next  character in the pattern i.e., '*' indicates an empty sequence
			# (b) '*' character matches with ith character in input
			if pattern[j-1] == '*':
				dp[i][j] = dp[i - 1][j] or dp[i][j-1]
			# Current characters are considered as matching in two cases
			# (a) current character of pattern is '?'
			# (b) characters actually match
			elif pattern[j-1] == '?' or string[i-1] == pattern[j-1]:
				dp[i][j] = dp[i - 1][j - 1]
			else: # If characters don't match
				dp[i][j] = False
	return dp[n][m]


def pattern_match_optimised(txt, pat, n, m):
	# empty pattern can only
	# match with empty sting
	# Base case
	if (m == 0):
		return (n == 0)

	# step 1
	# initailze markers :
	i = 0
	j = 0
	index_txt = -1
	index_pat = -1
	while (i < n - 2):

		# For step - (2, 5)
		if (j < m and txt[i] == pat[j]):
			i += 1
			j += 1

		# For step - (3)
		elif (j < m and pat[j] == '?'):
			i += 1
			j += 1

		# For step - (4)
		elif (j < m and pat[j] == '*'):
			index_txt = i
			index_pat = j
			j += 1

		# For step - (5)
		elif (index_pat != -1):
			j = index_pat + 1
			i = index_txt + 1
			index_txt += 1

		# For step - (6)
		else:
			return False
	# For step - (7)
	while (j < m and pat[j] == '*'):
		j += 1

	# Final Check
	if (j == m):
		return True

	return False


if __name__ == "__main__":
	string = "baaabab"
	pattern = "*****ba*****ab"
	print pattern_match(string, pattern, len(string), len(pattern))
	pattern = "**ba**ab"
	print pattern_match(string, pattern, len(string), len(pattern))
	pattern = "baaa?ab"
	print pattern_match(string, pattern, len(string), len(pattern))
	pattern = "ba*a?"
	print pattern_match(string, pattern, len(string), len(pattern))
	pattern = "a*ab"
	print pattern_match(string, pattern, len(string), len(pattern))

	print "Now using optimized\n"
	string = "baaabab"
	pattern = "*****ba*****ab"
	print pattern_match_optimised(string, pattern, len(string), len(pattern))
	pattern = "**ba**ab"
	print pattern_match_optimised(string, pattern, len(string), len(pattern))
	pattern = "baaa?ab"
	print pattern_match_optimised(string, pattern, len(string), len(pattern))
	pattern = "ba*a?"
	print pattern_match_optimised(string, pattern, len(string), len(pattern))
	pattern = "a*ab"
	print pattern_match_optimised(string, pattern, len(string), len(pattern))
