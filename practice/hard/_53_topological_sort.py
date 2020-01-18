#-*- coding: utf - 8 -*-
"""
Topological Sorting


Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every
directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible
if the graph is not a DAG.

For example, a topological sorting of the following graph is “5 4 2 3 1 0”.
There can be more than one topological sorting for a graph.

For example, another topological sorting of the following graph is “4 5 2 3 1 0”.
The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming edges).

Reference: https://www.geeksforgeeks.org/topological-sorting/
"""

from collections import defaultdict


class Graph:
	def __init__(self, vertices):
		self.graph = defaultdict(list)
		self.V = vertices

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def topological_sort(self):

		def topological_sort_util(v, visited, stack):
			visited[v] = True
			for i in self.graph[v]:
				if visited[i] == False:
					topological_sort_util(i, visited, stack)
			stack.insert(0, v)

		visited = [False] * self.V
		stack = []
		for i in range(self.V):
			if visited[i] == False:
				topological_sort_util(i, visited, stack)
		return stack


if __name__ == "__main__":
	g = Graph(6)
	g.add_edge(5, 2)
	g.add_edge(5, 0)
	g.add_edge(4, 0)
	g.add_edge(4, 1)
	g.add_edge(2, 3)
	g.add_edge(3, 1)
	print g.topological_sort()

