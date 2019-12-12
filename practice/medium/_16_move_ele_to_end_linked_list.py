'''
Move all occurrences of an element to end in a linked list
Given a linked list and a key in it, the task is to move all occurrences of given key to end of linked list,
keeping order of all other elements same.

Examples:

Input  : 1 -> 2 -> 2 -> 4 -> 3
         key = 2
Output : 1 -> 4 -> 3 -> 2 -> 2

Input  : 6 -> 6 -> 7 -> 6 -> 3 -> 10
         key = 6
Output : 7 -> 3 -> 10 -> 6 -> 6 -> 6
'''


class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


def move_to_end(node, key):
	tail = node
	while tail.next is not None:
		tail = tail.next
	last = tail
	prev = prev2 = None
	cur = node
	while cur != tail:
		if cur.data != key and prev2 is None:
			prev = cur
			cur = cur.next
			node = cur
			last.next = prev
			last = last.next
			last.next = None
			prev = None
		else:
			if cur.data == key and prev2 is not None:
				prev = cur
				cur = cur.next
				prev2.next = cur
				last.next = prev
				last = last.next
				last.next = None
			elif cur != tail:
				prev2 = cur
				cur = cur.next
	return node


def print_list(node):
	temp = node
	while temp is not None:
		print temp.data,
		temp = temp.next


if __name__ == "__main__":
	head = Node(1)
	head.next = Node(2)
	head.next.next = Node(2)
	head.next.next.next = Node(4)
	head.next.next.next.next = Node(3)
	key = 2
	print_list(head)
	head = move_to_end(head, key)
	print
	print_list(head)


