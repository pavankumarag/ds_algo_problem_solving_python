'''
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


class BinaryTree:
	def __init__(self):
		self.root = None

	def invert_rec(self, node):
		if node is None:
			return
		self.invert_rec(node.left)
		self.invert_rec(node.right)
		node.left, node.right = node.right, node.left

	def invert_iterative(self, node):
		if node is None:
			return
		queue = []
		queue.append(node)
		while len(queue):
			cur = queue.pop(0)
			if cur.left is not None:
				queue.append(cur.left)
			if cur.right is not None:
				queue.append(cur.right)
			cur.left, cur.right = cur.right, cur.left


	def inorder(self, node):
		if node is None:
			return
		self.inorder(node.left)
		print node.data,
		self.inorder(node.right)


if __name__ == "__main__":
	b = BinaryTree()
	b.root = Node(4)
	b.root.left = Node(2)
	b.root.left.left = Node(1)
	b.root.left.right = Node(3)
	b.root.right = Node(7)
	b.root.right.left = Node(6)
	b.root.right.right = Node(9)

	b.inorder(b.root)
	b.invert_rec(b.root)
	print
	b.inorder(b.root)
	b.invert_iterative(b.root)
	print
	b.inorder(b.root)



