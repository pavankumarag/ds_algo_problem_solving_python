# Given a binary tree and a number, return true if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given number. Return false if no such path can be found.


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


class Solution:
	def root_to_leaf_path_sum(self, root, sum_num):
		return self.root_left_path_sum_helper(root, sum_num)

	def root_left_path_sum_helper(self, node, rem_diff):
		if node is None:
			return False
		if node.left is None and node.right is None:
			if abs(node.data - rem_diff) == 0:
				return True
		if node.left is not None:
			if self.root_left_path_sum_helper(node.left, abs(node.data - rem_diff)):
				return True
		if node.right is not None:
			if self.root_left_path_sum_helper(node.right, abs(node.data - rem_diff)):
				return True
		return False


if __name__ == "__main__":
	root = Node(10)
	root.left = Node(8)
	root.right = Node(2)
	root.left.right = Node(5)
	root.left.left = Node(3)
	root.right.left = Node(2)
	solve = Solution()
	print solve.root_to_leaf_path_sum(root, 21)
	print solve.root_to_leaf_path_sum(root, 23)
	print solve.root_to_leaf_path_sum(root, 14)
	print solve.root_to_leaf_path_sum(root, 22)
	print solve.root_to_leaf_path_sum(root, 32)
