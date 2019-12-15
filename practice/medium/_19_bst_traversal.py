class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class Tree:
	def __init__(self):
		self.root = None

	def inorder(self, node):
		if node is not None:
			self.inorder(node.left)
			print node.data,
			self.inorder(node.right)

	def postorder(self, node):
		if node is not None:
			self.postorder(node.left)
			self.postorder(node.right)
			print node.data,

	def preorder(self, node):
		if node is not None:
			print node.data,
			self.preorder(node.left)
			self.preorder(node.right)

	def bfs(self, node):
		if node is None:
			return
		queue = []
		queue.append(node)
		while len(queue):
			print queue[0].data,
			node = queue.pop(0)
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)


if __name__ == "__main__":
	b = Tree()
	b.root = Node(1)
	b.root.left = Node(2)
	b.root.right = Node(3)
	b.root.left.left = Node(4)
	b.root.left.right = Node(5)

	print "\nInorder Traversal"
	b.inorder(b.root)
	print "\nPreorder Traversal"
	b.preorder(b.root)
	print "\nPostorder Traversal"
	b.postorder(b.root)
	print "\nBSF or level order Traversal"
	b.bfs(b.root)