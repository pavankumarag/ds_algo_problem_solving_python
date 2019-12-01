from collections import defaultdict


class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add_edge(self, u, v):
		self.graph[u].append(v)

	def dfs(self, v):
		visited = [False] * (len(self.graph))
		self.dfs_util(v, visited)

	def dfs_util(self, v, visited):
		visited[v] = True
		print v,
		for i in self.graph[v]:
			if visited[i] == False:
				self.dfs_util(i, visited)


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self):
		self.root = None
		self.inorder_list = []

	def inorder_traversal(self, node):
		if node is not None:
			self.inorder_traversal(node.left)
			print node.data,
			self.inorder_list.append(node.data)
			self.inorder_traversal(node.right)

	def preorder_traversal(self, node):
		if node is not None:
			print node.data,
			self.preorder_traversal(node.left)
			self.preorder_traversal(node.right)

	def postorder_traversal(self, node):
		if node is not None:
			self.postorder_traversal(node.left)
			self.postorder_traversal(node.right)
			print node.data,

if __name__ == "__main__":
	b = BinaryTree()
	b.root = Node(1)
	b.root.left = Node(2)
	b.root.right = Node(3)
	b.root.left.left = Node(4)
	b.root.left.right = Node(5)

	print "\nInorder Traversal"
	b.inorder_traversal(b.root)
	print "\nPreorder Traversal"
	b.preorder_traversal(b.root)
	print "\nPostorder Traversal"
	b.postorder_traversal(b.root)

	g = Graph()
	g.add_edge(0, 1)
	g.add_edge(0, 2)
	g.add_edge(1, 2)
	g.add_edge(2, 0)
	g.add_edge(2, 3)
	g.add_edge(3, 3)

	print "\nDepth First Traversl of a Graph\n"
	g.dfs(2)