#-*- coding: UTF-8 -*-
"""
Smallest window that contains all characters of string itself

Given a string, find the smallest window length with all distinct characters of the given string.
For eg. str = “aabcbcdbca”, then the result would be 4 as of the smallest window will be “dbca” .

Examples:

Input  : aabcbcdbca
Output : dbca
Explanation :
dbca of length 4 is the smallest
window with highest number of distinct
characters.

Input : aaab
Output : ab
Explanation :
ab of length 2 is the smallest window
with highest number of distinct characters.
"""

from collections import defaultdict

MAX_CHARS = 256


def findSubString(str):
	"""
	# Function to find smallest window  containing  all distinct characters
	"""
	n = len(str)

	# Count all distinct characters.
	dist_count = len(set([x for x in str]))

	#. We basically maintain a window of characters that contains all characters of given string.
	count, start, start_index, min_len = 0, 0, -1, 9999999999
	curr_count = defaultdict(lambda: 0)
	for j in range(n):
		curr_count[str[j]] += 1
		# If any distinct character matched, then increment count
		if curr_count[str[j]] == 1:
			count += 1

		# Try to minimize the window i.e., check if any character is occurring more no. of times  than its occurrence in
		# pattern, if yes then remove it from starting and also remove the useless characters.
		if count == dist_count:
			while curr_count[str[start]] > 1:
				if curr_count[str[start]] > 1:
					curr_count[str[start]] -= 1
				start += 1

			# Update window size
			len_window = j - start + 1
			if min_len > len_window:
				min_len = len_window
				start_index = start

	# Return substring starting from start_index and length min_len """
	return str[start_index: start_index + min_len]


if __name__== '__main__':
	print("Smallest window containing all distinct characters is {}"
				.format(findSubString("aabcbcdbca")))