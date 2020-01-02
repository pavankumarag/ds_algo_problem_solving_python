"""
Group Anagrams from given list

Anagrams are the words that are formed by similar elements but the orders in which these characters occur differ

Example:

The original list : ['lump', 'eat', 'me', 'tea', 'em', 'plum']
The grouped Anagrams : [['me', 'em'], ['lump', 'plum'], ['eat', 'tea']]
"""


def group_anagrams(lst):
	occurrence = dict()
	for string in lst:
		sorted_str = "".join(sorted(string))
		if sorted_str in occurrence.keys():
			occurrence[sorted_str].append(string)
		else:
			occurrence[sorted_str] = list()
			occurrence[sorted_str].append(string)
	return occurrence.values()


def group_anagrams_2(lst):
	from itertools import groupby
	temp = lambda test_list : sorted(test_list)
	result = []
	for key, val in groupby(sorted(lst, key=temp), temp):
		result.append(list(val))
	return result


if __name__ == "__main__":
	print group_anagrams(['lump', 'eat', 'me', 'tea', 'em', 'plum'])
	print group_anagrams_2(['lump', 'eat', 'me', 'tea', 'em', 'plum'])