class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


def insert(root,node):
	if root is None:
		root = node
	else:
			if root.data < node.data:
					if root.right is None:
							root.right = node
					else:
							insert(root.right, node)
			else:
					if root.left is None:
							root.left = node
					else:
							insert(root.left, node)


def print_inorder(node):
	if node is None:
		return
	print_inorder(node.left)
	print node.data,
	print_inorder(node.right)


if __name__ == "__main__":
	a = [5,4,9.2,7]
	r = Node(50)
	insert(r, Node(30))
	insert(r, Node(20))
	insert(r, Node(40))
	insert(r, Node(70))
	insert(r, Node(60))
	insert(r, Node(80))
	print_inorder(r)



