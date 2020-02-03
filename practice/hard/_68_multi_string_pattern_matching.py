"""
Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all
occurrences of pat[] in txt[]. You may assume that n > m


Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12

References:
https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
https://www.geeksforgeeks.org/optimized-naive-algorithm-for-pattern-searching/
"""


def search(pat, txt):
	M = len(pat)
	N = len(txt)

	# A loop to slide pat[] one by one */
	for i in range(N - M + 1):
		j = 0

		# For current index i, check
		# for pattern match */
		while j < M:
			if txt[i + j] != pat[j]:
				break
			j += 1
		if j == M:
			print("Pattern found at index ", i)


def search_optimised(pat, txt):
	M = len(pat)
	N = len(txt)
	i = 0
	while i <= N-M: # For current index i, check for pattern match
		for j in range(M):
			if txt[i+j] != pat[j]:
				break
			j += 1
		if j == M: # if pat[0...M-1] = txt[i,i+1,...i+M-1]
			print "Pattern found at index " + str(i)
			i = i + M
		elif j == 0:
			i =  i + 1
		else:
			i = i + j # slide the pattern by j

if __name__ == '__main__':
	txt = "AABAACAADAABAAABAA"
	pat = "AABA"
	search(pat, txt)
	search_optimised(pat, txt)