#-* - coding:UTF - 8 -*-
"""
Print Longest substring without repeating characters

Given a string, print the longest substring without repeating characters.
For example, the longest substrings without repeating characters for “ABDEFGABEF” are “BDEFGA” and “DEFGAB”, with
length 6. For “BBBB” the longest substring is “B”, with length 1.
The desired time complexity is O(n) where n is the length of the string
"""


def longest_substr(string):
	start_cur = 0 # starting point of current substring
	pos = {} # # Hash Map to store last occurrence of each already visited character
	start_max = 0 # starting index of maximum length substring
	max_len = 0 # maximum length substring without repeating characters
	n = len(string)
	pos[string[0]] = 0 # Last occurrence of first character is index 0
	for i in range(1, n):
		# If this character is not present in hash then this is first occurrence of this character
		if string[i] not in pos:
			pos[string[i]] = i
		else:
			# If this character is present in hash then this character has previous occurrence,
			# check if that occurrence is before or after starting point of current substring.
			if pos[string[i]] >= start_cur:
				# find length of current substring and update maxlen and start accordingly.
				cur_len = i - start_cur
				if max_len < cur_len:
					max_len = cur_len
					start_max = start_cur
				# Next substring will start after the last occurrence of current character to avoid its repetiion
				start_cur = pos[string[i]] + 1
			pos[string[i]] = i # Update last occurrence of current character
	# Compare length of last substring with maxlen and update maxlen and start accordingly
	if max_len < i - start_cur:
		max_len = i - start_cur
		start_max = start_cur
	return string[start_max : start_max + max_len]


if __name__ == "__main__":
	print longest_substr("GEEKSFORGEEKS")
	print longest_substr("ABDEFGABEF")
	print longest_substr("BBBB")
