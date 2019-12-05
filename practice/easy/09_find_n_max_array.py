def find_n_max_array_brute_force(a, N): # O(N*n) where n is size of an array
	n_max = list()
	for _ in range(N):
		maxx = -float('inf')
		for ele in a:
			if ele > maxx and ele not in n_max:
				maxx = ele
		n_max.append(maxx)
	return n_max


def find_n_max_array_nlogn(a, N): # sorting nlogn + N = nlogn
	n_max = list()
	a.sort(reverse=True)
	for i in range(N):
		n_max.append(a[i])
	return n_max


if __name__ == "__main__":
	a = [4,5,9,8,12]
	N = 2
	print find_n_max_array_brute_force(a, N)
	print find_n_max_array_nlogn(a, N)