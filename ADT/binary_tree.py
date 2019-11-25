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

	@staticmethod
	def find_min(node):
		while node.left is not None:
			node = node.left
		return node

	@staticmethod
	def delete_node(node, data):
		if node is None:
			return node
		elif data > node.data:
			node.right = BinaryTree.delete_node(node.right, data)
		elif data < node.data:
			node.left = BinaryTree.delete_node(node.left, data)
		else:
			if node.left is None and node.right is None: # case 1 No child
				node = None
			elif node.left is None:  # case 2 1 child
				temp = node.right
				node = None
				return temp
			elif node.right is None:
				temp = node.left
				node = None
				return temp
			else:
				temp = BinaryTree.find_min(node.right)
				node.data = temp.data
				node.right = BinaryTree.delete_node(node.right, temp.data)
		return node


def is_subtree_lesser(node, val):
	if node is None:
		return True
	if node.data <= val and is_subtree_lesser(node.left, val) and is_subtree_lesser(node.right, val):
		return True
	else:
		return False


def is_subtree_greater(node, val):
	if node is None:
		return True
	if node.data > val and is_subtree_greater(node.left, val) and is_subtree_greater(node.right, val):
		return True
	else:
		return False