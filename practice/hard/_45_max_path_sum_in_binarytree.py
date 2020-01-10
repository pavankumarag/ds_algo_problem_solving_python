"""
Given a binary tree, find the maximum path sum. The path may start and end at any node in the tree.

Example:

Input: Root of below tree
       1
      / \
     2   3
Output: 6

See below diagram for another example.
1+2+3

Reference: https://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/
"""


class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


def find_max_path(root):

	def find_max_path_util(root):
		if root is None:
			return 0
		l = find_max_path_util(root.left)
		r = find_max_path_util(root.right)
		max_single = max(max(l,r)+root.data, root.data)
		max_top = max(max_single, l+r+root.data)
		find_max_path_util.res = max(find_max_path_util.res, max_top)
		return max_single

	find_max_path_util.res = float('-inf')
	find_max_path_util(root)
	return find_max_path_util.res


if __name__ == "__main__":
	root = Node(10)
	root.left = Node(2)
	root.right = Node(10)
	root.left.left = Node(20)
	root.left.right = Node(1)
	root.right.right = Node(-25)
	root.right.right.left = Node(3)
	root.right.right.right = Node(4)
	print "Max path sum is ", find_max_path(root);