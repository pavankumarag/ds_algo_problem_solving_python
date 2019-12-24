class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Solution 1 takes O(n) but traverses the tree 3 times plus extra spaces to path arrays
def find_LCA(root, n1, n2):
	path1 = []
	path2 = []
	if not find_path(root, path1, n1) or not find_path(root, path2, n2):
		return -1
	i=0
	while i < len(path1) and i < len(path2):
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]


def find_path(root, path, n):
	if root is None:
		return False
	path.append(root.data)
	if root.data == n:
		return True
	if (root.left is not None and find_path(root.left, path, n)) or \
					(root.right is not None and find_path(root.right, path, n)):
		return True
	path.pop()
	return False


# Solution 2 takes O(n) but traverses the tree 1 times plus no extra spaces to path arrays
def find_lca_optimized(root, n1, n2):
	v = [False, False]
	lca = find_lca_optimized_util(root, n1, n2, v)
	if v[0] and v[1] or v[0] and find(lca, n2) or v[1] and find(lca, n1):
		return lca
	return None


def find_lca_optimized_util(root, n1, n2, v):
	if root is None:
		return None
	if root.data == n1:
		v[0] = True
		return root
	if root.data == n2:
		v[1] = True
		return root
	left_lca = find_lca_optimized_util(root.left, n1, n2, v)
	right_lca = find_lca_optimized_util(root.right, n1, n2, v)
	if left_lca and right_lca:
		return root
	if left_lca is not None:
		return left_lca
	else:
		return right_lca


def find(root, n):
	if root is None:
		return None
	if root.data == n or find(root.left, n) or find(root.right, n) :
		return True
	return False


if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)

	print "LCA(4, 5) = %d" % (find_LCA(root, 4, 5, ))
	print "LCA(4, 6) = %d" % (find_LCA(root, 4, 6))
	print "LCA(3, 4) = %d" % (find_LCA(root, 3, 4))
	print "LCA(2, 4) = %d" % (find_LCA(root, 2, 4))

	print "LCA(4, 5) = %d" % find_lca_optimized(root, 4, 5).data
	print "LCA(4, 6) = %d" % find_lca_optimized(root, 4, 6).data
	print "LCA(3, 4) = %d" % find_lca_optimized(root, 3, 4).data
	print "LCA(2, 4) = %d" % find_lca_optimized(root, 2, 4).data
	print "LCA(4, 10) = %r" % find_lca_optimized(root, 4, 10)

