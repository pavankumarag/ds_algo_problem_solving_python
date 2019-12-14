INT_MAX = 4294967296
INT_MIN = -4294967296


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


# Approach 1 is straight forward but less efficient takes O(n2)
def is_bst1(root):
	if root is None:
		return True
	if (is_subtree_lesser(root.left, root.data) and is_subtree_greater(root.right, root.data)
			and is_bst1(root.left) and is_bst1(root.right)):
		return True
	else:
		return False

# Approach 2, more efficient and takes O(n)
def is_bst2(node, min, max):
	if node is None:
		return True
	if node.data < min or node.data > max:
		return False
	return is_bst2(node.left, min, node.data - 1) and is_bst2(node.right, node.data + 1, max)


# Approach 3, check if inorder traversal of bst is sorted

if __name__ == "__main__":
	b = BinaryTree()
	b.root = Node(4)
	b.root.left = Node(2)
	b.root.right = Node(5)
	b.root.left.left = Node(1)
	b.root.left.right = Node(3)
	print "\nMethod 1: Recursively check left subtreee is less than root + right subtree is great then root, inefficient\n"
	if is_bst1(b.root):
		print "BST"
	else:
		print "Not BST"

	print "\nMethod 2: Inorder traveral can identify BST\n"
	b.inorder_traversal(b.root)
	if sorted(b.inorder_list) == b.inorder_list:
		print "BST"
	else:
		print "Not BST"

	print "\nMethod 3: Efficient with O(n)\n"
	if is_bst2(b.root, INT_MIN, INT_MAX):
		print "BST"
	else:
		print "Not BST"
