#-* - coding:UTF - 8 -*-
"""
Given an array arr[0..n-1] of positive and negative numbers we need to find if there is a cycle in array with given
rules of movements. If a number at an i index is positive, then move arr[i]%n forward steps, i.e., next index to
visit is (i + arr[i])%n.

Conversely, if it’s negative, move backward arr[i]%n steps i.e., next index to visit is (i – arr[i])%n.
Here n is size of array. If value of arr[i]%n is zero, then it means no move from index i.

Examples:

Input: arr[] = {2, -1, 1, 2, 2}
Output: Yes
Explanation: There is a loop in this array
because 0 moves to 2, 2 moves to 3, and 3
moves to 0.

Input  : arr[] = {1, 1, 1, 1, 1, 1}
Output : Yes
Whole array forms a loop.

Input  : arr[] = {1, 2}
Output : No
We move from 0 to index 1. From index
1, there is no move as 2%n is 0. Note that
n is 2.

Note that self loops are not considered a cycle. For example {0} is not cyclic.
"""


def is_cycle(a, n):
	def is_cycle_recur(v, adj, visited, recur):
		visited[v] = True
		recur[v] = True
		for i in range(len(adj[v])):
			if visited[adj[v][i]] == False:
				if is_cycle_recur(adj[v][i], adj, visited, recur):
					return True
				elif visited[adj[v][i]] == True and recur[adj[v][i]] == True:
					return True
		recur[v] = False
		return False

	adj = [[] for i in range(n)]
	for i in range(n):
		if i != (i + a[i] + n)%n:
			adj[i].append((i+a[i]+n)%n)

	visited = [False] * n
	recur = [False] * n
	for i in range(n):
		if visited[i] == False:
			if is_cycle_recur(i, adj, visited, recur):
				return True
	return False


if __name__ == "__main__":
	a = [2, -1, 1, 2, 2]
	print is_cycle(a, len(a))
	a = [1, 2]
	print is_cycle(a,len(a))