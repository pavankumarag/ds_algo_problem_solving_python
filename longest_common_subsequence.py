

def lcs_recursion(x, y, m, n):
	if m==0 or n == 0:
		return 0
	elif x[m-1] == y[n-1]:
		return 1 + lcs_recursion(x,y,m-1,n-1)
	else:
		return max(lcs_recursion(x,y,m-1,n), lcs_recursion(x,y,m,n-1))


def lcm_dp(x, y):
	m = len(x)
	n = len(y)
	l = [[0] * (n+1) for i in range(m+1)]
	print l
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
	print lcm_dp(x,y)