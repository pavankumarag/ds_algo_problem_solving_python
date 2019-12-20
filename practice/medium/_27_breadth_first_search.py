from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def bfs(self, v):
		visited = [False] * (len(self.graph))
		queue = []
		queue.append(v)
		visited[v] = True
		while len(queue):
			s = queue.pop(0)
			print s,
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self):
		self.root = None

	def bfs(self, node):
		queue = []
		queue.append(node)
		while len(queue):
			node = queue.pop(0)
			print node.data,
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)


if __name__ == "__main__":
	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)
	print
	g.bfs(2)

	b = BinaryTree()
	b.root = Node(1)
	b.root.left = Node(2)
	b.root.right = Node(3)
	b.root.left.left = Node(4)
	b.root.left.right = Node(5)
	print
	b.bfs(b.root)