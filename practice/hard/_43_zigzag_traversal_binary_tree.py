"""
Write a function to print ZigZag order traversal of a binary tree.
For the below binary tree the zigzag order traversal will be 1 3 2 7 6 5 4
							1
				2						3
			7		6				5		4
"""
class Node:
	def __init__(self, data):
		self.data = data
		self.right = None
		self.left = None


def zigzag_traverse(root):
	if root is None: # Base Case
		return
	ltr = True # if ltr is true push nodes from left to right otherwise from right to left
	# Create two stacks to store current and next level
	current_level = []
	next_level = []
	current_level.append(root)
	while len(current_level) > 0:
		temp = current_level.pop()
		print temp.data,
		if ltr: # if ltr is true push left before right
			if temp.left:
				next_level.append(temp.left)
			if temp.right:
				next_level.append(temp.right)
		else:
			if temp.right:
				next_level.append(temp.right)
			if temp.left:
				next_level.append(temp.left)
		if len(current_level) == 0:
			ltr = not ltr # reverse ltr to push node in opposite order
			current_level, next_level = next_level, current_level # swapping of stacks 


if __name__ == "__main__":
	root = Node(1)
	root.left = Node(2)
	root.left.left = Node(7)
	root.left.right = Node(6)
	root.right = Node(3)
	root.right.left = Node(5)
	root.right.right = Node(4)
	zigzag_traverse(root)
