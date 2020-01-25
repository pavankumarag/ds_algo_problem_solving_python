"""
Interleaving of two given strings with no common characters

Given three strings A, B and C. Write a function that checks whether C is an interleaving of A and B.
It may be assumed that there is no common character between A and B, C is said to be interleaving A and B,
if it contains all characters of A and B and order of all characters in individual strings is preserved.

Example
Input: str1 = "AB",  str2 = "CD"
For all the below Str3 values, str3 is interleaved of 1 and 2
    ABCD
    ACBD
    ACDB
    CABD
    CADB
    CDAB
"""


def is_c_interleaved(a, b, c):
	i=0
	j=0
	k=0
	for k in range(len(c)):
		if i < len(a) and a[i] == c[k]:
			i+=1
		elif j < len(b) and b[j] == c[k]:
			j+=1
		else:
			return False
	print i,j
	if i != len(a) or j != len(b):
		return False
	return True


if __name__ == "__main__":
	print is_c_interleaved("AB", "CD", "ACBG")
	print is_c_interleaved("AB", "CD", "CABD")
