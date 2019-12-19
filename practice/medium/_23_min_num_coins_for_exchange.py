'''
Given a value V, if we want to make change for V cents, and we have infinite supply of each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents'''


def min_coins_recursion(coins, m , V):
	if V == 0:
		return 0
	res = float('inf')
	for i in range(0, m):
		if coins[i] <= V:
			sub_res = min_coins_recursion(coins, m, V-coins[i])
			if sub_res != float('inf') and sub_res+1 < res:
				res = sub_res + 1
	return res


def min_coins_dp(coins, m, V):
	table = [ 0 for _ in range(V+1)]
	table[0] = 0
	for i in range(1, V+1):
		table[i] = float('inf')
	for i in range(1, V+1):
		for j in range(m):
			if coins[j] <= i:
				sub_res = table[i-coins[j]]
				if sub_res != float('inf') and sub_res+1 < table[i]:
					table[i] = sub_res + 1
	return table[V]


if __name__ == "__main__":
	coins = [1, 2, 5]
	V = 11
	print min_coins_recursion(coins, len(coins), V)
	print min_coins_dp(coins, len(coins), V)
